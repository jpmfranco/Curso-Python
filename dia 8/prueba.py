from cambia_texto import todo_mayusculas
import unittest


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = todo_mayusculas(palabra)
        self.assertEqual(resultado, "Buen Dia")


if __name__ == '__main__':
    unittest.main()