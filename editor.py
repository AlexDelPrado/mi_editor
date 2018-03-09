from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = "" # Variable global para almacenar la ruta del fichero

def nuevo():
	global ruta
	mensaje.set("Nuevo Fichero")
	ruta = ""
	texto.delete(1.0, "end")
	root.title("Mi first editor")


def abrir():
	global ruta
	mensaje.set("Abrir Fichero")
	ruta = FileDialog.askopenfilename(initialdir=".",
		filetypes=(("Fichero de texto", "*.txt"),),
		title="Abrir fichero de texto")

	if ruta != "":
		fichero = open(ruta, 'r')
		contenido = fichero.read()
		texto.delete(1.0, "end")
		texto.insert('insert', contenido)
		fichero.close()
		root.title(ruta + "Mi editor")


def guardar():
	mensaje.set("Guardar Fichero")
	if ruta != "":
		contenido = texto.get(1.0, 'end-1c')
		fichero = open(ruta, 'w+')
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Guardado correctamente")
	else:
		guardar_como()


def guardar_como():
	global ruta
	mensaje.set("Guardar Fichero Como")
	fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
	if fichero is not None:
		ruta = fichero.name
		contenido = texto.get(1.0, 'end-1c')
		fichero = open(ruta, 'w+')
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Guardado correctamente")
	else:
		mensaje.set("Guardado Cancelado")
		ruta = ""


# Configuramos la raiz
root = Tk()
root.title("Editor")

# Menu superior
menubar = Menu(root)
root.config(menu=menubar)

# Barra de menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar Como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")
menubar.add_cascade(label="Editar", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=True)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)

# Bucle del sistema
root.mainloop()
