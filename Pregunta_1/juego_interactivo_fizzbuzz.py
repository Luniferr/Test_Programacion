"""Código Juego FizzBuzz"""

class JuegoFizzBuzz:
    """Clase para el juego Fizz Buzz"""

    INSTRUCCIONES = """¡Perfecto!, aquí van las instrucciones:
    Se mostrarán números del 1 al 100 en la consola. Si el número es divisible por 3, escriba "fizz";
    si es divisible por 5, escriba "buzz"; y si es divisible por ambos, escriba "fizzbuzz".
    Si no corresponde a ninguno de las anteriores, sólo repita el número impreso.
    Si desea dejar de jugar, escriba "Salir."""

    def ejecutar(self):
        """Ejecuta el juego Fizz Buzz"""
        print("¡Bienvenido!, ¿Estás preparado para jugar FIZZ BUZZ?")
        respuesta = input(": ").lower()

        while respuesta != "salir":
            if respuesta == "si":
                self.jugar()
            elif respuesta == "no":
                print("No hay problema. Intenténtalo nuevamente más tarde. ¡Hasta pronto!")
            else:
                print("Respuesta no válida")

            print("...")
            print("¡Hola nuevamente!, ¿Estás preparado para jugar FIZZ BUZZ?")
            respuesta = input(": ").lower()

        print("Fin del juego")

    def jugar(self):
        """Jugar Fizz Buzz"""
        print(self.INSTRUCCIONES)

        for numero in range(1, 101):
            print(f"El número es: {numero}")

            respuesta_usuario = input("Respuesta: ").lower()

            respuesta_correcta_actual = self.respuesta_correcta(numero)

            if self.es_correcta(respuesta_usuario, numero):
                print("¡Felicitaciones! Sigamos con el siguiente número")
            else:
                print(f"Te has equivocado. La respuesta correcta era: {respuesta_correcta_actual}")

    @staticmethod
    def respuesta_correcta(numero):
        """Respuesta correcta para el número en cuestión"""
        if numero % 3 == 0 and numero % 5 == 0:
            return "fizzbuzz"
        elif numero % 3 == 0:
            return "fizz"
        elif numero % 5 == 0:
            return "buzz"
        else:
            return str(numero)

    @staticmethod
    def es_correcta(respuesta_usuario, numero):
        """Verifica si la respuesta del usuario es correcta"""
        if numero % 3 == 0 and numero % 5 == 0 and respuesta_usuario == "fizzbuzz":
            return True
        elif numero % 3 == 0 and respuesta_usuario == "fizz":
            return True
        elif numero % 5 == 0 and respuesta_usuario == "buzz":
            return True
        elif respuesta_usuario.lower() == "salir":
            return True
        elif respuesta_usuario.isdigit() and int(respuesta_usuario) == numero and respuesta_usuario not in ["fizz", "buzz", "fizzbuzz"]:
            return True
        else:
            return False


if __name__ == "__main__":
    juego = JuegoFizzBuzz()
    juego.ejecutar()
