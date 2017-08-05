"""
Requires Pillow (PIL)

This program is easiest to use if you have Microsoft Dual Monitor tools.
You dont have to use it, but it lets you determine the pixel positioning of
your monitors. You can also trial and error calibrate this, or find it other
ways.

This app was designed for dual screens of roughly the same size, but
different resilutions.

You can also just set pairs of the split images as your backgrounds,
but then you cant have a slideshow running (need individual images)

I made my measurements in the correct system of measurement, by inches should
work just fine too (i hope).

Remember to set the wallpapers to tile (sanity check)

* I might add in the ability to account for the bezels/gap between monitors in
  the future.
_______________________________________________________________________________
         ________________
      ^  |                |  ______________         } Vertical offset, V
      |  |    left mon    | |   right mon  |  ^
  H1  |  |    R1H & R1W   | |   R2H & R2W  |  | H2
      |  |                | |______________|  v
      v  |________________|
                            <------W2------>
         <--------W1------>
_______________________________________________________________________________
STEPS
1. measure physical positions of your Monitors
2. check resolutions of Monitors
3. input parameters below, and save.
4. Create a parent folder where you want to work. Then create three child
   folders called 'input', 'dual' and 'output' and place slicer.py at the same
   at that level. Place the photos you want to convert into 'input'.
   eg;
        parent >    dual       >
                    output     >
                    slicer.py
                    input      >    ultrawidewallpaper1.png
                                    ultrawidewallpaper2.png
                                    ultrawidewallpaper1.jpg
                                            etc...
5. run slicer.py after installing Pillow/PIL and image_slicer.
6. set location of displays in 'Display settings' (right click desktop)
    -set the right screen to be at: R1H*(1-(H2/H1)). This value will be printed
     out for you after filling in the input parameters. NOTE THAT 0 IS LOCATED
     AT THE TOP OF THE SCREEN. REFERENCE POINT IS TOP.
    -you can 'fine tune' by editing a registry key
        -the reg key is at
        -HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Configuration\
            -edit Position.cy for the right screen (in the example case)
            - The multiple display configs listed here are memories of you
              swapping out other monitors. IF you cant tell which one is the
              current set up, delete all the subfolders here (the one in
              Configuration with the crazy names), sign out, sign back in, and
              a just the current active config file will be regenerated. edit
              position.cy. you can tell which screen is which by reading the
              data column. Sign out/in again.
"""
import glob, os
from PIL import Image

##############  INPUT PARAMETERS  ###################
H1 = 34 #height of first (left) monitor
H2 = 29 #width of first (left) monitor

W1 = 62 #height of second (right) monitor
W2 = 52 #width of second (right) monitorV

R1W = 3840#horizontal resolution of first monitor
R1H = 2160 #vertical resolution of first monitor

R2W = 1920#horizontal resolution of second monitor
R2H = 1080#vertical resolution of second monitor

V = 1.5 #vertical offset between tops of monitors.
######################################################

M2H = R1H*((1.0*V/H1)) #the pixel height that monitor 2 should be at.
print 'monitor 2 should be placed at: '+str(int(M2H))
i = 1
for file0 in glob.glob("./splitterinput/*.*"): #this is the folder where you put the pictures you want to adapt for dual screens.
    if file0[-4:] == '.png' or file0[-4:] == '.jpg' :
        print 'now processing: '+str(file0)
        width = R1W+R2W #input widths of a proper image generated from MS DualWallpaper
                     #this should be the width of your two monitors combined (pixels)
        height = max(R1H, R2H, R2H + M2H) #height of your tallest monitor. If your monitors are offset,
                                          # This could be improved
                      # then it should be the total height of both monitors, minus the overlap.

        new_im = Image.new('RGB', (width, height))

        picture = Image.open(file0)
        #image 1
        x_offset = 0 #shouldnt need to change this
        y_offset = 0 #change this if left monitor is lower than right
                     # DMT (dual monitor tools) by MS can tell you what the
                     # offsets should be. DMT>>Monitors>>working

        left    = 0
        bottom  = picture.size[1]
        right   = picture.size[0]/2 #take a horizontal part of the image,
                                             #that is proportional to the screen size
        top     = 0
        leftim = picture.crop(( left , top , right , bottom ))  #resolution of left screen
        leftim = leftim.resize((R1W,R1H))
        new_im.paste(leftim, (x_offset,0))

        #image 2
        picture2 = Image.open(file0)
        x_offset += int(leftim.size[0]) #place next to left im
        y_offset = int(M2H) #relative position of the monitors

        xratio = 1.0*W1/W2
        yratio = 1.0*H1/H2

        toplevel    = int(picture2.size[1]*V/H1)
        bottomlevel = int(picture2.size[1]*(V+H2)/H1)

        left    = picture.size[0]*W1/(W1+W2) #crop off whats on the left screen
        bottom  = bottomlevel
        right   = picture2.size[0]

        top     = toplevel

        rightim = picture2.crop(( left , top , right , bottom ))  #resolution of left screen
        rightim = rightim.resize((R1W,R1H))

        scaledH = int(yratio*R2H)
        scaledW = int(xratio*R2W)

        rightim = rightim.resize((R2W,R2H))

        new_im.paste(rightim, (x_offset,y_offset))

        new_im.save('./output/'+file0[16:])
        print str(i) + ' images complete'
        i +=1
    else: #the file is not a jpg or png
        print 'file '+file0+' is not a .png or .jpg. Skipping...'
        continue
