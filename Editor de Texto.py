
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


root=Tk()
root.config(width=500, height=600)
root.title("Editor de Texto")
# root.iconbitmap('C:\recursos\icono.ico')

#usada para la ventana emergente de abrir
ruta=""


#Ventanas emergentes
def infoAcercaDe():

	varAcercaDe = messagebox.showinfo("Editor de Texto", "Copyright * 2020 * Version 1.0")

def infoLicencia():

	varLicencia = messagebox.showwarning("Licencia", "Su Licencia tiene validez hasta el 26/07/2025")

def confirmacionSalir():

	varSalir = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")

	if varSalir=="yes":

		root.quit()

#Funciones del menu archivo


def nuevoArchivo():

	mensajeInferiorDerecha.set("Nuevo archivo")
	cajaTexto.delete(1.0, END)
	ruta=""
	root.title("Editor de Texto")


#abrir archivo ventana emergente

def abrirArchivo():

	global ruta

	mensajeInferiorDerecha.set("Abrir archivo")

	ruta = filedialog.askopenfilename(initialdir="C:", filetypes=(("Abrir ficheros de texto","*.txt"),("Todos los ficheros","*.*")),
	 title="Abrir un Fichero")

	if ruta!="":

		fichero = open(ruta, "r")
		contenido = fichero.read()
		cajaTexto.delete(1.0, "end")          #nos aseguramos que este vacio
		cajaTexto.insert("insert", contenido)  #insertamos contenido
		fichero.close()                         #cerramos fichero abierto
		root.title(ruta + " - Editor de Texto")  #cambiamos el titulo a la ventana

def guardarArchivo():

	mensajeInferiorDerecha.set("Guardar archivo")

	global ruta

	if ruta!="":

		contenido = cajaTexto.get(1.0, "end-1c")       #recuperamos el texto
		fichero = open(ruta, "w+")					#creamos el fichero o abrimos
		fichero.write(contenido)					#volcamos el contenido
		fichero.close()
		mensajeInferiorDerecha.set("Fichero guardado correctamente")

	else:

		guardarArchivoComo()

def guardarArchivoComo():

	mensajeInferiorDerecha.set("Guardar archivo como")

	global ruta

	fichero = filedialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")

	ruta = fichero.name

	if fichero is not None:

		contenido = cajaTexto.get(1.0, "end-1c")
		fichero = open(ruta, "w+")
		fichero.write(contenido)
		fichero.close()
		mensajeInferiorDerecha.set("Fichero guardado correctamente")

	else:

		mensajeInferiorDerecha.set("Guardado cancelado")


#COLORES DE FONDO

def colorNegro():

	cajaTexto.config(bg="black")

def colorAzul():

	cajaTexto.config(bg="light blue")

def colorRojo():

	cajaTexto.config(bg="red")

def colorVerde():

	cajaTexto.config(bg="light green")

def colorPredeterminado():

	cajaTexto.config(bg="white")


#COLORES LETRA


def colorBlancoLetra():

	cajaTexto.config(fg="white")

def colorVerdeLetra():

	cajaTexto.config(fg="green")


def colorAzulLetra():

	cajaTexto.config(fg="blue")


def colorRojoLetra():

	cajaTexto.config(fg="red")


def colorPredeterminadoLetra():

	cajaTexto.config(fg="black")


#Tipos de letra

                                     
def tipoLetra1():

	cajaTexto.config(font=("Calibri"))

	mensajeInferiorDatosTipo.set("Letra: Calibri")

def tipoLetra2():

	cajaTexto.config(font=("Arial"))

	mensajeInferiorDatosTipo.set("Letra: Arial")

def tipoLetra3():

	cajaTexto.config(font=("Georgia"))

	mensajeInferiorDatosTipo.set("Letra: Georgia")

def tipoLetra4():

	cajaTexto.config(font=("Consolas"))

	mensajeInferiorDatosTipo.set("Letra: Consolas")


#Tamaños de letra

def tamanoLetra1():

	cajaTexto.config(font=8)

	mensajeInferiorDatos.set("Tamaño: 8")

def tamanoLetra2():

	cajaTexto.config(font=12)

	mensajeInferiorDatos.set("Tamaño: 12")

def tamanoLetra3():

	cajaTexto.config(font=15)

	mensajeInferiorDatos.set("Tamaño: 15")

def tamanoLetra4():

	cajaTexto.config(font=18)

	mensajeInferiorDatos.set("Tamaño: 18")

def tamanoLetra5():

	cajaTexto.config(font=22)

	mensajeInferiorDatos.set("Tamaño: 22")


#MENU
menuBar = Menu(root)

fileMenu=Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Nuevo", command=nuevoArchivo)
fileMenu.add_command(label="Abrir", command=abrirArchivo)
fileMenu.add_command(label="Guardar", command=guardarArchivo)
fileMenu.add_command(label="Guardar como...", command=guardarArchivoComo)
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=confirmacionSalir)

editMenu=Menu(menuBar, tearoff=0)
colorEditMenu=Menu(editMenu, tearoff=0)
colorEditMenu.add_command(label="Negro", command=colorNegro)
colorEditMenu.add_command(label="Azul", command=colorAzul)
colorEditMenu.add_command(label="Rojo", command=colorRojo)
colorEditMenu.add_command(label="Verde", command=colorVerde)
colorEditMenu.add_command(label="Predeterminado", command=colorPredeterminado)

letraEditMenu=Menu(editMenu, tearoff=0)

letraEditMenuTipo=Menu(letraEditMenu, tearoff=0)
letraEditMenuTipo.add_command(label="Calibri", command=tipoLetra1)
letraEditMenuTipo.add_command(label="Arial", command=tipoLetra2)
letraEditMenuTipo.add_command(label="Georgia", command=tipoLetra3)
letraEditMenuTipo.add_command(label="Predeterminado", command=tipoLetra4)

letraEditMenuColor=Menu(letraEditMenu, tearoff=0)
letraEditMenuColor.add_command(label="Blanco", command=colorBlancoLetra)
letraEditMenuColor.add_command(label="Verde", command=colorVerdeLetra)
letraEditMenuColor.add_command(label="Azul", command=colorAzulLetra)
letraEditMenuColor.add_command(label="Rojo", command=colorRojoLetra)
letraEditMenuColor.add_command(label="Predeterminado", command=colorPredeterminadoLetra)

verMenu=Menu(menuBar, tearoff=0)
verMenu.add_command(label="Fecha y Hora")
zoomVerMenu=Menu(verMenu, tearoff=0)

helpMenu=Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Licencia", command=infoLicencia)
helpMenu.add_command(label="Enviar Comentarios")
helpMenu.add_separator()
helpMenu.add_command(label="Acerca de...", command=infoAcercaDe)

editMenu.add_cascade(label="Fondo    ", menu=colorEditMenu)
editMenu.add_cascade(label="Letra", menu=letraEditMenu)
letraEditMenu.add_cascade(label="Color", menu=letraEditMenuColor)
letraEditMenu.add_cascade(label="Tipo", menu=letraEditMenuTipo)

menuBar.add_cascade(label="Archivo", menu=fileMenu)
menuBar.add_cascade(label="Editar", menu=editMenu)
menuBar.add_cascade(label="Ver", menu=verMenu)
menuBar.add_cascade(label="Ayuda", menu=helpMenu)

#Hoja para escribir
cajaTexto = Text(root)
cajaTexto.pack(fill="both", expand=1)
cajaTexto.config(pady=1, padx=1, bd=2, relief="sunken", font=("consolas", 12,))

#Mensaje inferior
mensajeInferior = StringVar()
mensajeInferior.set("Copyright 2020 - Franco Nuñez")

labelInferior = Label(root, textvar=mensajeInferior)
labelInferior.pack(side="left")


#label de tamaño

mensajeInferiorDatos = StringVar()
mensajeInferiorDatos.set("- Tamaño: 12 ")

labelInferiorDatos = Label(root, textvar=mensajeInferiorDatos)
labelInferiorDatos.pack(side="right")

#label de tipo de letra


mensajeInferiorDatosTipo = StringVar()
mensajeInferiorDatosTipo.set("- Letra: Consolas")

labelInferiorDatosTipo = Label(root, textvar=mensajeInferiorDatosTipo)
labelInferiorDatosTipo.pack(side="right")


#mensaje inferior derecha
mensajeInferiorDerecha = StringVar()
mensajeInferiorDerecha.set("")

labelInferiorDerecho=Label(root, textvar=mensajeInferiorDerecha)
labelInferiorDerecho.pack(side="left")


root.config(menu=menuBar)
root.mainloop()

