import os
import shutil
import pandas as pd
from tkinter import *
from tkinter import filedialog
import webbrowser

def seleccionar_carpeta_imagenes():
    ruta_imagenes = filedialog.askdirectory()
    entry_ruta_imagenes.delete(0, END)
    entry_ruta_imagenes.insert(0, ruta_imagenes)

def seleccionar_archivo_excel():
    ruta_excel = filedialog.askopenfilename(filetypes=[("Archivos de Excel", "*.xlsx")])
    entry_ruta_excel.delete(0, END)
    entry_ruta_excel.insert(0, ruta_excel)

def mover_imagenes():
    ruta_imagenes = entry_ruta_imagenes.get()
    ruta_excel = entry_ruta_excel.get()
    df = pd.read_excel(ruta_excel)
    
    for index, row in df.iterrows():
        nombre_imagen = row.iloc[0]
        carpeta_destino = row.iloc[1]
        
        nombre_imagen_con_extension = nombre_imagen + ".jpg"
        ruta_origen = os.path.join(ruta_imagenes, nombre_imagen_con_extension)
        
        if os.path.isfile(ruta_origen):
            ruta_destino_base = os.path.join(ruta_imagenes, carpeta_destino)
            if not os.path.exists(ruta_destino_base):
                os.makedirs(ruta_destino_base)
            
            ruta_destino = os.path.join(ruta_destino_base, nombre_imagen_con_extension)
            shutil.copy(ruta_origen, ruta_destino)
        else:
            print(f"La imagen {nombre_imagen} no existe en la carpeta de imágenes.")


def abrir_pagina_web():
    url = "https://github.com/vasossvacioss"  # Reemplaza con la URL que deseas abrir
    webbrowser.open(url)

# Crear la ventana de la interfaz gráfica
ventana = Tk()
ventana.title("Copiar imágenes")

# Etiqueta y campo de entrada para la ruta de la carpeta de imágenes
label_ruta_imagenes = Label(ventana, text="Ruta de la carpeta de imágenes:")
label_ruta_imagenes.pack()
entry_ruta_imagenes = Entry(ventana)
entry_ruta_imagenes.pack()
button_seleccionar_imagenes = Button(ventana, text="Seleccionar carpeta", command=seleccionar_carpeta_imagenes)
button_seleccionar_imagenes.pack()

# Etiqueta y campo de entrada para la ruta del archivo de Excel
label_ruta_excel = Label(ventana, text="Ruta del archivo de Excel:")
label_ruta_excel.pack()
entry_ruta_excel = Entry(ventana)
entry_ruta_excel.pack()
button_seleccionar_excel = Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo_excel)
button_seleccionar_excel.pack()

# Botón para iniciar el proceso de copiar imágenes
boton_copiar = Button(ventana, text="Copiar imágenes", command=mover_imagenes)
boton_copiar.pack()

# Botón para abrir la página web
boton_web = Button(ventana, text="Repositorio GitHub", command=abrir_pagina_web)
boton_web.pack()

# Leyenda o etiqueta
leyenda = Label(ventana, text="Desarrollado por Javier Romero")
leyenda.pack()

# Ejecutar la ventana de la interfaz gráfica
ventana.mainloop()
