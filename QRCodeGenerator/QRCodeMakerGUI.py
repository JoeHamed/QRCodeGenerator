import qrcode
import tkinter
from customtkinter import *
from PIL import Image
color_options = ["black", "white", "red", "pink", "orange", "yellow", "purple", "green", "blue", "brown"]
def create_qr(data, fill_clr, bg_clr, ver):

    QR = qrcode.QRCode(version=ver,
                       box_size=20,
                       border=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L)
    try:
        if data != 0:
            QR.add_data(data)
            QR.make()
            QRCodeImage = QR.make_image(fill_color=fill_clr, back_color=bg_clr)
            QRCodeImage.save("QRCodeImage.png")

    except:
        pass

    # The version parameter is an integer from 1 to 40 that controls the size of the QR Code

    # The error_correction parameter controls the error correction used for the QR Code.
    # ERROR_CORRECT_L ---> About 7% or less errors can be corrected.
    # ERROR_CORRECT_M ---> About 15% or less errors can be corrected (default).
    # ERROR_CORRECT_Q ---> About 25% or less errors can be corrected.
    # ERROR_CORRECT_H ---> About 30% or less errors can be corrected.

    # The box_size parameter controls how many pixels each “box” of the QR code is.


def get_data():
    data = ''
    try:
        if data_entry.get():
            data = str(data_entry.get())
            print(data)
        else:
            return 0
    except:
        pass
    return data

def create_qr_canvas(data):
    qr_canvas = CTkCanvas(master=frame)
    # qr_canvas.delete('all')
    try:
        if data != 0:
            my_image = CTkImage(light_image=Image.open('QRCodeImage.png'),
                                              dark_image=Image.open('QRCodeImage.png'),
                                              size=(400, 400))  # WidthxHeight

            my_label = CTkLabel(master=frame, text="", image=my_image)
            my_label.grid(column=1, row=0, columnspan=1, rowspan=5, pady=40, padx=30)
    except:
        pass

# Create main window

app = CTk()
app.title("QR Code Maker")
set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
set_appearance_mode("system")  # light or dark depending on your system
window_width = 1000
window_height = 600
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
# width x height + x + y
app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
app.resizable(False, False)


var1 = tkinter.StringVar()
var1.set("Enter the data to convert")
var2 = tkinter.StringVar()
var2.set("Fill color")
var3 = tkinter.StringVar()
var3.set("Back color")
var4 = tkinter.IntVar()
var5 = tkinter.StringVar()
var5.set("QR size ")

# Create frame

frame = CTkFrame(master=app, width=window_width, height=window_height, corner_radius=20, border_width=3)

frame.grid()
frame.grid_propagate(0)


btn = CTkButton(master=frame,
                text="Generate",
                corner_radius=20,
                border_width=3,
                height=100,
                width=250,
                font=("Courier", 28, "bold"),
                command=lambda: [create_qr(get_data(), fill_clr=fill_color_combobox.get(),
                                           bg_clr=back_color_combobox.get(),
                                           ver=size_slider.get()),
                                 create_qr_canvas(get_data())])
# btn.configure(width=360, height=130)

# Labels
data_label = CTkLabel(master=frame, textvariable=var1, font=("Courier", 28, "bold"))
fill_color_label = CTkLabel(master=frame, textvariable=var2, font=("Courier", 20, "bold"))
back_color_label = CTkLabel(master=frame, textvariable=var3, font=("Courier", 20, "bold"))
size_label = CTkLabel(master=frame, textvariable=var4, font=("Courier", 20, "bold"))
QR_size_label = CTkLabel(master=frame, textvariable=var5, font=("Courier", 20, "bold"))

# Entries
data_entry = CTkEntry(master=frame, width=400, font=("Courier", 15, "bold"),
                      text_color="#C850C0")
# Sliders
size_slider = CTkSlider(master=frame, from_=1, to=40, number_of_steps=40,
                        button_color="#C850C0", progress_color="#C850C0",
                        orientation="horizontal", variable=var4)
# ComboBoxes
fill_color_combobox = CTkComboBox(master=frame, values=color_options)  # fg_color, border_color, dropdown_fg_color
fill_color_combobox["state"] = 'readonly'
back_color_combobox = CTkComboBox(master=frame, values=color_options)
back_color_combobox["state"] = 'readonly'


# Place on frame
data_label.grid(column=0, row=0, columnspan=1, pady=50, padx=50)
data_entry.grid(column=0, row=1, columnspan=1, pady=20, padx=10)
btn.grid(column=0, row=2, columnspan=1, pady=30, padx=20)

fill_color_label.grid(column=0, row=3, columnspan=1, pady=20, padx=10, sticky=W)
fill_color_combobox.grid(column=0, row=3, columnspan=1, pady=20, padx=10, sticky=E)

back_color_label.grid(column=0, row=4, columnspan=1, pady=20, padx=10, sticky=W)
back_color_combobox.grid(column=0, row=4, columnspan=1, pady=20, padx=10, sticky=E)

size_label.grid(column=0, row=5, columnspan=1, pady=20, padx=10, sticky=E)
QR_size_label.grid(column=0, row=5, columnspan=1, pady=20, padx=10, sticky=W)
size_slider.grid(column=0, row=5, columnspan=1, pady=20, padx=100, sticky=E)

# btn.pack(pady=80)
# label1.pack()
# data_entry.pack()


app.mainloop()
