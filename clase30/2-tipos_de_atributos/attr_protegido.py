""" 
Públicos: cualquier atributo. -> atributo
Protegidos: un “guión bajo”. -> _atributo
Privados: con “dobles guiones bajo”. -> __atributo
"""



class Vehiculo:
    def __init__(self, marca, color, placa):
        self._marca = marca
        self._color = color
        self._placa = placa
    @property
    def marca(self):
        return self._marca

    @property
    def color(self):
        return self._color

    @property
    def placa(self):
        return self._placa

# Uso
coche = Vehiculo("Ford", "Rojo", "AB123CD")
print(coche.marca)
print(coche.color)
print(coche.placa)



