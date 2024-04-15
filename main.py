from libroClass import Libro
from socioClass import Socio


def main():
    # Creación de objetos a partir de la clase Libro y Socios
    libro1 = Libro("Aprendiendo Programación I", "Profe Alex",
                   "2017", "Educativo", "Regular")
    libro2 = Libro("Aprendiendo Programación II", "Profe Alex",
                   "2018", "Educativo", "Regular")

    socio1 = Socio(46234324, "Diego", "Grande", "Veneranda",
                   "DiegoAmarok2024@volsvagen.com", "Vencida")

# Método de acceso al atributo
    print(libro1.autor)

    libro1.__str__()

    print(socio1.apellido)


if __name__ == '__main__':
    main()
