import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

# Creamos un diccionario con los datos
  
class App(ttk.Frame):
    '''Generamos la ventana principal del recetario'''
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.window = parent
        self.window.title("RECETARIO") #Damos el nombre a la ventana
        self.window.geometry("1750x400") #Establecemos atributos de tamaño
        self.window.iconbitmap("favicon.ico") #Cambiamos el ícono de la ventana
        menubar = tk.Menu(root) #Creamos una barra de Menus
        root.config(menu=menubar)

        filemenu=tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Crear', command=self.ventana_crearReceta) #Agregamos submenú
        filemenu.add_command(label='Buscar', command=self.ventana_buscarReceta) #Agregamos submenú
        filemenu.add_command(label='Eliminar', command=self.ventana_eliminarReceta) #Agregamos submenú
        menubar.add_cascade(label='Recetas', menu=filemenu)#Damos el atributo de cascada a los submenú

        ttk.Label(self,text='Lista de Recetas', padding=3, font = ("Segoe Print", 14)).grid(row=1, column=2) #Label que funciona de título de lo que muestra la ventana principal por defecto

        with open("recetarioprueba.csv", newline = "") as archivo:
            lector = csv.DictReader(archivo)
            lista_recetas = list(lector)
            contador = 2
            for receta in lista_recetas:
                nombre = receta["Nombre"]
                ingredientes = receta["Ingredientes"]
                fecha = receta["Fecha de creacion"]
                label = f"Nombre: {nombre} - Ingredientes: {ingredientes} - Fecha: {fecha}"
                ttk.Label(self,text=label, padding=3, font = "Roboto 12 bold").grid(row=contador, column=2) #Label que funciona de título de lo que muestra la ventana principal por defecto
                contador += 1

    def ventana_crearReceta(self):
        '''Creamos una ventana secundaria para crear una receta, indicando como padre la ventana principal'''
        ventana_crearReceta=tk.Toplevel(self.window)
        Receta(ventana_crearReceta).grid()
    
    def ventana_buscarReceta(self):
        '''Creamos una ventana secundaria para buscar una receta, indicando como padre la ventana principal'''
        ventana_buscarReceta=tk.Toplevel(self.window)
        BuscarReceta(ventana_buscarReceta).grid()
    
    def ventana_eliminarReceta(self):
        '''Creamos una ventana secundaria para eliminar una receta, indicando como padre la ventana principal'''
        ventana_eliminarReceta=tk.Toplevel(self.window)
        EliminarReceta(ventana_eliminarReceta).grid()

class Receta(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent, padding=10)
        self.window=parent
        self.window.title('Crear Receta')
        self.window.iconbitmap('favicon.ico')
        self.nombre=tk.StringVar()
        self.ingredientes=tk.StringVar()
        self.ingredientes1=tk.StringVar()
        self.ingredientes2=tk.StringVar()
        self.ingredientes3=tk.StringVar()
        self.ingredientes4=tk.StringVar()
        self.preparacion=tk.StringVar()
        self.preparacion1=tk.StringVar()
        self.preparacion2=tk.StringVar()
        #self.imagen 
        self.tiempo_preparacion=tk.StringVar()
        self.tiempo_coccion=tk.StringVar()
        self.fecha_creacion=tk.StringVar()
        self.fecha_creacion.set(datetime.now().strftime('%d/%m/%Y - %H:%M'))
        #se puede agregar etiqueta como palabra clave y si es favorita o no, como accesorio

        '''Creamos los label y entry necesarios para crear la receta'''
        ttk.Label(self,text='Crea tu receta', padding=3, font = ("Segoe Print", 14)).grid(row=1, column=2)
        ttk.Label(self,text='Nombre', padding=3, font = ("Segoe Print", 10)).grid(row=2, column=1) #fila 1 columna 1
        ttk.Entry(self, textvariable=self.nombre).grid(row=2, column=2) #fila 1 columna 2
        ttk.Label(self,text='Ingredientes', padding=3, font = ("Segoe Print", 10)).grid(row=3, column=1) #fila 2 columna 1
        ttk.Label(self,text='Utilice más de un ingrediente por fila', padding=3, font = ("Segoe Print", 10)).grid(row=4, column=1) #fila 3 columna 1
        ttk.Entry(self, textvariable=self.ingredientes).grid(row=3, column=2) #fila 2 columna 2
        ttk.Entry(self, textvariable=self.ingredientes1).grid(row=4, column=2) #fila 3 columna 2
        ttk.Entry(self, textvariable=self.ingredientes2).grid(row=5, column=2) #fila 4 columna 2
        ttk.Entry(self, textvariable=self.ingredientes3).grid(row=6, column=2) #fila 5 columna 2
        ttk.Entry(self, textvariable=self.ingredientes4).grid(row=7, column=2) #fila 6 columna 2
        ttk.Label(self,text='Preparación', padding=3, font = ("Segoe Print", 10)).grid(row=8, column=1) #fila 7 columna 1
        ttk.Label(self,text='Utilice más de un paso de preparación por fila', padding=3, font = ("Segoe Print", 10)).grid(row=9, column=1) #fila 8 columna 1
        ttk.Entry(self, textvariable=self.preparacion).grid(row=8, column=2) #fila 7 columna 2
        ttk.Entry(self, textvariable=self.preparacion1).grid(row=9, column=2) #fila 8 columna 2
        ttk.Entry(self, textvariable=self.preparacion2).grid(row=10, column=2) #fila 8 columna 2
        #ttk.Label(self, text='Imagen receta', padding=3).grid(row=4, column=1)
        #ttk.Entry(self, textvariable=self.imagen).grid(row=4, column=2)
        ttk.Label(self,text='Tiempo de Preparación', padding=3, font = ("Segoe Print", 10)).grid(row=11, column=1) #fila 9 columna 1
        ttk.Entry(self, textvariable=self.tiempo_preparacion).grid(row=11, column=2) #fila 9 columna 2
        ttk.Label(self,text='Tiempo de Cocción', padding=3, font = ("Segoe Print", 10)).grid(row=12, column=1) #fila 10 columna 1
        ttk.Entry(self, textvariable=self.tiempo_coccion).grid(row=12, column=2) #fila 10 columna 2
        ttk.Label(self,text='Fecha de creación', padding=3, font = ("Segoe Print", 10)).grid(row=13, column=1) #fila 11 columna 1
        ttk.Entry(self, textvariable=self.fecha_creacion).grid(row=13, column=2) #fila 11 columna 2

        btn_guardar=ttk.Button(self, text='Guardar', command=self.crear_receta)
        btn_cancelar=ttk.Button(self, text='Cancelar', command=self.window.destroy)
        btn_cancelar.grid(row=14, column=2)
        btn_guardar.grid(row=14, column=3)

    def crear_receta(self):
        '''Función para capturar los datos de los entry, crear la receta y guardarlo en un archivo csv'''
        recetas={} #Diccionario que almacena toda la información ingresada por el usuario
        """Variables de control de datos"""
        if self.nombre.get() != '':
            recetas['Nombre']=self.nombre.get()
        else:
            messagebox.showerror(message='Debe ingresar un nombre de la receta')
        if self.ingredientes.get() != '' and self.ingredientes1.get() != '' and self.ingredientes2.get() != '' and self.ingredientes3.get() != '' and self.ingredientes4.get() != '':
            recetas['Ingredientes']=[self.ingredientes.get(), self.ingredientes1.get(), self.ingredientes2.get(), self.ingredientes3.get(), self.ingredientes4.get()]
        else:
            messagebox.showerror(message='Debe ingresar por lo menos CINCO INGREDIENTES de la receta')
        if self.preparacion.get() != '' and self.preparacion1.get() != '' and self.preparacion2.get() != '':
            recetas['Preparacion']=[self.preparacion.get(), self.preparacion1.get(), self.preparacion2.get()]
        else:
            messagebox.showerror(message='Debe ingresar la preparación de la receta')
        if self.tiempo_preparacion.get() != '':
            recetas['Tiempo de preparacion']=self.tiempo_preparacion.get()
        else:
            messagebox.showerror(message='Debe ingresar el tiempo de la preparación')
        if self.tiempo_coccion.get() != '':
            recetas['Tiempo de coccion']=self.tiempo_coccion.get()
        else:
            messagebox.showerror(message='Debe ingresar el tiempo de cocción')
        if self.fecha_creacion.get() != '':
            recetas['Fecha de creacion']=self.fecha_creacion.get()
        else:
            messagebox.showerror(message='Debe ingresar la fecha de creación de la receta')
        
        encabezado = ("Nombre", "Ingredientes", "Preparacion", "Tiempo de preparacion", "Tiempo de coccion", "Fecha de creacion")

        with open("recetarioprueba.csv", "r") as archivo:
            """Abrimos el archivo csv en modo lectura para poder obtener una lista de diccionarios y agregar la receta que el usuario está creando"""
            lector = csv.DictReader(archivo)
            recetario = list(lector)
            recetario.append(recetas) #Agregamos a la lista la receta ingresada
        
        with open("recetarioprueba.csv", "w", newline = "") as archivo:
            """Abrimos el archivo csv en modo escritura para poder agregar la receta ingresada por el usuario"""
            escritor = csv.DictWriter(archivo, fieldnames = encabezado)
            escritor.writeheader()
            escritor.writerows(recetario)
            messagebox.showinfo(message = "¡Receta guardada con éxito") #Se muestra mensaje de éxito al guardar la receta
            self.window.destroy() #Se cierra la ventana secundaria

class BuscarReceta(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.window = parent
        self.window.title('Buscar Receta')
        self.window.iconbitmap('favicon.ico')
        self.nombreReceta = tk.StringVar()
        self.valorEncontrado = tk.StringVar()
        self.valorEncontrado2 = tk.StringVar()
        self.valorEncontrado3 = tk.StringVar()
        self.valorEncontrado4 = tk.StringVar()
        self.valorEncontrado5 = tk.StringVar()
        self.valorEncontrado6 = tk.StringVar()

        ttk.Label(self, text='Buscador', padding=3, font = ("Segoe Print", 14)).grid(row=1, column=2)
        ttk.Label(self, text='Nombre Receta', padding=3, font = ("Segoe Print", 10)).grid(row=2, column=1)
        ttk.Entry(self, textvariable=self.nombreReceta, width = 80).grid(row=2, column=2)
        ttk.Label(self, text='Tu Receta', padding=3, font = ("Segoe Print", 14)).grid(row=4, column=2)
        self.lbllabel= ttk.Label(self, text="Nombre:", padding=3, font = ("Segoe Print", 10)).grid(row=5, column=1)
        ttk.Entry(self, textvariable=self.valorEncontrado, width = 80).grid(row=5, column=2)
        self.lbllabel= ttk.Label(self, text="Ingredientes:", padding=3, font = ("Segoe Print", 10)).grid(row=6, column=1)
        ttk.Entry(self, textvariable=self.valorEncontrado2, width = 80).grid(row=6, column=2)
        self.lbllabel= ttk.Label(self, text="Preparación", padding=3, font = ("Segoe Print", 10)).grid(row=7, column=1)
        ttk.Entry(self, textvariable=self.valorEncontrado3, width = 80).grid(row=7, column=2)
        self.lbllabel= ttk.Label(self, text="Tiempo de Preparación:", padding=3, font = ("Segoe Print", 10)).grid(row=8, column=1)
        ttk.Entry(self, textvariable=self.valorEncontrado4, width = 80).grid(row=8, column=2)
        self.lbllabel= ttk.Label(self, text="Tiempo de cocción:", padding=3, font = ("Segoe Print", 10)).grid(row=9, column=1)
        ttk.Entry(self, textvariable=self.valorEncontrado5, width = 80).grid(row=9, column=2)
        self.lbllabel= ttk.Label(self, text="Fecha de creación:", padding=3, font = ("Segoe Print", 10)).grid(row=10, column=1)
        ttk.Entry(self, textvariable=self.valorEncontrado6, width = 80).grid(row=10, column=2)

        btn_buscar = ttk.Button(self, text="Buscar", command=self.buscar_receta)
        btn_buscar.grid(row=3, column=3)
        btn_modificar = ttk.Button(self, text="Modificar", command=self.modificar_receta)
        btn_modificar.grid(row=11, column=2, padx=5, pady=5)

    def buscar_receta(self):
        with open("recetarioprueba.csv", "r") as archivo:
            lector = csv.reader(archivo)
            header = next(lector)
            nombreReceta = header.index("Nombre")
            encontrado = False
            for row in lector:
                cadena=row[0] #Nombre
                cadena2=row[1] #Ingredientes
                cadena3=row[2] #Preparación
                cadena4=row[3] #Tiempo de preparación
                cadena5=row[4] #Tiempo de cocción
                cadena6=row[5] #Fecha de creación
                if cadena == self.nombreReceta.get():
                    self.valorEncontrado.set(cadena)        
                    self.valorEncontrado2.set(cadena2)
                    self.valorEncontrado3.set(cadena3)
                    self.valorEncontrado4.set(cadena4)
                    self.valorEncontrado5.set(cadena5)
                    self.valorEncontrado6.set(cadena6)
                    encontrado = True
            if encontrado == True:
                pass
            else:
                messagebox.showerror(message = "¡Receta no encontrada! Verifique el nombre de la receta")

    def modificar_receta(self):
        """Función para modificar la receta previamente buscada"""
        encabezado = ("Nombre", "Ingredientes", "Preparacion", "Tiempo de preparacion", "Tiempo de coccion", "Fecha de creacion")
        with open("recetarioprueba.csv", "r") as archivo:
            """Abrimos el archivo csv en modo lectura para poder obtener una lista de diccionarios y modificar la receta buscada"""
            lector = csv.DictReader(archivo)
            recetario = list(lector)
            for receta in recetario:
                for k,v in receta.items():
                    if k == "Nombre":
                        if v == self.nombreReceta.get():
                            receta["Nombre"] = self.nombreReceta.get()
                            receta["Ingredientes"] = [self.valorEncontrado2.get()]
                            receta["Preparacion"] = [self.valorEncontrado3.get()]
                            receta["Tiempo de preparacion"] = self.valorEncontrado4.get()
                            receta["Tiempo de coccion"] = self.valorEncontrado5.get()
                            receta["Fecha de creacion"] = self.valorEncontrado6.get()
            recetario.append(receta) #Agregamos a la lista la receta ingresada
        
        with open("recetarioprueba.csv", "w", newline = "") as archivo:
            """Abrimos el archivo csv en modo escritura para poder agregar la receta ingresada por el usuario"""
            escritor = csv.DictWriter(archivo, fieldnames = encabezado)
            escritor.writeheader()
            escritor.writerows(recetario)
            messagebox.showinfo(message = "¡Receta guardada con éxito") #Se muestra mensaje de éxito al guardar la receta
            self.window.destroy() #Se cierra la ventana secundaria

class EliminarReceta(ttk.Frame):
    """Clase que permite eliminar recetas"""
    lista_recetas = []

    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.window = parent
        self.window.title('Eliminar Receta')
        self.window.iconbitmap('favicon.ico')
         # Dividimos la ventana en dos secciones
        buscador = ttk.Frame(self)
        buscador.grid(row=0, column=0, sticky='nsew')
        resultados = ttk.Frame(self)
        resultados.grid(row=0, column=1, columnspan=2, sticky='nsew')
        # Asignamos proporciones a las columnas
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=3)
        self.window.columnconfigure(2, weight=3)

        self.nombreReceta = tk.StringVar()
        ttk.Label(buscador, text='Ingrese el nombre de la receta a eliminar: ', padding=3, font = ("Segoe Print", 10)).grid(row=0, column=0, sticky='w', padx=5, pady=5)
        ttk.Entry(buscador, textvariable=self.nombreReceta).grid(row=0, column=1, padx=5, pady=5)
        btn_eliminar = ttk.Button(buscador, text="Eliminar", command=self.eliminar_receta)
        btn_eliminar.grid(row=0, column=2, padx=5, pady=5)


    def eliminar_receta(self):
        nombre_receta = self.nombreReceta.get()
        with open("recetarioprueba.csv", "r") as archivo:
            lector = csv.reader(archivo)
            header = next(lector)
            nombreReceta = header.index("Nombre")
            lista_recetas = [row for row in lector if row[nombreReceta] != nombre_receta]

        # Escribir la lista de recetas actualizada en el archivo
        with open("recetarioprueba.csv", "w", newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(header)
            escritor.writerows(lista_recetas)

        if len(self.lista_recetas) != len(lista_recetas):
            self.lista_recetas = lista_recetas
            messagebox.showinfo("Receta eliminada", f"La receta {nombre_receta} ha sido eliminada.")
        else:
            messagebox.showerror("Receta no encontrada", f"No se encontró ninguna receta con el nombre {nombre_receta}.")

root = tk.Tk()
App(root).grid()
root.mainloop()
