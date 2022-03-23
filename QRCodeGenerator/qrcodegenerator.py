from tkinter import *
from PIL import Image, ImageTk
import qrcode


class Application:
    def __init__(self, master=None):
        self.font_standard = ("Arial", "10")
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 60
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 60
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 60
        self.thirdContainer["pady"] = 30
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 60
        self.fourthContainer.pack()

        self.title = Label(self.firstContainer, text="QRCode Generator")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.dataLabel = Label(self.secondContainer,text="Data Here: ", font=self.font_standard)
        self.dataLabel.pack(side=LEFT)

        self.data = Entry(self.secondContainer)
        self.data["width"] = 30
        self.data["font"] = self.font_standard
        self.data.pack(side=LEFT)

        self.generate = Button(self.thirdContainer)
        self.generate["text"] = "GENERATE"
        self.generate["font"] = ("Calibri", "8")
        self.generate["width"] = 12
        self.generate["command"] = self.generate_qrcode
        self.generate.pack()

        self.message = Label(self.thirdContainer, text="", image='', font=self.font_standard)
        self.message.pack()

    def generate_qrcode(self):
        input_data = self.data.get()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )

        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qrcode001.png')

        if input_data:
            self.message["text"] = "successfully generated, file in directory in this file"
        else:
            self.message["text"] = "ERROR"

root = Tk()
root.title('QRCode Generator')
Application(root)
root.mainloop()