"""Código Impresión Números del 1 al 100 considerando función FizzBuzz"""

class FizzBuzz:
    """Clase representativa de FizzBuzz"""

    def __init__(self):
        self.numero_maximo = 100

    def ejecutar(self):
        """Ejecutar Fizz Buzz."""
        for numero in range(1, self.numero_maximo + 1):
            respuesta = self.obtener_respuesta(numero)
            print(respuesta)

    def obtener_respuesta(self, numero):
        """Respuesta correcta para número correspondiente"""
        respuesta = ""
        if numero % 15 == 0:
            respuesta = "FizzBuzz"
        elif numero % 3 == 0:
            respuesta = "Fizz"
        elif numero % 5 == 0:
            respuesta = "Buzz"
        else:
            respuesta = str(numero)
        return respuesta


if __name__ == "__main__":
    juego = FizzBuzz()
    juego.ejecutar()
