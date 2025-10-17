# 1) definir una clase abstracta vehiculo con atributos marca, modelo, año y un métodos abstracto
from abc import ABC, abstractmethod 

class Vehiculo(ABC): # Clase abstracta
    def __init__(self, marca, modelo, año): # Constructor
        self.marca = marca # atributo público
        self.modelo = modelo # atributo público
        self.año = año # atributo público
        self.__kilometraje = 0  # atributo privado (encapsulado)

    @abstractmethod
    def descripcion(self):
        pass 

    @abstractmethod
    def calcular_costo_mantenimiento(self):
        pass

    # 3) encapsular el atributo kilometraje de cada vehiculo
    # crear metodos get_kilometraje y set_kilometraje
    # que validen que el kilometraje no sea negativo
    def get_kilometraje(self): # Getter
        return self.__kilometraje

    def set_kilometraje(self, kilometraje): # Setter  
        if kilometraje >= 0:
            self.__kilometraje = kilometraje 
        else:
            print("El kilometraje no puede ser negativo")

# 2) crear clase auto, moto y camion que hereden de vehiculo 
# cada clase debe implementar su propia version del método calcular_costo_mantenimiento
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def descripcion(self):
        return f"Auto: {self.marca} {self.modelo} {self.año}, Puertas: {self.puertas}"

    def calcular_costo_mantenimiento(self):
        return 300 + (2024 - self.año) * 20


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo

    def descripcion(self):
        return f"Moto: {self.marca} {self.modelo} {self.año}, Tipo: {self.tipo}"

    def calcular_costo_mantenimiento(self):
        return 150 + (2024 - self.año) * 15


class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad):
        super().__init__(marca, modelo, año)
        self.capacidad = capacidad

    def descripcion(self):
        return f"Camion: {self.marca} {self.modelo} {self.año}, Capacidad: {self.capacidad} toneladas"

    def calcular_costo_mantenimiento(self):
        return 500 + (2024 - self.año) * 30


# 4) proggramar un ejemplo donde se creen diferentes vehiculos, se alamacenen en una lista
# y se muestre el costo de mantenimiento de cada uno
if __name__ == "__main__":
    auto1 = Auto("Toyota", "Corolla", 2020, 4)
    moto1 = Moto("Honda", "CBR500R", 2019, "Deportiva")
    camion1 = Camion("Volvo", "FH16", 2018, 20)

    auto1.set_kilometraje(15000)
    moto1.set_kilometraje(8000)
    camion1.set_kilometraje(50000)

    vehiculos = [auto1, moto1, camion1]

    for v in vehiculos: # recorrer la lista de vehiculos
        print(v.descripcion())
        print(f"Kilometraje: {v.get_kilometraje()} km")
        print(f"Costo de mantenimiento: ${v.calcular_costo_mantenimiento()}\n")

