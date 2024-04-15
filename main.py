from libroClass import Libro
from socioClass import Socio


def main():
    libro1 = Libro("Aprendiendo Programacion I", "Profe Alex",
                   "2017", "Educativo", "Regular")
    libro2 = Libro("Aprendiendo Programacion II", "Profe Alex",
                   "2018", "Educativo", "Regular")

    socio1 = Socio(46234324, "Diego", "Grande", "Veneranda",
                   "DiegoAmarok2024@volsvagen.com", "Vencida")

    print(libro1.autor)
    libro1.__str__()

    print(socio1.apellido)


if __name__ == '__main__':
    main()
