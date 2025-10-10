from tkinter import *
from tkinter import messagebox, Toplevel, Text, Label, END
import base64
import os

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#50C878")

        message = text1.get(1.0, END).strip()

        if message == "":
            messagebox.showerror("Error", "Please enter text to decrypt.")
            return

        # Decrypt base64
        try:
            decoded_bytes = base64.b64decode(message.encode("ascii"))
            decrypted = decoded_bytes.decode("ascii")
        except Exception:
            messagebox.showerror("Error", "Invalid encrypted text!")
            return

        Label(screen2, text="DECRYPTED TEXT", font="Arial 12 bold", fg="white", bg="#50C878").place(x=10, y=5)

        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypted)
    elif password == "":
        messagebox.showerror("Error", "Please enter a password!")
    else:
        messagebox.showerror("Error", "Invalid password! Use 1234.")



def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()

        if message == "":
            messagebox.showerror("Error", "Please enter text to encrypt.")
            return

        # Encrypt using base64
        encoded_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded_message)
        encrypted = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED TEXT", font="Arial 12 bold", fg="white", bg="#ed3833").place(x=10, y=5)

        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypted)
    elif password == "":
        messagebox.showerror("Error", "Please enter a password!")
    else:
        messagebox.showerror("Error", "Invalid password! Use 1234.")
        
def main_screen():

    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Text Encryption Generator")

    # icon 
    image_icon = PhotoImage(file="/Users/afeefur/Desktop/CSE 115/VS code/My-Python-Projects/My-Python-Projects/Text Encryption Project/keys.png")
    screen.iconphoto(False, image_icon)

    def reset(event=None):
        code.set("")
        text1.delete(1.0, END)

    Label(
        text="Enter text for encryption and decryption",
        fg="black",
        font=("Times New Roman", 13)
    ).place(x=10, y=10)

    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(
        text="Enter secret key for encryption and decryption",
        fg="black",
        font=("Times New Roman", 13)
    ).place(x=10, y=170)

    code = StringVar()
    Entry(
        textvariable=code,
        width=19,
        bd=0,
        font=("arial", 25),
        show="*"
    ).place(x=10, y=200)

    # --- Custom buttons (Labels for color persistence) ---
    encrypt_btn = Label(
        text="Encrypt",
        bg="#ed3833",
        fg="white",
        width=23,
        height=2,
        font=("Arial", 10),
        cursor="hand2"
    )
    encrypt_btn.place(x=10, y=250)
    encrypt_btn.bind("<Button-1>", lambda event: encrypt())  

    decrypt_btn = Label(
        text="Decrypt",
        bg="#50C878",
        fg="white",
        width=23,
        height=2,
        font=("Arial", 10),
        cursor="hand2"
    )
    decrypt_btn.place(x=200, y=250)
    decrypt_btn.bind("<Button-1>", lambda event: decrypt()) 

    reset_btn = Label(
        text="Reset",
        bg="#1089ff",
        fg="white",
        width=50,
        height=2,
        font=("Arial", 10),
        cursor="hand2"
    )
    reset_btn.place(x=10, y=300)
    reset_btn.bind("<Button-1>", reset)

    screen.mainloop()



main_screen()
from tkinter import *
from tkinter import messagebox, Toplevel, Text, Label, END
import base64
import os

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#50C878")

        message = text1.get(1.0, END).strip()

        if message == "":
            messagebox.showerror("Error", "Please enter text to decrypt.")
            return

        # Decrypt base64
        try:
            decoded_bytes = base64.b64decode(message.encode("ascii"))
            decrypted = decoded_bytes.decode("ascii")
        except Exception:
            messagebox.showerror("Error", "Invalid encrypted text!")
            return

        Label(screen2, text="DECRYPTED TEXT", font="Arial 12 bold", fg="white", bg="#50C878").place(x=10, y=5)

        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypted)
    elif password == "":
        messagebox.showerror("Error", "Please enter a password!")
    else:
        messagebox.showerror("Error", "Invalid password! Use 1234.")



def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()

        if message == "":
            messagebox.showerror("Error", "Please enter text to encrypt.")
            return

        # Encrypt using base64
        encoded_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded_message)
        encrypted = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED TEXT", font="Arial 12 bold", fg="white", bg="#ed3833").place(x=10, y=5)

        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypted)
    elif password == "":
        messagebox.showerror("Error", "Please enter a password!")
    else:
        messagebox.showerror("Error", "Invalid password! Use 1234.")
        
def main_screen():

    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Text Encryption Generator")

    # icon 
    image_icon = PhotoImage(file="/Users/afeefur/Desktop/CSE 115/VS code/My-Python-Projects/My-Python-Projects/Text Encryption Project/keys.png")
    screen.iconphoto(False, image_icon)

    def reset(event=None):
        code.set("")
        text1.delete(1.0, END)

    Label(
        text="Enter text for encryption and decryption",
        fg="black",
        font=("Times New Roman", 13)
    ).place(x=10, y=10)

    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(
        text="Enter secret key for encryption and decryption",
        fg="black",
        font=("Times New Roman", 13)
    ).place(x=10, y=170)

    code = StringVar()
    Entry(
        textvariable=code,
        width=19,
        bd=0,
        font=("arial", 25),
        show="*"
    ).place(x=10, y=200)

    # --- Custom buttons (Labels for color persistence) ---
    encrypt_btn = Label(
        text="Encrypt",
        bg="#ed3833",
        fg="white",
        width=23,
        height=2,
        font=("Arial", 10),
        cursor="hand2"
    )
    encrypt_btn.place(x=10, y=250)
    encrypt_btn.bind("<Button-1>", lambda event: encrypt())  

    decrypt_btn = Label(
        text="Decrypt",
        bg="#50C878",
        fg="white",
        width=23,
        height=2,
        font=("Arial", 10),
        cursor="hand2"
    )
    decrypt_btn.place(x=200, y=250)
    decrypt_btn.bind("<Button-1>", lambda event: decrypt()) 

    reset_btn = Label(
        text="Reset",
        bg="#1089ff",
        fg="white",
        width=50,
        height=2,
        font=("Arial", 10),
        cursor="hand2"
    )
    reset_btn.place(x=10, y=300)
    reset_btn.bind("<Button-1>", reset)

    screen.mainloop()



main_screen()
