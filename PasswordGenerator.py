from tkinter import *
from tkinter import ttk
from pickle import dump, load
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import pyperclip as p
from random import randint
from os import remove, rename, popen
from time import ctime
import pyqrcode
import png
import webbrowser


def copied_display():
    global img2
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat")
    b2.place(
        x=150, y=417,
        width=161,
        height=55)
    window.after(1000, b2.destroy)


def error_display():
    global img3
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        relief="flat")
    b3.place(
        x=108, y=488,
        width=261,
        height=88)
    window.after(1500, b3.destroy)


def pwd():
    global qrcode1
    password = ""
    try:
        l = int(entry0.get())
        special = entry1.get()
        characters = "A1B2C3D4E5qFr6sG7tH8I9Ju0KaLbvMcNdwOePfQgxRhSivTjUkzVlWmXnYoZp"
        if l >= 4:
            if special == 'No' or special == "N" or special == "no" or special == "n":
                for i in range(l):
                    char = characters[randint(0, 61)]
                    password += char
                p.copy(password)
                copied_display()
                qrcode = pyqrcode.create(
                    "Password: {0}\nWebsite: {1}".format(password, entry2.get()))
                qrcode.png("generated_qrcode.png", scale=4)

                qrcode1 = PhotoImage(file="generated_qrcode.png")
                qrcode_button = Button(
                    image=qrcode1,
                    borderwidth=0,
                    highlightthickness=0,
                    relief="flat")
                qrcode_button.place(
                    x=130,
                    y=220)

                remove("generated_qrcode.png")
                window.after(60000, qrcode_button.destroy)
            elif special == 'yes' or special == 'Yes' or special == "y" or special == 'Y':
                special_characters = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
                for i in range(l):
                    choices = [True, False]
                    choice = choices[randint(0, 1)]
                    if choice == True:
                        char = special_characters[randint(0, 29)]
                        password += char
                    elif choice == False:
                        char = characters[randint(0, 61)]
                        password += char
                p.copy(password)
                copied_display()
                qrcode = pyqrcode.create(
                    "Password: {0}\nWebsite: {1}".format(password, entry2.get()))
                qrcode.png("generated_qrcode.png", scale=4)

                qrcode1 = PhotoImage(file="generated_qrcode.png")
                qrcode_button = Button(window,
                                       image=qrcode1,
                                       borderwidth=0,
                                       highlightthickness=0,
                                       relief="flat")
                qrcode_button.place(
                    x=130,
                    y=220)

                remove("generated_qrcode.png")
                window.after(60000, qrcode_button.destroy)
            else:
                specify_error = Label(
                    window, text="Invalid Input", font=("Verdana", 10), fg='red')
                specify_error.place(x=800, y=260)
                if style.theme_use() == 'dark':
                    specify_error.configure(bg="#333333")
                window.after(1000, specify_error.destroy)
        else:
            error_display()
    except ValueError:
        error_display()
    if password:
        f = open("Passwords.bin", "ab")
        data = [ctime(), password, entry2.get()]
        dump(data, f)
        f.close()


def shw_pwds():
    global tree
    win = Toplevel()
    win.title("Passwords")
    win.iconbitmap('./resource/passwordbook.ico')
    win.geometry("925x620")
    if style.theme_use() == 'dark':
        win.configure(background="#333333")

    try:
        with open("Passwords.bin", 'rb') as f:
            try:
                data = []
                while True:
                    data.append(load(f))
            except EOFError:
                pass
    except FileNotFoundError:
        label5 = ttk.Label(win,
                           font=("Broadway", 48),
                           text="File Not Found")
        label5.place(
            y=250,
            x=260)
        win.after(500, win.destroy)

    try:
        if data != []:
            tree = ttk.Treeview(win, column=(
                "c1", "c2", "c3"), show='headings', height=20)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Time")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Password")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3", text="Website")
    except:
        pass

    try:
        n = 1
        for i in data:
            tree.insert('', 'end', text=n, values=(
                i[0], i[1], i[2]), tags=[i[1], i[2]])
            n += 1
    except UnboundLocalError:
        pass

    try:
        def browse(event):
            selected_item = tree.focus()
            item = tree.item(selected_item)['values']
            url = item[2]
            webbrowser.open(url)

        def ctrl_c(event):
            global live_qrcode_img
            selected_item = tree.focus()
            item = tree.item(selected_item)['values']
            p.copy(item[1])
            live_qrcode = pyqrcode.create(
                "Password: {0}\nWebsite: {1}".format(item[1], item[2]))
            live_qrcode.png("live_generated_qrcode.png", scale=2)

            live_qrcode_img = PhotoImage(file="live_generated_qrcode.png")
            live_qrcode_label = Label(win,
                                      image=live_qrcode_img)
            live_qrcode_label.place(
                x=770,
                y=500)
            remove("live_generated_qrcode.png")
            win.after(60000, live_qrcode_label.destroy)

        tree.place(
            x=12,
            y=15,
            width=900)
        tree.bind("<Triple-1>", browse)
        tree.bind("<Double-1>", ctrl_c)

        def update():
            global entry1, entry2, label1, save_btn
            try:
                win.after(0, entry3.destroy)
                win.after(0, label2.destroy)
                win.after(0, search_in_btn.destroy)
                win.after(0, reset_btn.destroy)
            except:
                pass

            def save():
                with open("Passwords.bin", 'rb') as f:
                    try:
                        data = []
                        while True:
                            data.append(load(f))
                    except EOFError:
                        pass
                selected_item = tree.focus()
                item = tree.item(selected_item)['values']
                n = tree.item(selected_item)['text']
                with open("Passwords.bin", "wb") as f:
                    for i in data:
                        if i[1] == item[1]:
                            i[1] = entry1.get()
                            i[2] = entry2.get()
                            dump(i, f)
                            tree.delete(tree.selection()[0])
                            tree.insert('', 'end', text=n,
                                        values=(ctime(), i[1], i[2]))
                        elif i[1] != item[1]:
                            dump(i, f)
                win.after(0, label1.destroy)
                win.after(0, entry1.destroy)
                win.after(0, entry2.destroy)
                win.after(0, save_btn.destroy)

            if tree.selection():
                selected_item = tree.focus()
                item = tree.item(selected_item)['values']
                save_btn = ttk.Button(win, text="Save", command=save)
                label1 = Label(win,
                               text=item[0])
                if style.theme_use() == 'dark':
                    label1.configure(bg="#333333", fg='white')
                entry1 = ttk.Entry(win,
                                   width=43)
                entry1.insert(0, item[1])
                entry2 = ttk.Entry(win,
                                   width=43)
                entry2.insert(0, item[2])
                label1.place(
                    y=500,
                    x=300)
                entry1.place(
                    y=525,
                    x=300)
                entry2.place(
                    y=560,
                    x=300)
                save_btn.place(
                    y=560,
                    x=580)
            else:
                select_record_label = Label(
                    win, text="Select a record to update", font=("Verdana", 10), fg='red')
                if style.theme_use() == 'dark':
                    select_record_label.configure(bg="#333333")
                select_record_label.place(x=300, y=525)
                win.after(1000, select_record_label.destroy)

        def delete():
            selected_item = tree.focus()
            item = tree.item(selected_item)['values']
            with open("Passwords.bin", "rb") as f:
                a = []
                try:
                    while True:
                        a.append(load(f))
                except EOFError:
                    pass
            with open("Edited.bin", "wb") as f:
                for i in a:
                    if i != item:
                        dump(i, f)
            remove("Passwords.bin")
            rename("Edited.bin", "Passwords.bin")
            tree.delete(tree.selection()[0])

        def delete_all(event):
            remove("key.key")
            remove('password_file.key')
            remove("Passwords.bin")
            label4 = Label(win,
                           width=43,
                           text="Deleted Successfully",
                           font=("Verdana", 10), fg='red')
            if style.theme_use() == 'dark':
                label4.configure(bg="#333333", fg='white')
            label4.place(
                y=500,
                x=250)
            tree.delete(*tree.get_children())
            win.update()

        def search():
            global entry3, label2, search_in_btn, reset_btn
            try:
                win.after(0, entry1.destroy)
                win.after(0, entry2.destroy)
                win.after(0, label1.destroy)
                win.after(0, save_btn.destroy)
            except:
                pass

            def reset():
                global tree, up_data
                tree.delete(*tree.get_children())
                tree = ttk.Treeview(win, column=(
                    "c1", "c2", "c3"), show='headings', height=20)
                tree.column("# 1", anchor=CENTER)
                tree.heading("# 1", text="Time")
                tree.column("# 2", anchor=CENTER)
                tree.heading("# 2", text="Password")
                tree.column("#3", anchor=CENTER)
                tree.heading("#3", text="Website")
                up_data = []
                with open("Passwords.bin", 'rb') as f:
                    try:
                        while True:
                            up_data.append(load(f))
                    except EOFError:
                        pass
                n = 1
                for i in up_data:
                    tree.insert('', 'end', text=n, values=(
                        i[0], i[1], i[2]), tags=[i[1], i[2]])
                    n += 1
                tree.place(
                    x=12,
                    y=15,
                    width=900)
                tree.bind("<Triple-1>", browse)
                tree.bind("<Double-1>", ctrl_c)
                win.update()
                win.after(1, reset_btn.destroy)

            def search_in():
                global tree
                full_data = []
                with open("Passwords.bin", 'rb') as f:
                    try:
                        while True:
                            full_data.append(load(f))
                    except EOFError:
                        pass
                matching_data = []
                for i in full_data:
                    if entry3.get() == i[1]:
                        matching_data.append(i)
                    elif entry3.get() == i[2]:
                        matching_data.append(i)

                tree.delete(*tree.get_children())
                tree = ttk.Treeview(win, column=(
                    "c1", "c2", "c3"), show='headings', height=20)
                tree.column("# 1", anchor=CENTER)
                tree.heading("# 1", text="Time")
                tree.column("# 2", anchor=CENTER)
                tree.heading("# 2", text="Password")
                tree.column("#3", anchor=CENTER)
                tree.heading("#3", text="Website")
                n = 1
                for i in matching_data:
                    tree.insert('', 'end', text=n, values=(
                        i[0], i[1], i[2]), tags=[i[1], i[2]])
                    n += 1
                tree.place(
                    x=12,
                    y=15,
                    width=900)
                tree.bind("<Triple-1>", browse)
                tree.bind("<Double-1>", ctrl_c)
                win.update()

                win.after(1, entry3.destroy)
                win.after(1, label2.destroy)
                win.after(1, search_in_btn.destroy)

            entry3 = ttk.Entry(win,
                               width=50)
            entry3.place(
                y=500,
                x=230)
            label2 = ttk.Label(win,
                               width=27,
                               text="Search by website or password")
            label2.place(
                y=525,
                x=230)
            search_in_btn = ttk.Button(win, text="Search", command=search_in)
            search_in_btn.place(
                x=450,
                y=538)
            reset_btn = ttk.Button(win, text="Reset", command=reset)
            reset_btn.place(
                x=680,
                y=538)

        update_btn = ttk.Button(win, text="Update", command=update)
        update_btn.place(
            x=40,
            y=500)
        del_btn = ttk.Button(win, text="Delete", command=delete)
        del_btn.place(
            x=130,
            y=500)
        del_all_btn = ttk.Button(win, text="Delete All")
        del_all_btn.bind('<Double 1>', delete_all)
        del_all_btn.place(
            x=40,
            y=540)
        search_btn = ttk.Button(win, text="Search", command=search)
        search_btn.place(
            x=130,
            y=540)
    except UnboundLocalError:
        win.destroy

    win.resizable(False, False)
    win.mainloop()


def Current_User(decryption_key, b, c):
    global open_eye, closed_eye, open_eye_bright, closed_eye_bright

    def forgot(event):
        def auth_forgot():
            if question_answer.get() == c:
                window4.destroy()
                remove('password_file.key')
                remove('key.key')
                remove('security_question_file.key')
                New_User()
            else:
                Invalid_Password_label_1 = Label(
                    window4, text="Invalid", fg='red')
                if style.theme_use() == 'dark':
                    Invalid_Password_label_1.configure(bg="#333333")
                Invalid_Password_label_1.place(x=50, y=80)
                window4.after(500, Invalid_Password_label_1.destroy)

        window1.destroy()
        window4 = Toplevel()
        window4.title("Forgot Password")
        window4.iconbitmap('./resource/forgot.ico')
        window4.geometry('290x120')
        if style.theme_use() == 'dark':
            window4.configure(background="#333333")

        question_label = Label(
            window4, text="Where did you attend your high school?")
        question_label.place(x=10, y=10)
        if style.theme_use() == 'dark':
            question_label.configure(bg="#333333", fg="white")

        question_answer = ttk.Entry(window4, show="*", width=40)
        question_answer.place(x=10, y=40)

        def change_eye_forgot_1(event):
            eye_icon_1.configure(image=open_eye)
            if style.theme_use() == "dark":
                eye_icon_1.configure(image=open_eye_bright)
            eye_icon_1.bind("<Button>", change_eye_forgot)
            question_answer.configure(show="*")

        def change_eye_forgot(event):
            eye_icon_1.configure(image=closed_eye)
            if style.theme_use() == 'dark':
                eye_icon_1.configure(image=closed_eye_bright)
            eye_icon_1.bind("<Button>", change_eye_forgot_1)
            question_answer.configure(show="")

        eye_icon_1 = Label(window4, image=open_eye)
        if style.theme_use() == 'dark':
            eye_icon_1.configure(image=open_eye_bright)
        eye_icon_1.place(x=250, y=11)
        eye_icon_1.bind("<Button>", change_eye_forgot)

        if style.theme_use() == 'dark':
            eye_icon_1.configure(bg="#333333")

        Save_Button = ttk.Button(window4, text="Continue", command=auth_forgot)
        Save_Button.place(x=170, y=80)

        window4.resizable(False, False)
        window4.mainloop()

    window1 = Toplevel()
    window1.title("Login")
    window1.iconbitmap('./resource/login.ico')
    window1.geometry("300x100")
    if style.theme_use() == 'dark':
        window1.configure(background="#333333")

    Password_label = Label(window1, text="Password")
    Password_label.place(x=20, y=15)

    forgot_password_label = Label(window1, text='Forgot Password', fg='red')
    forgot_password_label.place(x=50, y=50)
    if style.theme_use() == 'dark':
        Password_label.configure(bg="#333333", fg='white')
        forgot_password_label.configure(bg="#333333")

    Password = ttk.Entry(window1, show="*", width=26)
    Password.place(x=84, y=10)

    def change_eye_1(event):
        eye_icon.configure(image=open_eye)
        if style.theme_use() == 'dark':
            eye_icon.configure(image=open_eye_bright)
        eye_icon.bind("<Button>", change_eye)
        Password.configure(show="*")

    def change_eye(event):
        eye_icon.configure(image=closed_eye)
        if style.theme_use() == 'dark':
            eye_icon.configure(image=closed_eye_bright)
        eye_icon.bind("<Button>", change_eye_1)
        Password.configure(show="")

    eye_icon = Label(window1, image=open_eye)
    if style.theme_use() == 'dark':
        eye_icon.configure(image=open_eye_bright)
    eye_icon.place(x=265, y=14)
    eye_icon.bind("<Button>", change_eye)

    if style.theme_use() == 'dark':
        eye_icon.configure(bg="#333333")

    forgot_password_label.bind("<Button>", forgot)

    def invalid_password():
        Invalid_Password_label = Label(
            window1, text="Invalid Password", fg='red')
        if style.theme_use() == 'dark':
            Invalid_Password_label.configure(bg="#333333")
        Invalid_Password_label.place(x=50, y=50)
        window1.after(500, Invalid_Password_label.destroy)

    def correct_password():
        window1.destroy()
        shw_pwds()

    def authentication():
        if Password.get() == decryption_key.decrypt(b).decode():
            correct_password()
        else:
            invalid_password()

    Continue_button = ttk.Button(
        window1, width=10, text="Continue", command=authentication)
    Continue_button.place(x=170, y=50)

    window1.resizable(False, False)
    window1.mainloop()


def New_User():
    global Password, open_eye, closed_eye
    window2 = Toplevel()
    window2.title("Sign Up")
    window2.geometry("290x200")
    window2.iconbitmap('./resource/signup.ico')
    if style.theme_use() == 'dark':
        window2.configure(background="#333333")

    def check_passwords():
        if New_Password.get() == "" or Re_enter_Password.get() == "" or Security_question.get() == "":
            invalid_input = Label(
                window2, text="Entries can't\nbe empty", font=("Verdana", 10), fg='red')
            if style.theme_use() == 'dark':
                invalid_input.configure(bg="#333333")
            invalid_input.place(x=20, y=150)
            window2.after(500, invalid_input.destroy)
        elif New_Password.get() == Re_enter_Password.get():
            Password = Re_enter_Password.get()
            key = Fernet.generate_key()
            security_answer = Security_question.get()
            key_file = open("key.key", 'wb')
            encryption_key = Fernet(key)
            e_password = encryption_key.encrypt(Password.encode())
            dump(key, key_file)
            key_file.close()
            password_file = open("password_file.key", 'wb')
            dump(e_password, password_file)
            security_question_file = open("security_question_file.key", 'wb')
            dump(security_answer, security_question_file)
            password_file.close()
            security_question_file.close()
            window2.destroy()
            shw_pwds()
        elif New_Password.get() != Re_enter_Password.get():
            no_matchLabel = Label(
                window2, text="Passwords not\nmatching", font=('Verdana', 10), fg='red')
            if style.theme_use() == 'dark':
                no_matchLabel.configure(bg="#333333")
            no_matchLabel.place(x=20, y=150)
            window2.after(500, no_matchLabel.destroy)

    Password_label = Label(window2, text="Password")
    Password_label.place(x=20, y=15)

    New_Password = ttk.Entry(window2, show="*", width=26)
    New_Password.place(x=84, y=10)

    Password_label_1 = Label(window2, text="Re-enter\nPassword")
    Password_label_1.place(x=20, y=46)

    Re_enter_Password = ttk.Entry(window2, show="*", width=26)
    Re_enter_Password.place(x=84, y=50)

    Security_question_label = Label(
        window2, text="Where did you attend your high school?")
    Security_question_label.place(x=20, y=85)

    if style.theme_use() == 'dark':
        Password_label.configure(bg="#333333", fg='white')
        Password_label_1.configure(bg="#333333", fg='white')
        Security_question_label.configure(bg="#333333", fg='white')

    Security_question = ttk.Entry(window2, show="*", width=37)
    Security_question.place(x=20, y=110)

    def change_eye_sign_up_1(event):
        eye_icon_2.configure(image=open_eye)
        if style.theme_use() == 'dark':
            eye_icon_2.configure(image=open_eye_bright)
        eye_icon_2.bind("<Button>", change_eye_sign_up)
        New_Password.configure(show="*")
        Re_enter_Password.configure(show="*")
        Security_question.configure(show="*")

    def change_eye_sign_up(event):
        eye_icon_2.configure(image=closed_eye)
        if style.theme_use() == 'dark':
            eye_icon_2.configure(image=closed_eye_bright)
        eye_icon_2.bind("<Button>", change_eye_sign_up_1)
        New_Password.configure(show="")
        Re_enter_Password.configure(show="")
        Security_question.configure(show="")

    eye_icon_2 = Label(window2, image=open_eye)
    if style.theme_use() == 'dark':
        eye_icon_2.configure(image=open_eye_bright)
    eye_icon_2.place(x=130, y=155)
    eye_icon_2.bind("<Button>", change_eye_sign_up)

    if style.theme_use() == 'dark':
        eye_icon_2.configure(bg="#333333")

    Save_Button = ttk.Button(window2, text="Save", command=check_passwords)
    Save_Button.place(x=170, y=150)

    window2.resizable(False, False)
    window2.mainloop()


def Execution():
    try:
        f = open("key.key", 'rb')
        a = load(f)
        decryption_key = Fernet(a)
        f.close()
        f = open("password_file.key", 'rb')
        b = load(f)
        f.close()
        f = open("security_question_file.key", 'rb')
        c = load(f)
        f.close()
        Current_User(decryption_key, b, c)
    except:
        New_User()


window = Tk()
window.title("Password Generator")
window.iconbitmap('./resource/passwordwindow.ico')
window.geometry("1000x600")
style = ttk.Style()
window.call('source', 'dark.tcl')
window.call("source", "light.tcl")
style.theme_use("light")

canvas = Canvas(
    window,
    bg="#186ded",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

light_bg = PhotoImage(file=f"./resource/background_light.png")
background = canvas.create_image(
    500.0, 300.0,
    image=light_bg)

dark_mode_img_org = Image.open("./resource/nightmode.png")
resize_dark_mode_img = dark_mode_img_org.resize((30, 30))
dark_mode_img = ImageTk.PhotoImage(resize_dark_mode_img)
light_mode_img_org = Image.open("./resource/brightmode.png")
resize_light_mode_img = light_mode_img_org.resize((30, 30))
light_mode_img = ImageTk.PhotoImage(resize_light_mode_img)
dark_bg = PhotoImage(file=f'./resource/background.png')
img2 = PhotoImage(file=f"./resource/img0_light.png")
img3 = PhotoImage(file=f"./resource/img1_light.png")

closed_eye_org = Image.open("./resource/closed_eye.png")
resized_closed_eye = closed_eye_org.resize((20, 20))
closed_eye = ImageTk.PhotoImage(resized_closed_eye)

closed_eye_bright_org = Image.open("./resource/closed_eye_bright.png")
resized_closed_eye_bright = closed_eye_bright_org.resize((20, 20))
closed_eye_bright = ImageTk.PhotoImage(resized_closed_eye_bright)

open_eye_org = Image.open("./resource/open_eye.png")
resized_open_eye = open_eye_org.resize((20, 20))
open_eye = ImageTk.PhotoImage(resized_open_eye)

open_eye_bright_org = Image.open("./resource/open_eye_bright.png")
resized_open_eye_bright = open_eye_bright_org.resize((20, 20))
open_eye_bright = ImageTk.PhotoImage(resized_open_eye_bright)


def theme_change_dark(event):
    global background, canvas, dark_bg, img2, img3, theme_set, window
    theme_set.configure(image=light_mode_img)
    style.theme_use('dark')
    theme_set.bind("<Button>", theme_change_light)
    img2 = PhotoImage(file=f"./resource/img0.png")
    img3 = PhotoImage(file=f"./resource/img1.png")
    background = canvas.create_image(
        500.0, 300.0,
        image=dark_bg)
    window.configure(background='#333333')
    if style.theme_use() == 'dark':
        theme_set.configure(bg='#222222')


def theme_change_light(event):
    global style, background, canvas, light_bg, img2, img3, theme_set, window
    theme_set.configure(image=dark_mode_img)
    theme_set.bind("<Button>", theme_change_dark)
    img2 = PhotoImage(file=f"./resource/img0_light.png")
    img3 = PhotoImage(file=f"./resource/img1_light.png")
    background = canvas.create_image(
        500.0, 300.0,
        image=light_bg)
    style.theme_use('light')
    window.configure(background='white')
    if style.theme_use() == 'light':
        theme_set.configure(bg='white')


theme_set = Label(window,
                  image=dark_mode_img,
                  borderwidth=0,
                  highlightthickness=0)

theme_set.bind("<Button>", theme_change_dark)

theme_set.place(x=900, y=40)

entry0 = ttk.Entry(window)

entry0.place(
    x=503.0, y=140,
    width=395.0,
    height=46)

entry1 = ttk.Entry(window)

entry1.place(
    x=503.0, y=242,
    width=395.0,
    height=51)

entry2 = ttk.Entry(window)

entry2.place(
    x=503.0, y=357,
    width=395.0,
    height=77)

b0 = ttk.Button(window,
                text="GENERATE",
                command=pwd)

b0.place(
    x=500, y=472,
    width=174,
    height=47)

b1 = ttk.Button(window,
                text="Show Passwords",
                command=Execution)

b1.place(
    x=703, y=471,
    width=220,
    height=48)

window.resizable(False, False)
window.mainloop()
