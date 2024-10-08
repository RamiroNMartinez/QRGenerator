import customtkinter as ctk

# Inicializamos la ventana principal
app = ctk.CTk()
app.geometry("400x300")


# Clase que gestiona el cambio de pantallas
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Generador QR")
        self.resizable(False, False)

        # Creamos un contenedor donde se mostrarán los frames
        self.container = ctk.CTkFrame(self, width=400, height=300)
        self.container.pack(fill="both", expand=True)

        # Diccionario para almacenar las pantallas
        self.frames = {}

        # Inicializamos las pantallas
        for F in (Pantalla1, Pantalla2):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mostramos la primera pantalla al iniciar
        self.mostrar_pantalla(Pantalla1)

    def mostrar_pantalla(self, pantalla):

        frame = self.frames[pantalla]
        frame.tkraise()


# Definimos las pantallas como clases que heredan de CTkFrame
class Pantalla1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label1 = ctk.CTkLabel(self, text="Ingresa el link a la página:")
        label1.pack(pady=10)

        urlIn = ctk.CTkEntry(self, placeholder_text="Link")
        urlIn.pack(pady=5)

        label2 = ctk.CTkLabel(self, text="Ingresa el nombre de la imagen:")
        label2.pack(pady=10)

        titleIn = ctk.CTkEntry(self, placeholder_text="Título")
        titleIn.pack(pady=5)

        button = ctk.CTkButton(
            self,
            text="Crear QR",
            command=lambda: controller.mostrar_pantalla(Pantalla2),
        )
        button.pack(pady=20)


class Pantalla2(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Esta es la Pantalla 2")
        label.pack(pady=20)

        # Botón para regresar a Pantalla 1
        boton_cambio = ctk.CTkButton(
            self,
            text="Regresar a Pantalla 1",
            command=lambda: controller.mostrar_pantalla(Pantalla1),
        )
        boton_cambio.pack(pady=20)


# Ejecutamos la aplicación
app = App()
app.grid_rowconfigure(0, weight=1)
app.mainloop()


# url = urlIn.get()
# title = titleIn.get()
