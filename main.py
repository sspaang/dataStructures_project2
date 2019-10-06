from tkinter import *
from PIL import Image, ImageTk
from iphone_window import ipwindow

def ipwindow():
    ip_window = Toplevel()
    ip_window.title("iPhone")
    ip_canvas = Canvas(ip_window, height=HEIGHT, width=WIDTH)
    ip_canvas.pack()
    ip_window.resizable(height=False, width=False)
    #ip_pic = Image.open("iphone.png")
    #ip_photo = ImageTk.PhotoImage(ip_pic)
    #iphone_img = iphone_pic.resize((int(iphone_pic.width*.5), int(iphone_pic.height*.5)))
    #pic1 = Label(image=photo).pack()

    # Details
    ip_head = Label(ip_window, text="โทรศัพท์ยี่ห้อ Apple\nรุ่น iPhone")
    ip_head.place(x=285, y=40)
    ip_start = Label(ip_window, text="ราคาเริ่มต้น")
    ip_start.place(x=100, y=150)
    ip_startp = Label(ip_window, text="14,000 บาท")
    ip_startp.place(x=415, y=150)
    # Bet
    ip_bet = Label(ip_window, text="ราคาที่ต้องการประมูล")
    ip_bet.place(x=100, y=250)
    ip_entry = Entry(ip_window, bd=3)
    ip_entry.place(x=415, y=250)

def macwindow():
    mac_window = Toplevel()
    mac_window.title("Macbook")
    mac_canvas = Canvas(mac_window, height=HEIGHT, width=WIDTH)
    mac_canvas.pack()
    mac_window.resizable(height=False, width=False)
    mac_pic = Image.open("macbook.png")
    photo = ImageTk.PhotoImage(mac_pic)
    #iphone_img = iphone_pic.resize((int(iphone_pic.width*.5), int(iphone_pic.height*.5)))
    #pic1 = Label(image=photo).pack()

    # Details
    mac_head = Label(mac_window, text="แลปท็อปยี่ห้อ Apple\nรุ่น Macbook Pro")
    mac_head.place(x=285, y=40)
    mac_start = Label(mac_window, text="ราคาเริ่มต้น")
    mac_start.place(x=100, y=150)
    mac_startp = Label(mac_window, text="20,000 บาท")
    mac_startp.place(x=415, y=150)
    # Bet
    mac_bet = Label(mac_window, text="ราคาที่ต้องการประมูล")
    mac_bet.place(x=100, y=250)
    mac_entry = Entry(mac_window, bd=3)
    mac_entry.place(x=415, y=250)

def pswindow():
    ps_window = Toplevel()
    ps_window.title("PS")
    ps_canvas = Canvas(ps_window, height=HEIGHT, width=WIDTH)
    ps_canvas.pack()
    ps_window.resizable(height=False, width=False)
    ps_pic = Image.open("ps.png")
    ps_photo = ImageTk.PhotoImage(ps_pic)
    #iphone_img = iphone_pic.resize((int(iphone_pic.width*.5), int(iphone_pic.height*.5)))
    #pic1 = Label(image=photo).pack()

    # Details
    ps_head = Label(ps_window, text="เครื่องเล่นเกมส์ PlayStation\nรุ่น PlayStation5")
    ps_head.place(x=240, y=40)
    ps_start = Label(ps_window, text="ราคาเริ่มต้น")
    ps_start.place(x=100, y=150)
    ps_startp = Label(ps_window, text="8,000 บาท")
    ps_startp.place(x=415, y=150)
    # Bet
    ps_bet = Label(ps_window, text="ราคาที่ต้องการประมูล")
    ps_bet.place(x=100, y=250)
    ps_entry = Entry(ps_window, bd=3)
    ps_entry.place(x=415, y=250)

def wtwindow():
    wt_window = Toplevel()
    wt_window.title("Watch")
    wt_canvas = Canvas(wt_window, height=HEIGHT, width=WIDTH)
    wt_canvas.pack()
    wt_window.resizable(height=False, width=False)
    #wt_pic = Image.open("ps.png")
    #wt_photo = ImageTk.PhotoImage(wt_pic)
    #iphone_img = iphone_pic.resize((int(iphone_pic.width*.5), int(iphone_pic.height*.5)))
    #pic1 = Label(image=photo).pack()

    # Details
    wt_head = Label(wt_window, text="นาฬิกา Richard Mille\nรุ่น RM 029")
    wt_head.place(x=240, y=40)
    wt_start = Label(wt_window, text="ราคาเริ่มต้น")
    wt_start.place(x=100, y=150)
    wt_startp = Label(wt_window, text="2,000,000 บาท")
    wt_startp.place(x=415, y=150)
    # Bet
    wt_bet = Label(wt_window, text="ราคาที่ต้องการประมูล")
    wt_bet.place(x=100, y=250)
    wt_entry = Entry(wt_window, bd=3)
    wt_entry.place(x=415, y=250)

def neswindow():
    nes_window = Toplevel()
    nes_window.title("Nintendo")
    nes_canvas = Canvas(nes_window, height=HEIGHT, width=WIDTH)
    nes_canvas.pack()
    nes_window.resizable(height=False, width=False)
    nes_pic = Image.open("nes.png")
    #nes_photo = ImageTk.PhotoImage(nes_pic)
    #iphone_img = iphone_pic.resize((int(iphone_pic.width*.5), int(iphone_pic.height*.5)))
    #pic1 = Label(image=photo).pack()

    # Details
    nes_head = Label(nes_window, text="เครื่องเล่นเกมส์ Nintendo\nรุ่น Nontendo Switch")
    nes_head.place(x=240, y=40)
    nes_start = Label(nes_window, text="ราคาเริ่มต้น")
    nes_start.place(x=100, y=150)
    nes_startp = Label(nes_window, text="6,000 บาท")
    nes_startp.place(x=415, y=150)
    # Bet
    nes_bet = Label(nes_window, text="ราคาที่ต้องการประมูล")
    nes_bet.place(x=100, y=250)
    nes_entry = Entry(nes_window, bd=3)
    nes_entry.place(x=415, y=250)

WIDTH = 800
HEIGHT = 600

home = Tk()
home.title("Aunction")
home.option_add("*Font", "consolas 20")

# Window
canvas = Canvas(home, height=HEIGHT, width=WIDTH)
canvas.pack()

home.resizable(height=False, width=False)

# Heading
head_lbl = Label(home, text="ดาต้า 8 การประมูล", bg="orange", fg="white")
subhead_lbl = Label(home, text='รายการสินค้า')
head_lbl.place(x=300, y=30)
subhead_lbl.place(x=50, y=100)

# iPhone layout
iphone_button = Button(text="iPhone", bd=0, command=ipwindow)
iphone_button.place(x=50,y=160)
iphone_price_button = Button(text="เช็คราคาสินค้า", bg='green', command=ipwindow)
iphone_price_button.place(x=550, y=160)

# Macbook layout
macbook_button = Button(text="Macbook", bd=0, command=macwindow)
macbook_button.place(x=50, y=240)
macbook_price_button = Button(text="เช็คราคาสินค้า", bg='green', command=macwindow)
macbook_price_button.place(x=550, y=240)

# PlayStation layout
playstation_button = Button(text="PlayStation", bd=0, command=pswindow)
playstation_button.place(x=50, y=320)
playstation_price_button = Button(text="เช็คราคาสินค้า", bg='green', command=pswindow)
playstation_price_button.place(x=550, y=320)

# Watch layout
watch_button = Button(text="Watch", bd=0, command=wtwindow)
watch_button.place(x=50, y=400)
watch_price_button = Button(text="เช็คราคาสินค้า", bg='green', command=wtwindow)
watch_price_button.place(x=550, y=400)

# Nintendo layout
nintendo_button = Button(text="Nintendo", bd=0, command=neswindow)
nintendo_button.place(x=50, y=480)
nintendo_price_button = Button(text="เช็คราคาสินค้า", bg='green', command=neswindow)
nintendo_price_button.place(x=550, y=480)


home.mainloop()