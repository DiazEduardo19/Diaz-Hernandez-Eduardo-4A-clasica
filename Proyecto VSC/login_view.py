import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("inicio de sesion")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        tk.Label(root, text="Bienvenidos al sistema", font=("Arial", 16, "bold")).pack(pady=16)

        tk.Label(root, text="Ingresa tu nombre de usuario:", font=("Arial", 12)).pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Ingresa tu contraseña:", font=("Arial", 12)).pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Iniciar Sesión", command=self.login).pack(pady=20)

    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showinfo("Faltan datos", "Por favor de ingresar el usuario y contraseña")
            return

        if validar_credenciales(usuario, password):
            messagebox.showinfo("Acceso concedido", f"Bienvenido {usuario}")
        else:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

root = tk.Tk()
app = LoginApp(root)
root.mainloop()