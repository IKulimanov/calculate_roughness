import pickle
from tkinter import Tk, Frame, BOTH, Button, BooleanVar, DoubleVar, Entry, IntVar, Radiobutton, Label
from e_calc import ECalc


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()
        self.rb_deep20 = Radiobutton(text="20 мкм", font="Times 13", variable=self.deep, value=20)
        self.rb_deep40 = Radiobutton(text="40 мкм", font="Times 13", variable=self.deep, value=40)
        self.rb_deep50 = Radiobutton(text="50 мкм", font="Times 13", variable=self.deep, value=50)

        self.otris()

    def initUI(self):
        self.parent.title("Simple")
        self.parent.resizable(width=False, height=False)
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        self.material = BooleanVar()
        self.side = BooleanVar()
        self.napr = BooleanVar()
        self.method = BooleanVar()
        self.alfa = DoubleVar()
        self.fi = DoubleVar()
        self.ra = DoubleVar()
        self.rz = DoubleVar()
        self.depth = IntVar()
        self.tochn = IntVar()
        self.deep = IntVar()
        self.tochn.set(10)
        rb_deep20 = Radiobutton(text="20 мкм", font="Times 13", variable=self.deep, value=20)
        rb_deep40 = Radiobutton(text="40 мкм", font="Times 13", variable=self.deep, value=40)
        rb_deep50 = Radiobutton(text="50 мкм", font="Times 13", variable=self.deep, value=50)

        label_material = Label(text="Выберите материал:", font="Times 15")

        label_ugol = Label(text="Введите угол наклона(\u03B1) и поворота(\u03C6):", font="Times 14")

        label_alfa = Label(text="\u03B1 =", font="Times 15")
        label_fi = Label(text="\u03C6 =", font="Times 15")

        label_side = Label(text="Выберите вид поверхности:", font="Times 15")

        label_method = Label(text="Выберите средство измерения:", font="Times 15")

        label_napr = Label(text="Выберите направление измерения:", font="Times 15")

        label_depth = Label(text="Введите толщину слоя:", font="Times 15")

        label_rarz = Label(text="Введите Ra и Rz:", font="Times 15")

        rb_material_x15 = Radiobutton(text="Х15Н5Д4Б", font="Times 13", variable=self.material, value=1)
        rb_material_kx28 = Radiobutton(text="КХ28М6", font="Times 13", variable=self.material, value=0)

        en_alfa = Entry(width=12, font="Arial 13", textvariable=self.alfa)
        en_fi = Entry(width=12, font="Arial 13", textvariable=self.fi)

        rb_side_outer = Radiobutton(text="Наружняя", font="Times 14", variable=self.side, value=1)
        rb_side_inter = Radiobutton(text="Внутренняя", font="Times 14", variable=self.side, value=0)

        rb_napr_prod = Radiobutton(text="Продольное", font="Times 14", variable=self.napr, value=1,
                                   command=self.profiClic)
        rb_napr_poper = Radiobutton(text="Поперечное", font="Times 14", variable=self.napr, value=0,
                                   command=self.profiClic)
        rb_microscope = Radiobutton(text="Микроскоп", font="Times 14", variable=self.method, value=1,
                                    command=self.microClic)
        rb_profilometr = Radiobutton(text="Профилометр", font="Times 14", variable=self.method, value=0,
                                     command=self.profiClic)

        en_depth = Entry(width=15, font="Times 14", textvariable=self.depth)

        en_ra = Entry(width=15, font="Times 14", textvariable=self.ra)
        en_rz = Entry(width=15, font="Times 14", textvariable=self.rz)

        label_toch = Label(text="Введите отклонение в %: ", font="Times 15")
        en_toch = Entry(width=8, font="Times 14", textvariable=self.tochn)

        bCalc = Button(width=15, text="Рассчитать", font="Times 13", command=self.onClick)
        # лабел материала
        label_material.place(x=100, y=10)
        # радиобатан материала
        rb_material_x15.place(x=50, y=50)
        rb_material_kx28.place(x=220, y=50)
        # лаблы углов
        # label_ugol.place(x=40, y=100)
        # label_alfa.place(x=40, y=137)
        # label_fi.place(x=214, y=137)
        # поля ввода углов
        # en_alfa.place(x = 76, y = 140)
        # en_fi.place(x = 250, y = 140)
        # лабел выбора стороны
        label_side.place(x=80, y=100)
        # Выбор стороны
        rb_side_outer.place(x=50, y=140)
        rb_side_inter.place(x=220, y=140)
        # лабел средства
        label_napr.place(x=60, y=190)
        # выбор способа сбора инфы

        rb_napr_prod.place(x=50, y=230)
        rb_napr_poper.place(x=220, y=230)
        # лабел направления
        label_method.place(x=68, y=280)
        # выбор направления
        rb_microscope.place(x=50, y=320)
        rb_profilometr.place(x=220, y=320)
        # лабел толщины
        label_depth.place(x=85, y=370)
        # ввод толщины
        # en_depth.place(x=130, y=410)
        #  if self.method:
        # else:
        #      if self.napr:
        # rb_deep50.place(x=330, y=410)
        # rb_deep20.place(x=50, y=410)
        # rb_deep40.place(x=150, y=410)
        # rb_deep50.place(x=320, y=410)

        label_rarz.place(x=100, y=450)

        en_ra.place(x=50, y=490)
        en_rz.place(x=220, y=490)
        label_toch.place(x=50, y=540)
        en_toch.place(x=275, y=540)
        bCalc.place(x=130, y=650)

    def onClick(self):
        # print(self.depth.get())
        ecl = ECalc()

        di = ecl.eCalc(self.material.get(), self.side.get(), self.method.get(), self.napr.get(), self.alfa.get(),
                       self.fi.get(), self.ra.get(), self.rz.get(), self.deep.get(), self.tochn.get())



        # lb1 = Label(text=di, font="Times 15").place(x=00, y=620)
        lb1 = Label(text="Ra =", font="Times 15").place(x=90, y=580)
        lb2 = Label(text=di.get('ra'), font="Times 15").place(x=130, y=580)
        lb3 = Label(text="\u03B1 =", font="Times 15").place(x=50, y=610)
        lb4 = Label(text=di.get('alfa'), font="Times 15").place(x=90, y=610)
        lb5 = Label(text="\u03C6 =", font="Times 15").place(x=240, y=610)
        lb6 = Label(text=di.get('fi'), font="Times 15").place(x=280, y=610)
        # lb2 = Label(text=ecl.calcRz, font="Times 15").place(x=260, y=620)

    def centerWindow(self):
        w = 400
        h = 700

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2

        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def microClic(self):
        self.rb_deep20.place_forget()
        self.rb_deep40.place_forget()
        self.rb_deep50.place_forget()

        self.rb_deep20.place(x=150, y=410)

    def profiClic(self):
        self.rb_deep20.place_forget()
        self.rb_deep40.place_forget()
        self.rb_deep50.place_forget()
        if self.method.get():
            self.rb_deep20.place(x=150, y=410)
        else:
            if self.napr.get():
                self.rb_deep40.place(x=100, y=410)
                self.rb_deep50.place(x=230, y=410)
            else:
                self.rb_deep20.place(x=50, y=410)
                self.rb_deep40.place(x=150, y=410)
                self.rb_deep50.place(x=250, y=410)

    def otris(self):
        self.rb_deep20.place(x=50, y=410)
        self.rb_deep40.place(x=150, y=410)
        self.rb_deep50.place(x=250, y=410)

