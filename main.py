class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        signo = '+' if self.imaginario >= 0 else ''
        return f"{self.real} {signo} {self.imaginario}i"

    def suma(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(real, imaginario)

    def resta(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(real, imaginario)

    def multiplicacion(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def division(self, otro):
        divisor = otro.real ** 2 + otro.imaginario ** 2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
        return NumeroComplejo(real, imaginario)

# Ejemplo de uso
a = NumeroComplejo(3, 2)
b = NumeroComplejo(1, 7)

print("Suma:", a.suma(b))
print("Resta:", a.resta(b))
print("Multiplicación:", a.multiplicacion(b))
print("División:", a.division(b))
