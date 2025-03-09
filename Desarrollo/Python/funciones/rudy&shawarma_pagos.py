import tkinter as tk
from tkinter import messagebox

# Datos globales
usuarios_oficina = ["Alvaro", "Esteban", "Enrique", "Facu P", "Facu B",
                    "Silvina", "Sofia", "Victoria", "Ana", "Laura", "Sebastian",
                    "Guillermo"]

lista_productos = []
lista_precios = []
productos_a_pagar = []
total_pagos = []
usuario_actual = ""

def iniciar_sesion():
    global usuario_actual
    usuario_actual = entry_usuario.get()
    if usuario_actual in usuarios_oficina:
        label_usuario.config(text=f"Usuario: {usuario_actual}")
        entry_usuario.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Usuario no registrado")

def agregar_producto():
    producto = entry_producto.get()
    precio = entry_precio.get()

    if not producto or not precio:
        messagebox.showwarning("Advertencia", "Debe ingresar producto y precio.")
        return

    try:
        precio = float(precio)
        lista_productos.append(producto)
        lista_precios.append((producto, precio))
        listbox_productos.insert(tk.END, producto)
        entry_producto.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un precio válido.")

def seleccionar_producto():
    if not usuario_actual:
        messagebox.showwarning("Advertencia", "Debe iniciar sesión primero.")
        return

    seleccion = listbox_productos.curselection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Debe seleccionar un producto.")
        return

    producto = listbox_productos.get(seleccion[0])
    productos_a_pagar.append((usuario_actual, producto))
    listbox_seleccion.insert(tk.END, f"{usuario_actual} - {producto}")

def calcular_total():
    if not usuario_actual:
        messagebox.showwarning("Advertencia", "Debe iniciar sesión primero.")
        return

    total = sum(precio for prod, precio in lista_precios if any(p[1] == prod and p[0] == usuario_actual for p in productos_a_pagar))
    total_pagos.append((usuario_actual, total))
    label_total.config(text=f"Total a pagar: ${total:.2f}")

def aplicar_descuento():
    descuento = scale_descuento.get()
    total_descuento = sum(pago for usuario, pago in total_pagos if usuario == usuario_actual) * (1 - descuento / 100)
    label_total.config(text=f"Total con descuento: ${total_descuento:.2f}")

# Configuración de la ventana
root = tk.Tk()
root.title("Gestión de Compras")
root.geometry("500x500")

# Ingreso de usuario
tk.Label(root, text="Ingrese su nombre:").pack()
entry_usuario = tk.Entry(root)
entry_usuario.pack()
tk.Button(root, text="Iniciar sesión", command=iniciar_sesion).pack()
label_usuario = tk.Label(root, text="Usuario: Ninguno", font=("Arial", 12, "bold"))
label_usuario.pack()

# Ingreso de productos
tk.Label(root, text="Producto:").pack()
entry_producto = tk.Entry(root)
entry_producto.pack()
tk.Label(root, text="Precio:").pack()
entry_precio = tk.Entry(root)
entry_precio.pack()
tk.Button(root, text="Agregar Producto", command=agregar_producto).pack()

# Lista de productos
tk.Label(root, text="Lista de productos:").pack()
listbox_productos = tk.Listbox(root, height=5)
listbox_productos.pack()
tk.Button(root, text="Seleccionar Producto", command=seleccionar_producto).pack()

# Lista de productos seleccionados
tk.Label(root, text="Productos seleccionados:").pack()
listbox_seleccion = tk.Listbox(root, height=5)
listbox_seleccion.pack()
tk.Button(root, text="Calcular Total", command=calcular_total).pack()

# Total y Descuento
label_total = tk.Label(root, text="Total a pagar: $0.00", font=("Arial", 12, "bold"))
label_total.pack()
tk.Label(root, text="Descuento %:").pack()
scale_descuento = tk.Scale(root, from_=0, to=50, orient="horizontal")
scale_descuento.pack()
tk.Button(root, text="Aplicar Descuento", command=aplicar_descuento).pack()

# Ejecutar la interfaz
root.mainloop()
