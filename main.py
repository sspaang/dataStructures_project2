from tkinter import *
from PIL import Image, ImageTk
from BinarySearchTree import *
from tkinter import messagebox
import os
#from iphone_window import ipwindow

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def ipwindow():
    ip_window = Toplevel()
    ip_window.title("iPhone")
    ip_canvas = Canvas(ip_window, height=HEIGHT, width=WIDTH)
    ip_canvas.pack()
    ip_window.resizable(height=False, width=False)

    #photo_file = os.path.join(THIS_FOLDER, 'rsz_1rsz_iphone11.png')
    #img = PhotoImage(file=photo_file)
    #ip_canvas.create_image(WIDTH/2, 0, image=img)

    def insert_price():
        input_price = ip_entry.get()
        if float(input_price) < 14000:
            msgBox = messagebox.showwarning(title='WARNING', message='กรุณาใส่ราคามากกว่า 14,000 บาท')
        else:
            ipPrice_listbox.insert(END, f"{float(input_price)}")
            bst_insert = tree.insert(float(input_price))

            fr = open(ip_auction_price, 'a')    #เขียนต่อท้ายไฟล์เดิม
            fr.write(f'{float(input_price)};')
            fr.close

        ip_entry.delete(0, 'end')

    def price_search():
        input_price = ipPriceSearchEntry.get()
        if tree.search(float(input_price)) == True:
            return ipPriceLabel.config(text=f'{input_price} มีอยู่ในระบบแล้ว', fg='green')
        else:
            return ipPriceLabel.config(text=f'{input_price} ยังไม่มีอยู่ในระบบ', fg='red')
    
    def onReturn(*args):
        return insert_price()
    
    def onReturn_search(*args):
        return price_search()

    def on_mousewheel(*args):
        return ipPrice_listbox.yview

    tree = BST()
    ip_auction_price = os.path.join(THIS_FOLDER, 'ipAuction.txt')

    # Details
    ip_head = Label(ip_window, text="โทรศัพท์ยี่ห้อ Apple\nรุ่น iPhone")
    ip_head.place(x=285, y=40)
    ip_start = Label(ip_window, text="ราคาเริ่มต้น")
    ip_start.place(x=100, y=100)
    ip_startp = Label(ip_window, text="14,000 บาท")
    ip_startp.place(x=415, y=100)

    # Bet
    ip_bet = Label(ip_window, text="ราคาที่ต้องการประมูล")
    ip_bet.place(x=100, y=150)
    ip_entry = Entry(ip_window, bd=3)
    ip_entry.place(x=415, y=150)
    ip_entry.bind("<Return>", onReturn)

    ipAuction_btn = Button(ip_window ,text='ลงราคาประมูล', bg="#40E0D0", command=insert_price)
    ipAuction_btn.place(x=470, y=190)

    ipPrice_listbox = Listbox(ip_window, height=6, width=30)
    ipPrice_listbox.place(x=180+40, y=250)
    yscroll = Scrollbar(ip_window, orient=VERTICAL, command=ipPrice_listbox.yview)
    ipPrice_listbox.configure(yscrollcommand = yscroll.set)
    yscroll.bind("<MouseWheel>", on_mousewheel)
    yscroll.place(x=450+80, y=200+50, relheight=0.235)

    ipPriceSearchLabel = Label(ip_window, text='ตรวจสอบราคาประมูล')
    ipPriceSearchLabel.place(x=100, y=410)

    ipPriceSearchEntry = Entry(ip_window, bd=3)
    ipPriceSearchEntry.place(x=415, y=410)
    ipPriceSearchEntry.bind('<Return>', onReturn_search)

    ipPriceSearchBtn = Button(ip_window, text='ตรวจสอบ', bg='pink', command=price_search)
    ipPriceSearchBtn.place(x=470, y=460)

    ipPriceLabel = Label(ip_window, text='')
    ipPriceLabel.place(x=415, y=510)

    f = open(ip_auction_price, 'r')
    for i in f:
        try:
            price_list = i.split(";")   # List
            for each_price in price_list:
                tree.insert(float(each_price))
                ipPrice_listbox.insert(END, f'{float(each_price)}')
        except ValueError as e:
            print(f'Error -> {e} at {each_price}')

    ip_entry.focus()

    f.close()   #ปิดไฟล์

def nes_window():
    mac_window = Toplevel()
    mac_window.title("Macbook")
    mac_canvas = Canvas(mac_window, height=HEIGHT, width=WIDTH)
    mac_canvas.pack()
    mac_window.resizable(height=False, width=False)

    ip_file = os.path.join(THIS_FOLDER, 'iphone11.gif')

    def insert_price():
        input_price = mac_entry.get()
        if float(input_price) < 20000:
            msgBox = messagebox.showwarning(title='WARNING', message='กรุณาใส่ราคามากกว่า 20,000 บาท')
        else:
            macPrice_listbox.insert(END, f"{float(input_price)}")
            bst_insert = tree.insert(float(input_price))

            fr = open(mac_auction_price, 'a+')    #เขียนต่อท้ายไฟล์เดิม
            fr.write(f'{float(input_price)};')
            fr.close

        mac_entry.delete(0, 'end')

    def price_search():
        input_price = macPriceSearchEntry.get()
        if tree.search(float(input_price)) == True:
            return macPriceLabel.config(text=f'{input_price} มีอยู่ในระบบแล้ว', fg='green')
        else:
            return macPriceLabel.config(text=f'{input_price} ยังไม่มีอยู่ในระบบ', fg='red')
    
    def onReturn(*args):
        return insert_price()
    
    def onReturn_search(*args):
        return price_search()

    def on_mousewheel(*args):
        return macPrice_listbox.yview

    tree = BST()
    mac_auction_price = os.path.join(THIS_FOLDER, 'macAuction.txt')

    # Details
    mac_head = Label(mac_window, text="แลปท็อปยี่ห้อ Apple\nรุ่น Macbook Pro")
    mac_head.place(x=285, y=40)
    mac_start = Label(mac_window, text="ราคาเริ่มต้น")
    mac_start.place(x=100, y=100)
    mac_startp = Label(mac_window, text="20,000 บาท")
    mac_startp.place(x=415, y=100)
    # Bet
    mac_bet = Label(mac_window, text="ราคาที่ต้องการประมูล")
    mac_bet.place(x=100, y=150)
    mac_entry = Entry(mac_window, bd=3)
    mac_entry.place(x=415, y=150)
    mac_entry.bind("<Return>", onReturn)

    macAuction_btn = Button(mac_window ,text='ลงราคาประมูล', bg="#40E0D0", command=insert_price)
    macAuction_btn.place(x=470, y=190)

    macPrice_listbox = Listbox(mac_window, height=6, width=30)
    macPrice_listbox.place(x=180+40, y=250)
    yscroll = Scrollbar(mac_window, orient=VERTICAL, command=macPrice_listbox.yview)
    macPrice_listbox.configure(yscrollcommand = yscroll.set)
    yscroll.bind("<MouseWheel>", on_mousewheel)
    yscroll.place(x=450+80, y=200+50, relheight=0.235)

    macPriceSearchLabel = Label(mac_window, text='ตรวจสอบราคาประมูล')
    macPriceSearchLabel.place(x=100, y=410)

    macPriceSearchEntry = Entry(mac_window, bd=3)
    macPriceSearchEntry.place(x=415, y=410)
    macPriceSearchEntry.bind('<Return>', onReturn_search)

    macPriceSearchBtn = Button(mac_window, text='ตรวจสอบ', bg='pink', command=price_search)
    macPriceSearchBtn.place(x=470, y=460)

    macPriceLabel = Label(mac_window, text='')
    macPriceLabel.place(x=415, y=510)

    f = open(mac_auction_price, 'r')
    for i in f:
        try:
            price_list = i.split(";")   # List
            for each_price in price_list:
                tree.insert(float(each_price))
                macPrice_listbox.insert(END, f'{float(each_price)}')
        except ValueError as e:
            print(f'Error -> {e} at {each_price}')

    mac_entry.focus()

    f.close()   #ปิดไฟล์

def pswindow():
    ps_window = Toplevel()
    ps_window.title("PS")
    ps_canvas = Canvas(ps_window, height=HEIGHT, width=WIDTH)
    ps_canvas.pack()
    ps_window.resizable(height=False, width=False)

    def insert_price():
        input_price = ps_entry.get()
        if float(input_price) < 8000:
            msgBox = messagebox.showwarning(title='WARNING', message='กรุณาใส่ราคามากกว่า 8000 บาท')
        else:
            psPrice_listbox.insert(END, f"{float(input_price)}")
            bst_insert = tree.insert(float(input_price))

            fr = open(ps_auction_price, 'a+')    #เขียนต่อท้ายไฟล์เดิม
            fr.write(f'{float(input_price)};')
            fr.close

        ps_entry.delete(0, 'end')

    def price_search():
        input_price = psPriceSearchEntry.get()
        if tree.search(float(input_price)) == True:
            return psPriceLabel.config(text=f'{input_price} มีอยู่ในระบบแล้ว', fg='green')
        else:
            return psPriceLabel.config(text=f'{input_price} ยังไม่มีอยู่ในระบบ', fg='red')
    
    def onReturn(*args):
        return insert_price()
    
    def onReturn_search(*args):
        return price_search()

    def on_mousewheel(*args):
        return psPrice_listbox.yview

    tree = BST()
    ps_auction_price = os.path.join(THIS_FOLDER, 'psAuction.txt')

    # Details
    ps_head = Label(ps_window, text="เครื่องเล่นเกมส์ PlayStation\nรุ่น PlayStation 5")
    ps_head.place(x=240, y=40)
    ps_start = Label(ps_window, text="ราคาเริ่มต้น")
    ps_start.place(x=100, y=100)
    ps_startp = Label(ps_window, text="8,000 บาท")
    ps_startp.place(x=415, y=100)
    # Bet
    ps_bet = Label(ps_window, text="ราคาที่ต้องการประมูล")
    ps_bet.place(x=100, y=150)
    ps_entry = Entry(ps_window, bd=3)
    ps_entry.place(x=415, y=150)
    ps_entry.bind("<Return>", onReturn)

    psAuction_btn = Button(ps_window ,text='ลงราคาประมูล', bg="#40E0D0", command=insert_price)
    psAuction_btn.place(x=470, y=190)

    psPrice_listbox = Listbox(ps_window, height=6, width=30)
    psPrice_listbox.place(x=180+40, y=250)
    yscroll = Scrollbar(ps_window, orient=VERTICAL, command=psPrice_listbox.yview)
    psPrice_listbox.configure(yscrollcommand = yscroll.set)
    yscroll.bind("<MouseWheel>", on_mousewheel)
    yscroll.place(x=450+80, y=200+50, relheight=0.235)

    psPriceSearchLabel = Label(ps_window, text='ตรวจสอบราคาประมูล')
    psPriceSearchLabel.place(x=100, y=410)

    psPriceSearchEntry = Entry(ps_window, bd=3)
    psPriceSearchEntry.place(x=415, y=410)
    psPriceSearchEntry.bind('<Return>', onReturn_search)

    psPriceSearchBtn = Button(ps_window, text='ตรวจสอบ', bg='pink', command=price_search)
    psPriceSearchBtn.place(x=470, y=460)

    psPriceLabel = Label(ps_window, text='')
    psPriceLabel.place(x=415, y=510)

    f = open(ps_auction_price, 'r')
    for i in f:
        try:
            price_list = i.split(";")   # List
            for each_price in price_list:
                tree.insert(float(each_price))
                psPrice_listbox.insert(END, f'{float(each_price)}')
        except ValueError as e:
            print(f'Error -> {e} at {each_price}')

    ps_entry.focus()

    f.close()   #ปิดไฟล์

def wtwindow():
    wt_window = Toplevel()
    wt_window.title("Watch")
    wt_canvas = Canvas(wt_window, height=HEIGHT, width=WIDTH)
    wt_canvas.pack()
    wt_window.resizable(height=False, width=False)

    def insert_price():
        input_price = wt_entry.get()
        if float(input_price) < 2000000:
            msgBox = messagebox.showwarning(title='WARNING', message='กรุณาใส่ราคามากกว่า 2,000,000 บาท')
        else:
            wtPrice_listbox.insert(END, f"{float(input_price)}")
            bst_insert = tree.insert(float(input_price))

            fr = open(wt_auction_price, 'a+')    #เขียนต่อท้ายไฟล์เดิม
            fr.write(f'{float(input_price)};')
            fr.close

        wt_entry.delete(0, 'end')

    def price_search():
        input_price = wtPriceSearchEntry.get()
        if tree.search(float(input_price)) == True:
            return wtPriceLabel.config(text=f'{input_price} มีอยู่ในระบบแล้ว', fg='green')
        else:
            return wtPriceLabel.config(text=f'{input_price} ยังไม่มีอยู่ในระบบ', fg='red')
    
    def onReturn(*args):
        return insert_price()
    
    def onReturn_search(*args):
        return price_search()

    def on_mousewheel(*args):
        return wtPrice_listbox.yview

    tree = BST()
    wt_auction_price = os.path.join(THIS_FOLDER, 'watchAuction.txt')

    # Details
    wt_head = Label(wt_window, text="นาฬิกา Richard Mille\nรุ่น RM 029")
    wt_head.place(x=240, y=40)
    wt_start = Label(wt_window, text="ราคาเริ่มต้น")
    wt_start.place(x=100, y=100)
    wt_startp = Label(wt_window, text="2,000,000 บาท")
    wt_startp.place(x=415, y=100)
    # Bet
    wt_bet = Label(wt_window, text="ราคาที่ต้องการประมูล")
    wt_bet.place(x=100, y=150)
    wt_entry = Entry(wt_window, bd=3)
    wt_entry.place(x=415, y=150)
    wt_entry.bind("<Return>", onReturn)

    wtAuction_btn = Button(wt_window ,text='ลงราคาประมูล', bg="#40E0D0", command=insert_price)
    wtAuction_btn.place(x=470, y=190)

    wtPrice_listbox = Listbox(wt_window, height=6, width=30)
    wtPrice_listbox.place(x=180+40, y=250)
    yscroll = Scrollbar(wt_window, orient=VERTICAL, command=wtPrice_listbox.yview)
    wtPrice_listbox.configure(yscrollcommand = yscroll.set)
    yscroll.bind("<MouseWheel>", on_mousewheel)
    yscroll.place(x=450+80, y=200+50, relheight=0.235)

    wtPriceSearchLabel = Label(wt_window, text='ตรวจสอบราคาประมูล')
    wtPriceSearchLabel.place(x=100, y=410)

    wtPriceSearchEntry = Entry(wt_window, bd=3)
    wtPriceSearchEntry.place(x=415, y=410)
    wtPriceSearchEntry.bind('<Return>', onReturn_search)

    wtPriceSearchBtn = Button(wt_window, text='ตรวจสอบ', bg='pink', command=price_search)
    wtPriceSearchBtn.place(x=470, y=460)

    wtPriceLabel = Label(wt_window, text='')
    wtPriceLabel.place(x=415, y=510)

    f = open(wt_auction_price, 'r')
    for i in f:
        try:
            price_list = i.split(";")   # List
            for each_price in price_list:
                tree.insert(float(each_price))
                wtPrice_listbox.insert(END, f'{float(each_price)}')
        except ValueError as e:
            print(f'Error -> {e} at {each_price}')

    wt_entry.focus()

    f.close()   #ปิดไฟล์

def neswindow():
    nes_window = Toplevel()
    nes_window.title("Nintendo")
    nes_canvas = Canvas(nes_window, height=HEIGHT, width=WIDTH)
    nes_canvas.pack()
    nes_window.resizable(height=False, width=False)

    def insert_price():
        input_price = nes_entry.get()
        if float(input_price) < 6000:
            msgBox = messagebox.showwarning(title='WARNING', message='กรุณาใส่ราคามากกว่า 6,000 บาท')
        else:
            nesPrice_listbox.insert(END, f"{float(input_price)}")
            bst_insert = tree.insert(float(input_price))

            fr = open(nes_auction_price, 'a+')    #เขียนต่อท้ายไฟล์เดิม
            fr.write(f'{float(input_price)};')
            fr.close

        nes_entry.delete(0, 'end')

    def price_search():
        input_price = nesPriceSearchEntry.get()
        if tree.search(float(input_price)) == True:
            return nesPriceLabel.config(text=f'{input_price} มีอยู่ในระบบแล้ว', fg='green')
        else:
            return nesPriceLabel.config(text=f'{input_price} ยังไม่มีอยู่ในระบบ', fg='red')
    
    def onReturn(*args):
        return insert_price()
    
    def onReturn_search(*args):
        return price_search()

    def on_mousewheel(*args):
        return nesPrice_listbox.yview

    tree = BST()
    nes_auction_price = os.path.join(THIS_FOLDER, 'ninAuction.txt')

    # Details
    nes_head = Label(nes_window, text="เครื่องเล่นเกมส์ Nintendo\nรุ่น Nontendo Switch")
    nes_head.place(x=240, y=40)
    nes_start = Label(nes_window, text="ราคาเริ่มต้น")
    nes_start.place(x=100, y=100)
    nes_startp = Label(nes_window, text="6,000 บาท")
    nes_startp.place(x=415, y=100)
    # Bet
    nes_bet = Label(nes_window, text="ราคาที่ต้องการประมูล")
    nes_bet.place(x=100, y=150)
    nes_entry = Entry(nes_window, bd=3)
    nes_entry.place(x=415, y=150)
    nes_entry.bind("<Return>", onReturn)

    nesAuction_btn = Button(nes_window ,text='ลงราคาประมูล', bg="#40E0D0", command=insert_price)
    nesAuction_btn.place(x=470, y=190)

    nesPrice_listbox = Listbox(nes_window, height=6, width=30)
    nesPrice_listbox.place(x=180+40, y=250)
    yscroll = Scrollbar(nes_window, orient=VERTICAL, command=nesPrice_listbox.yview)
    nesPrice_listbox.configure(yscrollcommand = yscroll.set)
    yscroll.bind("<MouseWheel>", on_mousewheel)
    yscroll.place(x=450+80, y=200+50, relheight=0.235)

    nesPriceSearchLabel = Label(nes_window, text='ตรวจสอบราคาประมูล')
    nesPriceSearchLabel.place(x=100, y=410)

    nesPriceSearchEntry = Entry(nes_window, bd=3)
    nesPriceSearchEntry.place(x=415, y=410)
    nesPriceSearchEntry.bind('<Return>', onReturn_search)

    nesPriceSearchBtn = Button(nes_window, text='ตรวจสอบ', bg='pink', command=price_search)
    nesPriceSearchBtn.place(x=470, y=460)

    nesPriceLabel = Label(nes_window, text='')
    nesPriceLabel.place(x=415, y=510)

    f = open(nes_auction_price, 'r')
    for i in f:
        try:
            price_list = i.split(";")   # List
            for each_price in price_list:
                tree.insert(float(each_price))
                nesPrice_listbox.insert(END, f'{float(each_price)}')
        except ValueError as e:
            print(f'Error -> {e} at {each_price}')

    nes_entry.focus()

    f.close()   #ปิดไฟล์

""" ------------------------------------------------------------------------------------------------------------------ """

WIDTH = 800
HEIGHT = 600

home = Tk()
home.title("Aunction")
home.option_add("*Font", "consolas 14")

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
macbook_button = Button(text="Macbook", bd=0, command=nes_window)
macbook_button.place(x=50, y=240)
macbook_price_button = Button(text="เช็คราคาสินค้า", bg='green', command=nes_window)
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