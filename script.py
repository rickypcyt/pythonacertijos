import tkinter as tk
from tkinter import messagebox
import random


# Función para leer los acertijos desde un archivo
def leer_acertijos(nombre_archivo):
    acertijos = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            acertijo, solucion = linea.strip().split(";")
            acertijos.append((acertijo, solucion))
    return acertijos


# Declarar variables globales para el acertijo actual y su solución
acertijo_actual = ""
solucion_actual = ""


# Función para mostrar un nuevo acertijo
def mostrar_nuevo_acertijo(acertijos, label_acertijo, respuesta_usuario):
    global acertijo_actual, solucion_actual
    acertijo_actual, solucion_actual = random.choice(acertijos)
    respuesta_usuario.set("")  # Limpiar la respuesta anterior
    label_acertijo.config(text=acertijo_actual)


# Función para comprobar la respuesta del usuario
def comprobar_respuesta(acertijos, respuesta_usuario):
    global acertijo_actual, solucion_actual
    solucion_ingresada = respuesta_usuario.get().strip().lower()
    if solucion_ingresada == solucion_actual.lower():
        messagebox.showinfo("¡Correcto!", "¡Bien hecho! La respuesta es correcta.")
    else:
        messagebox.showerror(
            "Incorrecto", "Lo siento, la respuesta correcta es: " + solucion_actual
        )


# Función para preguntar nombre y edad y mostrar acertijos
def preguntar_nombre_y_edad():
    nombre = nombre_usuario.get()
    edad = edad_usuario.get()
    messagebox.showinfo(
        "Bienvenido",
        f"¡Hola, {nombre}! Ya que tienes {edad} años de edad, ¿estás listo para resolver algunos acertijos?",
    )
    mostrar_acertijos()  # Mostrar los acertijos


# Función para mostrar los acertijos
def mostrar_acertijos():
    # Leer los acertijos desde el archivo
    archivo_acertijos = "pythonacertijos/acertijos.txt"
    acertijos = leer_acertijos(archivo_acertijos)

    # Ocultar los widgets de nombre y edad
    nombre_label.pack_forget()
    entry_nombre.pack_forget()
    edad_label.pack_forget()
    entry_edad.pack_forget()
    boton_continuar.pack_forget()

    # Etiqueta para mostrar el acertijo
    label_acertijo = tk.Label(ventana, text="", wraplength=450)
    label_acertijo.pack(pady=10)

    # Campo de entrada para la respuesta del usuario
    respuesta_usuario = tk.StringVar()
    entry_respuesta = tk.Entry(ventana, textvariable=respuesta_usuario)
    entry_respuesta.pack(pady=5)

    # Botón para comprobar la respuesta
    boton_comprobar = tk.Button(
        ventana,
        text="Comprobar respuesta",
        command=lambda: comprobar_respuesta(acertijos, respuesta_usuario),
    )
    boton_comprobar.pack(pady=5)

    # Botón para mostrar un nuevo acertijo
    boton_nuevo_acertijo = tk.Button(
        ventana,
        text="Nuevo acertijo",
        command=lambda: mostrar_nuevo_acertijo(
            acertijos, label_acertijo, respuesta_usuario
        ),
    )
    boton_nuevo_acertijo.pack(pady=5)

    # Mostrar el primer acertijo
    mostrar_nuevo_acertijo(acertijos, label_acertijo, respuesta_usuario)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Resuelve el acertijo")
ventana.geometry("500x400")  # Establecer las dimensiones de la ventana

# Preguntar al usuario su nombre y edad
nombre_label = tk.Label(ventana, text="¡Hola! ¿Cómo te llamas?")
nombre_label.pack()
nombre_usuario = tk.StringVar()
entry_nombre = tk.Entry(ventana, textvariable=nombre_usuario)
entry_nombre.pack()

edad_label = tk.Label(ventana, text="¿Cuál es tu edad?")
edad_label.pack()
edad_usuario = tk.StringVar()
entry_edad = tk.Entry(ventana, textvariable=edad_usuario)
entry_edad.pack()

# Botón para continuar después de ingresar nombre y edad
boton_continuar = tk.Button(ventana, text="Continuar", command=preguntar_nombre_y_edad)
boton_continuar.pack()

# Mostrar la ventana
ventana.mainloop()
