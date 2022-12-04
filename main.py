from tkinter import *
from tkinter import filedialog
from math import sqrt
import customtkinter
from PIL import ImageColor
from PIL import PngImagePlugin
from PIL import ImageTk, Image
import numpy
import os


def CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount):
    distanceToEdge: float = 199 * scale
    minX: float = middleX - distanceToEdge
    minY: float = middleY - distanceToEdge
    z: float = minY
    i: float = minX
    roundtrackerX = 0
    roundtrackerY = 1
    imagePosX = 1
    imagePosY = 399

    evenRgb = ImageColor.getrgb(userInputEven)
    oddRgb = ImageColor.getrgb(userInputOdd)
    exceededRgb = ImageColor.getrgb(userInputExceeded)

    data = numpy.zeros((400, 400, 3), dtype=numpy.uint8)

    while True:
        if roundtrackerY == 400:
            print("We are all done here")
            break
        while True:
            roundtrackerX = roundtrackerX + 1
            round(i)
            returnValue = CalculateMandel(i, z, maxAmount)
            i = i + scale
            # odds
            if returnValue == 1:
                data[imagePosY, imagePosX] = oddRgb
                imagePosX = imagePosX + 1
            # evens
            elif returnValue == 0:
                data[imagePosY, imagePosX] = evenRgb
                imagePosX = imagePosX + 1
            # exceeded
            elif returnValue == 2:
                data[imagePosY, imagePosX] = exceededRgb
                imagePosX = imagePosX + 1
            if roundtrackerX == 399:
                roundtrackerX = 0
                imagePosY = imagePosY - 1
                imagePosX = 1
                z = z + scale
                round(z)
                roundtrackerY = roundtrackerY + 1
                i = minX
                break
    image = Image.fromarray(data)
    imageCounter = 1
    while True:
        imagePath = "Mandelbrots/Mandel" + str(imageCounter) + ".png"
        isExist = os.path.exists(imagePath)
        if isExist:
            imageCounter += 1
        else:
            break
    image.save(imagePath)
    # create metadata
    info = PngImagePlugin.PngInfo()
    info.add_text("middleX", str(middleX))
    info.add_text("middleY", str(middleY))
    info.add_text("scale", str(scale))
    info.add_text("userInputEven", userInputEven)
    info.add_text("userInputOdd", userInputOdd)
    info.add_text("userInputExceeded", userInputExceeded)
    info.add_text("maxAmount", str(maxAmount))
    image.save(imagePath, "PNG", pnginfo=info)
    # use created metadata to update information in GUI
    entry1.configure(placeholder_text=str(middleX))
    entry2.configure(placeholder_text=str(middleY))
    entry3.configure(placeholder_text=str(scale))
    entry4.configure(placeholder_text=str(userInputEven))
    entry5.configure(placeholder_text=str(userInputOdd))
    entry6.configure(placeholder_text=str(userInputExceeded))
    entry7.configure(placeholder_text=str(maxAmount))

    img = Image.open(imagePath)
    img = img.resize((399, 399), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img, width=399, height=399)
    panel.image = img
    panel.bind("<Button-1>",
               lambda event: Zoom(event, middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded,
                                  maxAmount))
    panel.bind("<Button-3>",
               lambda event: Zoomout(event, middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded,
                                     maxAmount))


def Zoom(eventorigin, middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount):
    global x, y
    x = eventorigin.x
    y = eventorigin.y
    print(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)

    if x == 200 & y == 200:
        return

    if x > 399:
        x = 399
    if x < 1:
        x = 1
    if y > 399:
        y = 399
    if y < 1:
        y = 1

    if x > 200:
        pixelDifference = x - 200
        distance = pixelDifference * scale
        print(middleX)
        tempX = middleX + distance
        print(distance, tempX)
        if middleY > 200:
            pixelDifference = y - 200
            distance = pixelDifference * scale
            middleY = middleY + distance
            scale = scale - 0.001
            print(x, y, middleX, middleY)
            CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)
        else:
            pixelDifference = 200 - y
            distance = pixelDifference * scale
            middleY = middleY - distance
            scale = scale - 0.001
            print(x, y, middleX, middleY)
            CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)
    else:
        pixelDifference = 200 - x
        distance = pixelDifference * scale
        middleX = middleX - distance
        if middleY > 200:
            pixelDifference = 200 - y
            distance = pixelDifference * scale
            middleY = middleY + distance
            scale = scale - 0.001
            print(x, y, middleX, middleY)
            CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)
        else:
            pixelDifference = y - 200
            distance = pixelDifference * scale
            middleY = middleY - distance
            scale = scale - 0.001
            print(x, y, middleX, middleY)
            CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)


def Zoomout(eventorigin, middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount):
    global x, y
    x = eventorigin.x
    y = eventorigin.y
    print(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)

    if x == 200 & y == 200:
        return

    if x > 399:
        x = 399
    if x < 1:
        x = 1
    if y > 399:
        y = 399
    if y < 1:
        y = 1

    if x > 200:
        pixelDifference = x - 200
        distance = pixelDifference * scale
        print(middleX)
        tempX = middleX + distance
        print(distance, tempX)
        if middleY > 200:
            pixelDifference = y - 200
            distance = pixelDifference * scale
            middleY = middleY + distance
            scale = scale + 0.001
            print(x, y, middleX, middleY)
            CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)
        else:
            pixelDifference = 200 - y
            distance = pixelDifference * scale
            middleY = middleY - distance
            scale = scale + 0.001
            print(x, y, middleX, middleY)
            CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)
    else:
        pixelDifference = 200 - x
        distance = pixelDifference * scale
        middleX = middleX - distance
        if middleY > 200:
            pixelDifference = 200 - y
            distance = pixelDifference * scale
            middleY = middleY + distance
            scale = scale + 0.001
            print(x, y, middleX, middleY)
            CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)
        else:
            pixelDifference = y - 200
            distance = pixelDifference * scale
            middleY = middleY - distance
            scale = scale + 0.001
            print(x, y, middleX, middleY)
            CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)


def CalculateMandel(currentX, currentY, maxAmount):
    a: float = 0
    b: float = 0
    mandelGetal: float = 0

    while True:
        if mandelGetal == maxAmount:
            outcomeNumber = 2
            break
        tempA: float = a * a - b * b + currentX
        tempB: float = 2 * a * b + currentY
        a = tempA
        b = tempB
        numbersSquared: float = a * a + b * b
        distance = sqrt(numbersSquared)
        if distance > 2:
            mandelGetal += 1
            if (mandelGetal % 2) == 0:
                outcomeNumber = 0
                break
            elif (mandelGetal % 2) != 0:
                outcomeNumber = 1
                break
        mandelGetal += 1
    return outcomeNumber


def exportVariables():
    middleX = float(entry1.get())
    middleY = float(entry2.get())
    scale = float(entry3.get())
    userInputEven = entry4.get()
    userInputOdd = entry5.get()
    userInputExceeded = entry6.get()
    maxAmount = float(entry7.get())
    CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)


def openMandelbrot():
    imagePath = filedialog.askopenfile()
    im = Image.open(imagePath.name)
    middleX = float(im.info["middleX"])

    middleY = float(im.info["middleY"])
    scale = float(im.info["scale"])
    userInputEven = (im.info["userInputEven"])
    userInputOdd = (im.info["userInputOdd"])
    userInputExceeded = (im.info["userInputExceeded"])
    maxAmount = float(im.info["maxAmount"])
    CalculatePositions(middleX, middleY, scale, userInputEven, userInputOdd, userInputExceeded, maxAmount)


# GUI Stuff
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("MandelbrotC")
root.geometry("600x700")
root.maxsize(600, 700)
root.minsize(600, 700)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

grid = customtkinter.CTkFrame(master=frame)
grid.pack(pady=1, fill="y", expand=True)

label1 = customtkinter.CTkLabel(grid, text="midden x:")
label2 = customtkinter.CTkLabel(grid, text="midden y:")
label3 = customtkinter.CTkLabel(grid, text="schaal:")
label4 = customtkinter.CTkLabel(grid, text="kleur even:")
label5 = customtkinter.CTkLabel(grid, text="kleur oneven:")
label6 = customtkinter.CTkLabel(grid, text="kleur > max aantal:")
label7 = customtkinter.CTkLabel(grid, text="max aantal:")

entry1 = customtkinter.CTkEntry(grid, placeholder_text="0")
entry2 = customtkinter.CTkEntry(grid, placeholder_text="0")
entry3 = customtkinter.CTkEntry(grid, placeholder_text="0.01")
entry4 = customtkinter.CTkEntry(grid, placeholder_text="zwart")
entry5 = customtkinter.CTkEntry(grid, placeholder_text="wit")
entry6 = customtkinter.CTkEntry(grid, placeholder_text="zwart")
entry7 = customtkinter.CTkEntry(grid, placeholder_text="100", width=100, )
button = customtkinter.CTkButton(grid, text="GO!", command=exportVariables, width=50)
buttonOpen = customtkinter.CTkButton(grid, text="Open Mandelbrot", command=openMandelbrot, width=50)

label1.grid(row=2, column=1)
entry1.grid(row=2, column=2)
label2.grid(row=3, column=1)
entry2.grid(row=3, column=2)
label3.grid(row=4, column=1)
entry3.grid(row=4, column=2)
label4.grid(row=5, column=1)
entry4.grid(row=5, column=2)
label5.grid(row=6, column=1)
entry5.grid(row=6, column=2)
label6.grid(row=7, column=1)
entry6.grid(row=7, column=2)
label7.grid(row=8, column=1)
entry7.grid(row=8, column=2)
button.grid(row=9, column=2)
buttonOpen.grid(row=9, column=3)

imageFrame = customtkinter.CTkFrame(master=frame)
imageFrame.pack()
img = Image.open("Mandelbrots/default.png")
img = img.resize((399, 399), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(imageFrame, image=img, width=399, height=399)
panel.image = img
panel.bind("<Button-1>",
           lambda event: Zoom(event, 0, 0, 0.01, "#000000", "#FFFFFF", "#000000",
                              100))
panel.bind("<Button-3>",
           lambda event: Zoomout(event, 0, 0, 0.01, "#000000", "#FFFFFF", "#000000", 100))
panel.pack()

root.mainloop()
