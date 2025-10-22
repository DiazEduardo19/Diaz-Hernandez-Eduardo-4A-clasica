import tkinter as tk
from tkinter import messagebox

class DashboardApp:
    def __init__(self, usuario): 
        self.username = usuario  
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {usuario}")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.crear_elementos() 
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"Hola {self.username}", font=("Arial",22, "bold")).pack(pady=10)

        tk.Button(self.root, text="Ver usuarios", width=20, command=self.ver_usuarios).pack(pady=20)

        tk.Button(self.root, text="Actualizar usuarios", width=20, command=self.actualizar_usuarios).pack(pady=20)

        tk.Button(self.root, text="Eliminar usuarios", width=20, command=self.eliminar_usuarios).pack(pady=20)

        tk.Button(self.root, text="Cerrar sesion", width=50, command=self.cerrar_sesion).pack(pady=20)

    def ver_usuarios(self): 
        messagebox.showinfo("Ver lista", "Funcion")

    def actualizar_usuarios(self):
        messagebox.showinfo("Actualizar usuario", "Funcion")
    
    def eliminar_usuarios(self):
        messagebox.showinfo("Eliminar usuario", "Funcion")

    def cerrar_sesion(self):
        self.root.destroy()

if __name__ == "__main__":
    App = DashboardApp("Eduardo")