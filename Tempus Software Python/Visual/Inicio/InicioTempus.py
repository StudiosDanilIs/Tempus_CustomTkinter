from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
import util.ImagenRead as utl
from Visual.Inicio.VentanaCliente import agregar_cliente as new_client


class VentanaPrincipal:
    def __init__(self, usuario):
        self.root2 = tk.Tk()
        self.root2.title("Inicio - Tempus Software")
        self.root2.geometry("1100x600")
        self.root2.resizable(0, 0)
        rol_programa = usuario

        # Create a frame to contain elements
        self.lgn_frame = Frame(self.root2, bg="#FFFFFF")
        self.lgn_frame.pack(expand=tk.YES, fill=tk.BOTH)

        # Cargar la imagen de fondo
        logo = utl.leer_imagen("images//1.png", (200, 200))
        self.logo_inicio_label = tk.Label(self.lgn_frame, image=logo, bg="#FFFFFF")
        self.logo_inicio_label.image = logo
        self.logo_inicio_label.place(relx=0.5, rely=0.36, anchor=tk.CENTER)
        
        
        self.rol_label = Label(
            self.lgn_frame,
            text=f"Nivel de Permisos: {rol_programa}",
            anchor="center",
            bg="#FFFFFF",
            fg="#000000",
            font=("Exo 2", 14),
        )
        self.rol_label.pack(fill=tk.BOTH, pady=14, padx=(545,2))

        # Etiqueta de bienvenida
        self.username_label = Label(
            self.lgn_frame,
            text="Welcome to\n Tempus Software.",
            anchor="center",
            bg="#FFFFFF",
            fg="#000000",
            font=("Exo 2", 21),
        )
        self.username_label.place(relx=0.5, rely=0.60, anchor=CENTER)

        # Etiqueta del rol
        self.rol_label = Label(
            self.lgn_frame,
            text="Tu aliado tecnológico: eficiencia y confianza al\n alcance de tu mano.",
            bg="#FFFFFF",
            fg="#000000",
            font=("Inconsolata", 12),
        )
        self.rol_label.place(relx=0.5, rely=0.70, anchor=CENTER)

        # Menú principal
        self.menu_tempus = tk.Menu(self.root2, tearoff=0)
        self.root2.config(menu=self.menu_tempus)

        # Menú de solicitud
        self.opcion_solicitud = tk.Menu(self.menu_tempus, tearoff=0)
        self.menu_tempus.add_cascade(label="Solicitudes", menu=self.opcion_solicitud)

        self.opcion_solicitud.add_command(label="Crear Pedido")
        self.opcion_solicitud.add_command(label="Crear Venta")
        self.opcion_solicitud.add_command(label="Crear Reparaciones")

        # Menú de clientes
        self.opcion_clientes = tk.Menu(self.menu_tempus, tearoff=0)
        self.menu_tempus.add_cascade(label="Clientes", menu=self.opcion_clientes)
        self.opcion_clientes.add_command(label="Clientes")
        self.opcion_clientes.add_command(label="Agregar Clientes", command=lambda: self.agregar_cliente_con_self())

        # Menú de Historial
        self.opcion_historial = tk.Menu(self.menu_tempus, tearoff=0)
        self.menu_tempus.add_cascade(label="Historial", menu=self.opcion_historial)
        self.opcion_historial.add_command(label="Ventas")
        self.opcion_historial.add_command(label="Pedidos")
        self.opcion_historial.add_command(label="Reparaciones")

        # Menú de Herramientas
        self.menu_tempus.add_cascade(
            label="Salir del Sistema", command=self.Close_Windows
        )
        
        self.root2.mainloop() 
        
    def agregar_cliente_con_self(self):
        new_client(self)
    
    # Función para cerrar la ventana
    def Close_Windows(self):
        if messagebox.askokcancel("Close", "¿Desea Cerrar la Aplicación?"):
            self.root2.destroy()
               


# Crear una instancia de la ventana principal
if __name__ == "__main__":
    # ventana = VentanaPrincipal()
    # ventana.root2.mainloop()
    VentanaPrincipal()