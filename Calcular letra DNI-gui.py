# -*- coding: utf-8 -*-
# Calcular letra del NIF o NIE español
# Autor: César Campos Sánchez
# Fecha: 12-06-2025
# Este programa calcula la letra del NIF o NIE español y la copia al portapapeles.

import pyperclip
import tkinter as tk

class Dni():
    def __init__(self, master):
        self.Letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
        self.master = master
        master.title("Calculadora de letra NIF/NIE")
        self.frame_contenedor = tk.Frame(master)
        self.frame_contenedor.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.frame_calculadora = tk.Frame(self.frame_contenedor)
        self.frame_calculadora.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Etiqueta de bienvenida
        self.label_bienvenida = tk.Label(self.frame_calculadora, text="Calculadora de letra NIF/NIE", font=("Arial", 16))
        self.label_bienvenida.pack(pady=10)
        # Entrada para el número del NIF/NIE
        self.entry_numero = tk.Entry(self.frame_calculadora, font=("Arial", 14), justify=tk.CENTER)
        self.entry_numero.pack(pady=5)
        self.entry_numero.bind("<Return>", lambda event: self.calcular_letra_dni_nie())  # Permitir calcular con Enter
        # Botón para calcular la letra
        self.boton_calcular = tk.Button(self.frame_calculadora, text="Calcular Letra", command=self.calcular_letra_dni_nie)
        self.boton_calcular.pack(pady=5)
        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(self.frame_calculadora, text="", font=("Arial", 12))
        self.label_resultado.pack(pady=10)
        # Botón para salir
        self.boton_salir = tk.Button(self.frame_calculadora, text="Salir", command=master.quit)
        self.boton_salir.pack(pady=10)
        
        self.entry_numero.focus_set()  # Foco inicial en la entrada de texto

    def calcular_letra_dni_nie(self):
        numero = self.entry_numero.get().strip().upper()
        if not numero:
            self.label_resultado.config(text="Introduce el número del NIF o NIE.")
            return

        # NIF: 8 dígitos
        if numero.isdigit() and len(numero) == 8:
            try:
                numeroint = int(numero)
                resto = numeroint % 23
                letra = self.Letras[resto]
                resultado = f"{numero}{letra}"
                pyperclip.copy(resultado)
                self.label_resultado.config(text=f"NIF completo:\n\n{resultado}\n\n(Pégalo donde quieras con Ctrl+V)")
                # Limpiar la entrada después de calcular
                self.entry_numero.delete(0, tk.END)
            except Exception:
                self.label_resultado.config(text="Error al calcular la letra del NIF.")
            return

        # NIE: Letra inicial (X, Y, Z) + 7 dígitos
        if len(numero) == 8 and numero[0] in "XYZ" and numero[1:].isdigit():
            letra_inicio = numero[0]
            digitos = numero[1:]
            if letra_inicio == "X":
                nie_num = "0" + digitos
            elif letra_inicio == "Y":
                nie_num = "1" + digitos
            elif letra_inicio == "Z":
                nie_num = "2" + digitos
            else:
                self.label_resultado.config(text="Letra inicial de NIE no válida.")
                return
            try:
                numeroint = int(nie_num)
                resto = numeroint % 23
                letra = self.Letras[resto]
                resultado = f"{numero}{letra}"
                pyperclip.copy(resultado)
                self.label_resultado.config(text=f"NIE completo:\n\n{resultado}\n\n(Copiado al portapapeles)")
                self.entry_numero.delete(0, tk.END)
            except Exception:
                self.label_resultado.config(text="Error al calcular la letra del NIE.")
            return

        self.label_resultado.config(text="Formato no válido. NIF: 8 dígitos. \n NIE: X/Y/Z seguido de 7 dígitos.")

# Centrar la ventana principal
        self.master.update_idletasks()
        ancho = self.master.winfo_width()
        alto = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.master.winfo_screenheight() // 2) - (alto // 2)
        self.master.geometry(f"+{x}+{y}")
        self.master.minsize(300, 200)

if __name__ == "__main__":
    root = tk.Tk()
    app = Dni(root)
    # Centrar la ventana principal
    root.update_idletasks()
    ancho = root.winfo_width()
    alto = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (ancho // 2)
    y = (root.winfo_screenheight() // 2) - (alto // 2)
    root.geometry(f"+{x}+{y}")
    root.minsize(300, 200)
    root.mainloop()
