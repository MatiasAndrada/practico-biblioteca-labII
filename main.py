from libroClass import Libro
from socioClass import Socio


def main():
    libro1 = Libro("Biblia", "Dios", "0-D.C", "Religion", "Regular")
    socio1 = Socio(46234324, "Diego", "Grande", "Veneranda",
                   "DiegoAmarok2024@volsvagen.com", "Vencida")
    print(libro1.autor)
    print(libro1.titulo)
    libro1.setTitulo("Nueva evangelio")
    print(libro1.titulo)
    print(socio1.apellido)


if __name__ == '__main__':
    main()
