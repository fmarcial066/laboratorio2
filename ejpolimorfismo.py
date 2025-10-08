class Gato(Animal):
    def hablar(self):
        return "Miau!"

animales = [Perro("Firulais"), Gato("Michi"), Animal("Desconocido")]

for a in animales:
    print(f"{a.nombre}: {a.hacer_sonido()}") 