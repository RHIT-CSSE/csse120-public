"""
Example showing for tkinter and ttk how to:
  -- Read an IMAGE from a FILE (jpeg, png, gif, ...)
  -- Resize that image
  -- Put the image on a Button, Canvas, ...

Note: This example requires that you install the PILLOW library.
If you have not already done so, install PILLOW like this:
   File ~ Settings
   Expand Project, then select Python Interpreter
   On the right-hand-side, find and select the little  +   sign
      (you may have to make the window wider to see it)
   In the dialog that pops up, type    pillow   and select it,
     make the  Install to user's site-packages ...   checkbox be UN-checked,
     then press the Install Package button.
     (If the install fails, try again with that checkbox checked.)

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk
from PIL import Image, ImageTk


def main():
    # The usual tkinter.Tk, ttk.Frame, and also a BLUE tkinter.Canvas.
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    canvas = tkinter.Canvas(main_frame, width=700, height=350,
                            background="blue")
    canvas.grid()

    # The next line assumes that the file named  queen_of_hearts.jpeg
    # is in the current folder and that the file named  QueenofHearts.png
    # is in a subfolder of the current folder named  Cards.
    # Change the names/pathnames as needed for your own files.
    image_jpeg = Image.open("queen_of_hearts.jpeg")
    image_png = Image.open("Cards/QueenofHearts.png")

    # The following lines are not necessary. They just show image size et al.
    print(image_png.format, image_png.size, image_png.mode)
    print(image_jpeg.format, image_jpeg.size, image_jpeg.mode)

    # Resize/crop the images to:
    #   -- image1: the JPEG image, unchanged
    #   -- image2: the JPEG image, stretched to be 300 wide by 100 tall
    #   -- image3: the PNG image, reduced to 1/20 of its original size
    #   -- image4: the PNG image, reduced, then cropped to get rid of the black
    image1 = image_jpeg
    image2 = image_jpeg.resize((300, 100))
    image3 = image_png.resize((image_png.size[0] // 20,
                               image_png.size[1] // 20))
    image4 = image3.crop((35, 25, 110, 135))

    # The following makes tkinter images from the Pillow images.
    # Use tkinter images in all your  tkinter/ttk  code.
    tk_image1 = ImageTk.PhotoImage(image1)
    tk_image2 = ImageTk.PhotoImage(image2)
    tk_image3 = ImageTk.PhotoImage(image3)
    tk_image4 = ImageTk.PhotoImage(image4)

    # Put the four tkinter images onto a Canvas and one onto a Button, where
    # the Canvas coordinates are for the CENTER of the image (by default):
    canvas.create_image(100, 150, image=tk_image1)
    canvas.create_image(350, 75, image=tk_image2)
    canvas.create_image(350, 200, image=tk_image3)
    canvas.create_image(600, 100, image=tk_image4)

    button1 = ttk.Button(main_frame, image=tk_image1)
    button1.grid()
    button1['command'] = lambda: print('hello')

    root.mainloop()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
