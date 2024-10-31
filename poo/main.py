import clases
import Animal

book = clases.Book('Titulo Libro', 'Autor Libro', 2009)
print(book.titulo)
print(book.autor)
print(book.year)

calc = clases.Calc(4, 4)
calc.add()
calc.rest()
calc.divide()
calc.multiply()

perro = Animal.Perro
perro.emitir_sonido()

gato = Animal.Gato
gato.emitir_sonido()