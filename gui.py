from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import sys
from dicom import *

from tomograf import *
import pydicom


# PARAMETRY:
WIDTH_WINDOW = 1300
HEIGHT_WINDOW = 800
WIDTH_IMAGE = 375
HEIGHT_IMAGE = 375

step = 3  # kroki
d = 115   # ilosc detektorow
beta = 300  # kat miedzy 1 a ostatnim detektorem
iterations = 360 // step  # liczba iteracji (emiterow) z uwzglednieniem kata pomiedzy nimi

input_image = cv2.imread("image1.jpg")
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
dicom_read("wynik.dcm")
# ds=pydicom.dcmread('plik.dcm')
# dcm_sample=ds.pixel_array*128
# input_image = cv2.cvtColor(dcm_sample, cv2.COLOR_BGR2GRAY)

def update_step(event):
    step = scale_step.get()
    d = scale_detector.get()
    beta = scale_beta.get()
    scale_iterations.configure(to=len(range(0, 360, step)))
    scale_iterations.set(len(range(0, 360, step)))
    iterations = scale_iterations.get()

    label_status.config(text="Czekanie...", fg="black")
    label_status.place(x=WIDTH_WINDOW - 325, y=HEIGHT_WINDOW - 125)
    f.update()
    sinogram, output_image = tomograf(input_image, step, d, beta, iterations)
    label_status.config(text="Zrobione!", fg="green")
    label_status.place(x=WIDTH_WINDOW - 325, y=HEIGHT_WINDOW - 125)

    new_sinogram = Image.fromarray(sinogram)
    resized_new_sinogram = new_sinogram.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
    new_sinogram = ImageTk.PhotoImage(resized_new_sinogram)
    f.itemconfig(sinogram_on_canvas, image=new_sinogram)

    new_output_image = Image.fromarray(output_image)
    resized_new_output_image = new_output_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
    new_output_image = ImageTk.PhotoImage(resized_new_output_image)
    f.itemconfig(output_image_on_canvas, image=new_output_image)

    root.mainloop()


def update_detector(event):
    step = scale_step.get()
    d = scale_detector.get()
    beta = scale_beta.get()
    iterations = scale_iterations.get()

    label_status.config(text="Czekanie...", fg="black")
    label_status.place(x=WIDTH_WINDOW - 325, y=HEIGHT_WINDOW - 125)
    f.update()
    sinogram, output_image = tomograf(input_image, step, d, beta, iterations)
    label_status.config(text="Zrobione!", fg="green")
    label_status.place(x=WIDTH_WINDOW - 325, y=HEIGHT_WINDOW - 125)

    new_sinogram = Image.fromarray(sinogram)
    resized_new_sinogram = new_sinogram.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
    new_sinogram = ImageTk.PhotoImage(resized_new_sinogram)
    f.itemconfig(sinogram_on_canvas, image=new_sinogram)

    new_output_image = Image.fromarray(output_image)
    resized_new_output_image = new_output_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
    new_output_image = ImageTk.PhotoImage(resized_new_output_image)
    f.itemconfig(output_image_on_canvas, image=new_output_image)

    root.mainloop()


def update_beta(event):
    step = scale_step.get()
    d = scale_detector.get()
    beta = scale_beta.get()
    iterations = scale_iterations.get()

    label_status.config(text="Czekanie...", fg="black")
    label_status.place(x=WIDTH_WINDOW - 395, y=HEIGHT_WINDOW - 125)
    f.update()
    sinogram, output_image = tomograf(input_image, step, d, beta, iterations)
    label_status.config(text="Zrobione!", fg="green")
    label_status.place(x=WIDTH_WINDOW - 325, y=HEIGHT_WINDOW - 125)

    new_sinogram = Image.fromarray(sinogram)
    resized_new_sinogram = new_sinogram.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
    new_sinogram = ImageTk.PhotoImage(resized_new_sinogram)
    f.itemconfig(sinogram_on_canvas, image=new_sinogram)

    new_output_image = Image.fromarray(output_image)
    resized_new_output_image = new_output_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
    new_output_image = ImageTk.PhotoImage(resized_new_output_image)
    f.itemconfig(output_image_on_canvas, image=new_output_image)

    root.mainloop()


def update_iterations(event):
    step = scale_step.get()
    d = scale_detector.get()
    beta = scale_beta.get()
    iterations = scale_iterations.get()

    label_status.config(text="Czekanie...", fg="black")
    label_status.place(x=WIDTH_WINDOW - 325, y=HEIGHT_WINDOW - 125)
    f.update()
    sinogram, output_image = tomograf(input_image, step, d, beta, iterations)
    label_status.config(text="Zrobione!", fg="green")
    label_status.place(x=WIDTH_WINDOW - 325, y=HEIGHT_WINDOW - 125)

    new_sinogram = Image.fromarray(sinogram)
    resized_new_sinogram = new_sinogram.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
    new_sinogram = ImageTk.PhotoImage(resized_new_sinogram)
    f.itemconfig(sinogram_on_canvas, image=new_sinogram)

    new_output_image = Image.fromarray(output_image)
    resized_new_output_image = new_output_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
    new_output_image = ImageTk.PhotoImage(resized_new_output_image)
    f.itemconfig(output_image_on_canvas, image=new_output_image)

    root.mainloop()


root = Tk()
root.title("Tomograf")
root.resizable(0, 0)

width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()

x_position = (width_screen / 2) - (WIDTH_WINDOW / 2)
y_position = (height_screen / 2) - (HEIGHT_WINDOW / 2)

root.geometry('%dx%d+%d+%d' % (WIDTH_WINDOW, HEIGHT_WINDOW, x_position, y_position))

f = Canvas(root, width=WIDTH_WINDOW, height=HEIGHT_WINDOW)
f.pack()

'''button = Button(text="EXIT", width=20, height=2)
button.pack()
button.place(x=330, y=530)'''

sinogram, output_image = tomograf(input_image, step, d, beta, iterations)

label_step = Label(root, text="Krok:")
label_step.pack()
label_step.place(x=50, y=530)
scale_step = Scale(root, from_=1, to=90, orient=HORIZONTAL, length=565)
scale_step.set(step)
scale_step.pack()
scale_step.place(x=250, y=510)
scale_step.bind("<ButtonRelease-1>", update_step)

label_detector = Label(root, text="Rzuty na detektory:")
label_detector.pack()
label_detector.place(x=50, y=580)
scale_detector = Scale(root, from_=1, to=1000, orient=HORIZONTAL, length=565)
scale_detector.set(d)
scale_detector.pack()
scale_detector.place(x=250, y=560)
scale_detector.bind("<ButtonRelease-1>", update_detector)

label_beta = Label(root, text="Kąt rozwarcia:")
label_beta.pack()
label_beta.place(x=50, y=630)
scale_beta = Scale(root, from_=1, to=360, orient=HORIZONTAL, length=565)
scale_beta.set(beta)
scale_beta.pack()
scale_beta.place(x=250, y=610)
scale_beta.bind("<ButtonRelease-1>", update_beta)

label_iterations = Label(root, text="Liczba iteracji:")
label_iterations.pack()
label_iterations.place(x=50, y=680)
scale_iterations = Scale(root, from_=1, to=(len(range(0, 360, step))), orient=HORIZONTAL, length=565)
scale_iterations.set(iterations)
scale_iterations.pack()
scale_iterations.place(x=250, y=660)
scale_iterations.bind("<ButtonRelease-1>", update_iterations)

def zapis(dane):
    f = open("zapis.txt", "w")
    f.write(dane)

def dicom():

    label_dicom = Label(text="Patient Name")
    label_dicom.pack()
    label_dicom.place(x=50, y=500)
    tkWindow = Tk()
    tkWindow.geometry('400x150')

    imieLabel = Label(tkWindow, text="Imie").grid(row=0, column=0)
    nazwiskoLabel = Label(tkWindow, text="Nazwisko").grid(row=1, column=0)
    komentarzLabel = Label(tkWindow, text="Komentarz").grid(row=2, column=0)
    ID_pacjentaLabel = Label(tkWindow, text="ID").grid(row=3, column=0)
    dataLabel = Label(tkWindow, text="Data").grid(row=4, column=0)


    imie = StringVar()
    nazwisko = StringVar()
    komentarz = StringVar()
    ID_pacjenta = StringVar()
    data = StringVar()


    imieEntry = Entry(tkWindow, textvariable=imie).grid(row=0, column=1)
    nazwiskoEntry = Entry(tkWindow, textvariable=nazwisko).grid(row=1, column=1)
    komentarzEntry = Entry(tkWindow, textvariable=komentarz).grid(row=2, column=1)
    ID_pacjentaEntry = Entry(tkWindow, textvariable=ID_pacjenta).grid(row=3, column=1)
    dataEntry = Entry(tkWindow, textvariable=data).grid(row=4, column=1)

    dane = 'Imie: '
    dane += str(imie)
    dane += '\nNazwisko: '
    dane += str(nazwisko)
    dane += '\nID_pacjenta: '
    dane += str(ID_pacjenta)
    dane += '\nkomentarz: '
    dane += str(komentarz)
    dane += '\ndata: '
    dane += str(data)

    loginButton = Button(tkWindow, text="Zapisz", command=zapis(dane)).grid(row=5, column=0)

dicom()

label_input_image = Label(root, text="Obraz_wejściowy:")
label_input_image.pack()
label_input_image.place(x=165, y=50)
display_image = Image.fromarray(input_image)
resized = display_image.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
display_image = ImageTk.PhotoImage(resized)
f.create_image(212, 300, image=display_image)

label_sinogram = Label(root, text="Sinogram:")
label_sinogram.pack()
label_sinogram.place(x=595, y=50)
input_image2 = Image.fromarray(sinogram)
resized2 = input_image2.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
input_image2 = ImageTk.PhotoImage(resized2)
sinogram_on_canvas = f.create_image(624, 300, image=input_image2)

label_output_image = Label(root, text="Obraz_wyjściowy:")
label_output_image.pack()
label_output_image.place(x=985, y=50)
input_image3 = Image.fromarray(output_image)
resized3 = input_image3.resize((WIDTH_IMAGE, HEIGHT_IMAGE), Image.NEAREST)
input_image3 = ImageTk.PhotoImage(resized3)
output_image_on_canvas = f.create_image(1036, 300, image=input_image3)

label_status = Label(root, text="Zrobione!", fg="green", font=("Courier", 32))
label_status.pack()
label_status.place(x=WIDTH_WINDOW - 325, y=HEIGHT_WINDOW - 125)


root.mainloop()