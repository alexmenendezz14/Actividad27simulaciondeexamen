class Curso:
    def __init__(self, id, nombre, creditos, añosdeestudio):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.añosdeestudio = añosdeestudio

    def mostrar_ficha(self):
        print(f"Ficha del Curso:\nID: {self.id}\nNombre: {self.nombre}\nCréditos: {self.creditos}\nAños de Estudio: {self.añosdeestudio}\n")


class Alumno:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def mostrar_ficha(self):
        print(f"Ficha del Alumno:\nID: {self.id}\nNombre: {self.nombre}\nEmail: {self.email}\n")


class Matricula:
    def __init__(self, idmatricula, fechamatricula, idalumno, idcurso):
        self.idmatricula = idmatricula
        self.fechamatricula = fechamatricula
        self.idalumno = idalumno
        self.idcurso = idcurso

    def mostrar_datos(self):
        print(f"Datos de Matrícula:\nID Matrícula: {self.idmatricula}\nFecha Matrícula: {self.fechamatricula}\nID Alumno: {self.idalumno}\nID Curso: {self.idcurso}\n")


class CentroEducativo:
    def __init__(self):
        self.matriculas = []

    def realizar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def mostrar_matriculas(self):
        print("Matrículas realizadas en el centro:")
        for matricula in self.matriculas:
            matricula.mostrar_datos()


# Ejemplo de uso:
curso1 = Curso(1, "Matemáticas", 4, 2)
curso2 = Curso(2, "Historia", 3, 1)

alumno1 = Alumno(101, "Juan Pérez", "juan@example.com")
alumno2 = Alumno(102, "María Gómez", "maria@example.com")

matricula1 = Matricula(1, "2023-01-15", alumno1.id, curso1.id)
matricula2 = Matricula(2, "2023-01-20", alumno2.id, curso1.id)
matricula3 = Matricula(3, "2023-01-25", alumno2.id, curso2.id)

centro_educativo = CentroEducativo()
centro_educativo.realizar_matricula(matricula1)
centro_educativo.realizar_matricula(matricula2)
centro_educativo.realizar_matricula(matricula3)

curso1.mostrar_ficha()
alumno1.mostrar_ficha()
alumno1.mostrar_ficha()

centro_educativo.mostrar_matriculas()
