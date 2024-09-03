class Calificacion:
    def __init__(self, nota: float):
        self.nota = nota
        self.literal = ""

    def convertir_a_literal(self):
        if 90 <= self.nota <= 100:
            self.literal = "A"
        elif 80 <= self.nota < 90:
            self.literal = "B"
        elif 70 <= self.nota < 80:
            self.literal = "C"
        elif 60 <= self.nota < 70:
            self.literal = "D"
        elif 0 <= self.nota < 60:
            self.literal = "F"
        else:
            self.literal = "Nota inválida"

    def mostrar_calificacion(self):
        print(f"Calificación numérica: {self.nota}")
        print(f"Calificación literal: {self.literal}")


if __name__ == "__main__":
    # Ejemplo de uso
    nota = float(input("Ingrese la calificación numérica: "))

    calificacion = Calificacion(nota)
    calificacion.convertir_a_literal()
    calificacion.mostrar_calificacion()