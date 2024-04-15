class Libro:
    def __init__(self, titulo, autor, fecha, genero, estado):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.genero = genero
        self.estado = estado

    def getLibro(self):
        return self

    def getTitulo(self):
        return self.Titulo

    def getAutor(self):
        return self.Autor

    def getFecha(self):
        return self.fecha

    def getGenero(self):
        return self.genero

    def getEstado(self):
        return self.estado

    def setTitulo(self, titulo):
        if type(titulo) == str:
            self.titulo = titulo
        else:
            print("ERROR")
