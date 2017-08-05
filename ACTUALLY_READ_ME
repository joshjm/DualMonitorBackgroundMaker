THIS IS COPIED FORM THE PYTHON FILES INTRO. GO EDIT THE PYTHON FILES AND READ THE FOLLOWING EITHER HERE, OR THERE. ITS IMPORTANT YO.

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
