# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:13:32 2024

@author: ProtofurOwO
Z"""
import tkinter as tk
from tkinter import messagebox
import re
def guardar_valores():
    if not validar_datos():
        return False
    
    nombres= tbnombre.get()
    apellidos= tbapellidos.get()
    edad= tbedad.get()
    estatura=tbestatura.get()
    telefono=tbtelefono.get()
    genero=""
    if var_genero.get()==1:
        genero="Hombre"
    elif var_genero.get()==2:
        genero="Mujer"
    datos= "Nombres: " + nombres + "\nApellidos: " + apellidos + "\nEdad: "+ edad +" años\n" + "Estatura: "+estatura + "\nTelefono: " + telefono + "\nGénero: "+ genero + "\n"
    with open("01092024Datos.txt","a") as archivo:
        archivo.write(datos+"\n\n")
    messagebox.showinfo("Informacion", "Datos guardados con éxito: \n\n"+ datos)
    
def limpiar_campos():
    tbnombre.delete(0,tk.END)
    tbapellidos.delete(0,tk.END)
    tbedad.delete(0,tk.END)
    tbestatura.delete(0,tk.END)
    tbtelefono.delete(0,tk.END)
    var_genero.set(0)

def borrar_fun():
    limpiar_campos()
    
def es_vacio(campo):
    return not campo.strip()

def es_numero(cadena):
    return cadena.isdigit()

def validar_datos():
    nombre = tbnombre.get().strip()
    apellido = tbapellidos.get().strip()
    edad = tbedad.get().strip()
    estatura = tbestatura.get().strip()
    telefono = tbtelefono.get().strip()
    genero = var_genero.get()

    if not nombre or not apellido:
        messagebox.showerror("Error", "Debes ingresar tu nombre y apellido")
        return False

    if not re.fullmatch(r'\d{10}', telefono):
        messagebox.showerror("Error", "El número de teléfono debe ser valido")
        return False

    if not re.fullmatch(r'\d+', edad) or int(edad) <= 0:
        messagebox.showerror("Error", "Debes ingresar una edad.")
        return False

    if not re.fullmatch(r'\d+(\.\d+)?', estatura) or float(estatura) <= 0:
        messagebox.showerror("Error", "Debes ingresar una estatura.")
        return False

    if genero == 0:
        messagebox.showerror("Error", "Debes seleccionar un género.")
        return False

    return True


ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")
var_genero = tk.IntVar()

lbnombre= tk.Label(ventana, text="Nombres: ")
lbnombre.pack()
tbnombre= tk.Entry()
tbnombre.pack()
lbapellidos= tk.Label(ventana, text="Apellidos: ")
lbapellidos.pack()
tbapellidos = tk.Entry()
tbapellidos.pack()
lbtelefono = tk.Label(ventana, text="Telefono: ")
lbtelefono.pack()
tbtelefono = tk.Entry()
tbtelefono.pack()
lbedad= tk.Label(ventana, text="Edad: ")
lbedad.pack()
tbedad= tk.Entry()
tbedad.pack()
lbestatura= tk.Label(ventana, text="Estatura: ")
lbestatura.pack()
tbestatura= tk.Entry()
tbestatura.pack()
lbgenero= tk.Label(ventana, text="Género: ")
lbgenero.pack()
rbhombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbhombre.pack()
rbmujer=tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbmujer.pack()

btnborrar = tk.Button(ventana, text="Borrar valores", command=limpiar_campos)
btnborrar.pack()
btnguardar= tk.Button(ventana, text="Guardar", command=guardar_valores)
btnguardar.pack()
ventana.mainloop()
