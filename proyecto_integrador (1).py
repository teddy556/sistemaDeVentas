import tkinter as tk
from tkinter import ttk


class SistemaDeVenta:
    def __init__(self):
        self.sistema_de_venta = tk.Tk()
        self.sistema_de_venta.title("SISTEMA DE VENTA")

        # Variables
        self.productos = self.lista_productos()

        # Crear ventana principal
        self.crear_interfaz()

    def lista_productos(self):
        productos = [
            {"codigo": "001", "nombre": "pan", "precio": 10.99},
            {"codigo": "002", "nombre": "coca cola", "precio": 5.99},
            {"codigo": "003", "nombre": "inca cola", "precio": 15.99},
            {"codigo": "004", "nombre": "fideos", "precio": 8.99},
            {"codigo": "005", "nombre": "tari", "precio": 12.99},
            {"codigo": "006", "nombre": "tampico", "precio": 10.99},
            {"codigo": "007", "nombre": "arros", "precio": 5.99},
            {"codigo": "008", "nombre": "huevo", "precio": 15.99},
            {"codigo": "009", "nombre": "papitas lays", "precio": 8.99},
            {"codigo": "010", "nombre": "pepsi", "precio": 12.99},
            {"codigo": "011", "nombre": "generade", "precio": 10.99},
            {"codigo": "012", "nombre": "cachito", "precio": 5.99},
            {"codigo": "013", "nombre": "leche", "precio": 15.99},
            {"codigo": "014", "nombre": "cereal", "precio": 8.99},
            {"codigo": "015", "nombre": "agua", "precio": 12.99},
            {"codigo": "016", "nombre": "agua cielo", "precio": 10.99},
            {"codigo": "017", "nombre": "agua san mateo", "precio": 5.99},
            {"codigo": "018", "nombre": "agua oro", "precio": 15.99},
            {"codigo": "019", "nombre": "fanta", "precio": 8.99},
            {"codigo": "020", "nombre": "chicle", "precio": 12.99}
        ]
        return productos

    def crear_interfaz(self):
        self.tabla_lista = ttk.Treeview(self.sistema_de_venta, columns=("codigo", "nombre", "precio"))
        self.tabla_lista.grid(row=0, column=0, columnspan=3)
        self.tabla_lista.column("#0", width=0)
        self.tabla_lista.heading("codigo", text="Código")
        self.tabla_lista.heading("nombre", text="Nombre")
        self.tabla_lista.heading("precio", text="Precio")
        self.cargar_productos()

        # Texto de los productos
        tk.Label(text="Nombre:", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=8, pady=5)
        tk.Label(text="Precio:", font=("Arial", 12, "bold")).grid(row=2, column=1, padx=8, pady=5)
        tk.Label(text="Codigo:", font=("Arial", 12, "bold")).grid(row=2, column=2, padx=8, pady=5)

        # Entrada de texto
        self.entry_nombre = tk.Entry()
        self.entry_nombre.config(font="Arial")
        self.entry_nombre.grid(row=1, column=0, padx=8, pady=5)

        self.entry_precio = tk.Entry()
        self.entry_precio.config(font="Arial")
        self.entry_precio.grid(row=1, column=1, padx=8, pady=5)

        self.entry_codigo = tk.Entry()
        self.entry_codigo.config(font=("Arial"))
        self.entry_codigo.grid(row=1, column=2, padx=8, pady=5)

        # Botones de agregar, editar y eliminar
        tk.Button(text="Agregar", width=20, font=("Arial", 8, "bold"), fg="#FFFFFF", bg="#DC143C",
                  command=self.agregar_producto).grid(row=4, column=0, padx=10, pady=5)
        tk.Button(text="Editar", width=20, font=("Arial", 8, "bold"), fg="#FFFFFF", bg="#DC143C",
                  command=self.editar_producto).grid(row=4, column=1, padx=10, pady=5)
        tk.Button(text="Eliminar", width=20, font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#DC143C",
                  command=self.eliminar_producto).grid(row=4, column=2, padx=8, pady=5)

        # Texto de la lista de productos en el carrito
        tk.Label(text="LISTA DE PRODUCTOS EN CARRITO", font=("Arial", 10)).grid(row=5, column=1)

        # Lista de productos en el carrito
        self.tabla_carro = ttk.Treeview(columns=("codigo", "nombre", "precio"))
        self.tabla_carro.grid(row=6, column=0, columnspan=3)
        self.tabla_carro.column("#0", width=0)
        self.tabla_carro.heading("codigo", text="Código")
        self.tabla_carro.heading("nombre", text="Nombre")
        self.tabla_carro.heading("precio", text="Precio")

        # Texto para el total
        tk.Label(text="TOTAL", font=("Arial", 10, "bold")).grid(row=7, column=1, pady=5, columnspan=2)

        # Entry para el total
        self.entry_total = tk.Entry()
        self.entry_total.config(font=("Arial"))
        self.entry_total.grid(row=7, column=2)

        # Entry para el código del producto a agregar al carrito
        self.entry_codigo_para_agregar_a_carrito = tk.Entry(width=15)
        self.entry_codigo_para_agregar_a_carrito.config(font=("Arial"))
        self.entry_codigo_para_agregar_a_carrito.grid(row=7, column=1)

        # Botones de agregar al carrito, nueva compra y venta
        tk.Button(text="AGREGAR AL CARRITO", width=20, font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#DC143C",
                  command=self.agregar_al_carrito).grid(row=7, column=0, pady=5)
        tk.Button(text="NUEVA COMPRA", width=20, font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#DC143C",
                  command=self.nueva_compra).grid(row=8, column=0, pady=5)
        tk.Button(text="VENTA", width=20, font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#DC143C",
                  command=self.realizar_venta).grid(row=8, column=2, pady=5)

    def cargar_productos(self):
        # Limpiar tabla de productos
        for item in self.tabla_lista.get_children():
            self.tabla_lista.delete(item)

        # Insertar los productos en la tabla
        for producto in self.productos:
            codigo = producto["codigo"]
            nombre = producto["nombre"]
            precio = producto["precio"]
            self.tabla_lista.insert("", tk.END, values=(codigo, nombre, precio))

    def agregar_producto(self):
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        codigo = self.entry_codigo.get()

        # Validar campos no vacíos
        if nombre and precio and codigo:
            nuevo_producto = {"codigo": codigo, "nombre": nombre, "precio": precio}
            self.productos.append(nuevo_producto)
            self.cargar_productos()
            self.limpiar_campos()

    def editar_producto(self):
        # Obtener el producto seleccionado
        item = self.tabla_lista.focus()
        if item:
            nombre = self.entry_nombre.get()
            precio = self.entry_precio.get()
            codigo = self.entry_codigo.get()

            # Validar campos no vacíos
            if nombre and precio and codigo:
                nuevo_producto = {"codigo": codigo, "nombre": nombre, "precio": precio}

                # Actualizar el producto en la lista
                index = self.tabla_lista.index(item)
                self.productos[index] = nuevo_producto

                self.cargar_productos()
                self.limpiar_campos()

    def eliminar_producto(self):
        # Obtener el producto seleccionado
        item = self.tabla_lista.focus()
        if item:
            # Eliminar el producto de la lista
            index = self.tabla_lista.index(item)
            del self.productos[index]

            self.cargar_productos()
            self.limpiar_campos()

    def agregar_al_carrito(self):
        codigo = self.entry_codigo_para_agregar_a_carrito.get()

        # Buscar el producto en la lista de productos
        producto = next((p for p in self.productos if p["codigo"] == codigo), None)
        if producto:
            # Insertar el producto en la tabla del carrito
            codigo = producto["codigo"]
            nombre = producto["nombre"]
            precio = producto["precio"]
            self.tabla_carro.insert("", tk.END, values=(codigo, nombre, precio))
            self.calcular_total()

    def calcular_total(self):
        total = 0
        # Obtener los precios de los productos en el carrito
        for item in self.tabla_carro.get_children():
            precio = float(self.tabla_carro.item(item)["values"][2])
            total += precio

        self.entry_total.delete(0, tk.END)
        self.entry_total.insert(tk.END, total)

    def nueva_compra(self):
        # Limpiar tabla del carrito y el campo del total
        for item in self.tabla_carro.get_children():
            self.tabla_carro.delete(item)
        self.entry_total.delete(0, tk.END)

    def realizar_venta(self):
        # Realizar las acciones necesarias para finalizar la venta
        self.nueva_compra()
        # Agregar aquí el código para guardar los datos de la venta, imprimir ticket, etc.

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_codigo.delete(0, tk.END)

    def iniciar_sistema(self):
        self.sistema_de_venta.mainloop()


# Crear instancia del sistema de venta y ejecutarlo
sistema_venta = SistemaDeVenta()
sistema_venta.iniciar_sistema()
