import tkinter as tk
from tkinter import messagebox

USERNAME_BENAR = "admin"
PASSWORD_BENAR = "1234"

def login():
    try:
        username = entry_username.get()
        password = entry_password.get()

        if not username.isalpha():
            raise ValueError("Username harus berupa teks (huruf)")

        if not password.isdigit():
            raise ValueError("Password harus berupa angka")

        if username == USERNAME_BENAR and password == PASSWORD_BENAR:
            messagebox.showinfo("Login Berhasil", "Selamat, login berhasil!")
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah")

    except ValueError as error:
        messagebox.showwarning("Peringatan", str(error))

root = tk.Tk()
root.title("Program Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
