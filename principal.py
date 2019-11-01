from tkinter import *
from tkinter import ttk
import alumnos

class App():


    def __init__(self):

        self.root=Tk()
        self.root.title('AMB Alumnos')



        self.nya=StringVar()
        self.dni=StringVar()
        self.materia=StringVar()
        self.nota=IntVar()
        self.calif=StringVar()

        self.nyaLabel= ttk.Label(self.root, text='Nombre y Apellido')
        self.nyaEntry= ttk.Entry(self.root, textvariable=self.nya, width=5)
        self.dniLabel= ttk.Label(self.root, text='DNI')
        self.dniEntry= ttk.Entry(self.root, textvariable=self.dni, width=5)
        self.materiaLabel= ttk.Label(self.root, text='Materia')
        self.materiaEntry= ttk.Entry(self.root, textvariable=self.materia, width=1)
        self.notaLabel= ttk.Label(self.root, text='Nota')
        self.notaEntry= ttk.Entry(self.root, textvariable=self.nota)
        self.califLabel= ttk.Label(self.root, text='Calificacion')
        self.califAutoLabel= ttk.Label(self.root, textvariable=self.calif)
        self.addButton= ttk.Button(self.root, text='Agregar', command=self.addAlumno)
        self.deleteButton= ttk.Button(self.root, text='Eliminar', command=self.deleteAlumno)
        self.saveButton= ttk.Button(self.root , text='Guardar' , command=self.saveList)
        self.openButton= ttk.Button(self.root , text='Abrir' , command=self.openList)
        self.scrollbar= ttk.Scrollbar(self.root, orient=VERTICAL)
        self.listBox= Listbox(self.root, yscrollcommand=self.scrollbar.set)

        self.addButton.pack(side=TOP , fill=BOTH , expand=False , padx=10 , pady=10 )
        self.deleteButton.pack(side=TOP , fill=BOTH , expand=False , padx=10 , pady=10 )
        self.saveButton.pack(side=TOP , fill=BOTH , expand=False , padx=10 , pady=10 )
        self.openButton.pack(side=TOP , fill=BOTH , expand=False , padx=10 , pady=10 )
        self.nyaLabel.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10 )
        self.nyaEntry.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10)

        self.dniLabel.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10)
        self.dniEntry.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10)
        self.materiaLabel.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10)
        self.materiaEntry.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10 )
        self.notaLabel.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10 )
        self.notaEntry.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10 )
        self.califLabel.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10 )
        self.califAutoLabel.pack(side=TOP , fill=BOTH , expand=True , padx=10 , pady=10)


        self.listBox.pack(side=RIGHT , fill=BOTH , expand=True , padx=10 , pady=10)
        #self.scrollbar.pack(side=LEFT , fill=BOTH , expand=True , padx=10 , pady=10)

        self.root.mainloop()

    def addAlumno(self):
        error_dato = False
        try:
            nya=self.nya.get()
            dni=self.dni.get()
            materia=self.materia.get()
            nota=int(self.nota.get())
            calif=''
        except:
            error_dato=True
        if not error_dato:
            unAlumno= alumnos.Alumnos(nya, dni, materia, nota, calif)
            if nota <=5:
                unAlumno.setCalif('Insuficiente')
                self.calif.set('Insuficiente')
            elif nota == 6:
                unAlumno.setCalif('Regular')
                self.calif.set('Regular')
            elif (nota > 6) and (nota <=8):
                unAlumno.setCalif('Bien')
                self.calif.set('Bien')
            elif nota == 9:
                unAlumno.setCalif('Muy Bien')
                self.calif.set('Muy Bien')
            elif nota == 10:
                unAlumno.setCalif('Excelente')
                self.calif.set('Excelente')

            self.listBox.insert(END, unAlumno.toString())

    def deleteAlumno(self):
        print(self.listBox.curselection()[0])
        self.listBox.delete(self.listBox.curselection()[0])

    def saveList(self):
        #print(self.listBox.get(0))
        with open('C:/Users/tiona/Desktop/Lista Alumnos.txt', 'w') as file:
            for i in range(self.listBox.size()):
                file.write('%s \n' %self.listBox.get(i))

    def openList(self):{}

def applic():
    ap=App()
    return 0

applic()
