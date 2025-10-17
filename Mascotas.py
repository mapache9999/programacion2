from abc import ABC, abstractmethod # Importar ABC y abstractmethod para crear clases abstractas

# Clase abstracta (ABSTRACCIÓN)
class Mascota(ABC): # Clase padre. Para nombrar la clase usamos pascal case.
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre            # atributo público
        self.edad = edad                # atributo público
        self.raza = raza                # atributo público
        self.__historial_medico = []    # atributo privado. Usamos doble guion bajo para indicar que es privado.

    @abstractmethod # Método abstracto
    def emitir_sonido(self): 
        pass # No tiene implementación en la clase base.

    # Métodos para acceder al historial (ENCAPSULACIÓN)
    def agregar_historial(self, registro):
        self.__historial_medico.append(registro)

    def mostrar_historial(self): # Método para mostrar el historial médico
        if not self.__historial_medico: # Si el historial está vacío
            print(f"{self.nombre} no tiene historial médico.") # Mensaje si no hay historial
        else: # Si hay historial, mostrarlo
            print(f"Historial médico de {self.nombre}:") # Mostrar el historial
            for item in self.__historial_medico: # Recorrer el historial
             print(f" - {item}") # Mostrar cada registro del historial


# Clases hijas (HERENCIA y POLIMORFISMO)
class Perro(Mascota): # Clase hija de Mascota
    def emitir_sonido(self): # Implementación del método abstracto
        return f"{self.nombre} dice: ¡Guau guau!"

class Gato(Mascota):
    def emitir_sonido(self): # Implementación del método abstracto
        return f"{self.nombre} dice: ¡Miau!"

class Ave(Mascota): # Clase hija de Mascota
    def emitir_sonido(self): # Implementación del método abstracto
        return f"{self.nombre} dice: ¡Pío pío!"


# Programa principal
if __name__ == "__main__": # Crear instancias de mascotas
    perro = Perro("Toby", 4, "Labrador") # Instancia de Perro
    gato = Gato("Luna", 5, "Siamesa") # Instancia de Gato
    ave = Ave("Piolin", 2, "Canario") # Instancia de Ave

    # Historial médico 
    perro.agregar_historial("Vacunación completa")
    gato.agregar_historial("Desparasitado en septiembre")
    ave.agregar_historial("Control de plumas realizado")

    # Mostrar la información
    mascotas = [perro, gato, ave] # lista de mascotas

    for m in mascotas: # recorrer la lista de mascotas
        print(f"\nMascota: {m.nombre}, {m.raza}, {m.edad} años")
        print(m.emitir_sonido())  # POLIMORFISMO: mismo método, distinto comportamiento
        m.mostrar_historial() # Mostrar el historial médico
