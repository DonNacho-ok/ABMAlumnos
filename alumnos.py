class Alumnos():

    def __init__(self, name, dni, materia, nota, calificacion):
        self.__Name=name
        self.__DNI=dni
        self.__Materia=materia
        self.__Nota=nota
        self.__Calif=calificacion

    def setName(self, name):
        self.__Name=name

    def setDNI(self, dni):
        self.__DNI=dni

    def setNota(self, nota):
        self.__Nota=nota

    def setMateria(self, mate):
        self.__Materia=mate

    def setCalif(self, calif):
        self.__Calif=calif

    def getName(self):
        return self.__Name

    def getDNI(self):
        return self.__DNI

    def getMateria(self):
        return self.__Materia

    def getNota(self):
        return self.__Nota

    def getCalif(self):
        return self.__Calif

    def toString(self):
        return "Alumno: {}, DNI: {}, Materia: {}, Nota: {}, Calificacion: {}".format(self.__Name, self.__DNI, self.__Materia, self.__Nota, self.__Calif)
