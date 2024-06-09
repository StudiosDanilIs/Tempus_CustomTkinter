# LIBRERÍAS
from PIL import ImageTk, Image as imim
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

# módulos de la aplicación
from RelacionMariaDB.VerificarCuenta import verificar_sesion as Verificar
from Visual.Login.SubEstructuraLogin import SubventanaLogin as Subventana
from Visual.Login.InfoSubventana import InformacionTempus as Info


class CreateLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("480x670")
        self.root.resizable(0, 0)
        self.root.title("Login - Tempus Software")

        # creación de la ventana principal
        self.lgn_frame = Frame(self.root, bg="#E6F0F3")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # incorporación de la imagen de la ventana principal
        self.sign_in_image = imim.open("images\\logotipo.png")
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg="#E6F0F3")
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.pack(side="top", fill=tk.X, pady=30)

        # opcion del usuario para iniciar sesión o registrarse
        self.username_label = Label(
            self.lgn_frame,
            text="Usuario",
            anchor="w",
            bg="#E6F0F3",
            fg="#1E90FF",
            font=("yu gothic ui", 13, "bold"),
        )
        self.username_label.pack(fill=tk.X, padx=25, pady=8)
        # inserción de la entrada de texto para el usuario
        self.username_entry = Entry(
            self.lgn_frame,
            relief=FLAT,
            bg="#E6F0F3",
            font=("yu gothic ui ", 12, "bold"),
            insertbackground="#1E90FF",
        )
        self.username_entry.pack(fill=tk.X, padx=30, pady=0)

        self.username_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#1E90FF", highlightthickness=0
        )
        self.username_line.pack(fill=tk.X, padx=30, pady=1)

        # opcion del Clave para iniciar sesión o registrarse
        self.password_label = Label(
            self.lgn_frame,
            text="Contraseña",
            anchor="w",
            bg="#E6F0F3",
            fg="#1E90FF",
            font=("yu gothic ui", 13, "bold"),
        )
        self.password_label.pack(fill=tk.X, padx=25, pady=8)
        # inserción de la entrada de texto para la Clave
        self.password_entry = Entry(
            self.lgn_frame,
            relief=FLAT,
            bg="#E6F0F3",
            font=("yu gothic ui", 12, "bold"),
            show="*",
            insertbackground="#1E90FF",
        )
        self.password_entry.pack(fill=tk.X, padx=30, pady=0)

        self.password_line = Canvas(
            self.lgn_frame, width=300, height=2.0, bg="#1E90FF", highlightthickness=0
        )
        self.password_line.pack(fill=tk.X, padx=30, pady=1)

        # botón para iniciar sesión
        self.login = Button(
            self.lgn_frame,
            text="Iniciar Sesion",
            font=("yu gothic ui", 13, "bold"),
            width=42,
            bd=0,
            bg="#1E90FF",
            cursor="hand2",
            activebackground="#3047ff",
            fg="white",
            command=lambda: Verificar(self=self, root=root),
        )
        self.login.pack(pady=35)
        # botón para iniciar sesión con la tecla enter
        self.login.bind("<Return>", (lambda event: Verificar()))

        # botón para restaurar la contraseña y el usuario
        self.forgot_button = Button(
            self.lgn_frame,
            text="Restaurar Acceso",
            font=("yu gothic ui", 13, "bold"),
            fg="#1E90FF",
            relief=FLAT,
            activebackground="#4169E1",
            borderwidth=0,
            background="#E6F0F3",
            cursor="hand2",
            command=lambda: Subventana(self=self),
        )

        self.forgot_button.pack(pady=2)

        # información de la versión del software
        self.forgot_button = Button(
            self.lgn_frame,
            text="Version Beta 1",
            font=("yu gothic ui", 13, "bold"),
            fg="#1E90FF",
            relief=FLAT,
            activebackground="#4169E1",
            borderwidth=0,
            background="#E6F0F3",
            cursor="hand2",
            command=lambda: Info(self=self),
        )
        self.forgot_button.pack(pady=2)