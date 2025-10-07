import random

GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
GRAY_BG = "\033[47m"
RESET = "\033[0m"

def colorear_letra(letra: str, estado: str) -> str :
    """ 
     La función recive una letra y y un estado de la letra y  devuelve la letra coloreada 
    """
    if estado == "verde":
        return f"{GREEN_BG} {letra.upper()} {RESET}"
    elif estado == "amarillo":
        return f"{YELLOW_BG} {letra.upper()} {RESET}"
    else:
        return f"{GRAY_BG} {letra.upper()} {RESET}"

# TODO_____________________

def elegir_palabra(palabras: list[str]) -> str: 
    """
    Selecciona aleatoriamente la palabra del día de la lista de palabras.

    Parámetros:
        palabras (list): lista de palabras en mayúsculas

    Retorna:
        str: palabra seleccionada
    """
    # TODO: implementar selección aleatoria
    pass


def comprobar_intento(palabra_secreta: str, intento: str):
    """
    Compara el intento con la palabra secreta y devuelve una lista indicando
    para cada letra si es:
        - "verde" -> letra correcta y en la posición correcta
        - "amarillo" -> letra presente en otra posición
        - "gris" -> letra no presente

    Parámetros:
        palabra_secreta (str): palabra a adivinar
        intento (str): intento del jugador

    Retorna:
        list[str]: lista de estados por letra
    """
    # TODO: implementar la lógica de comprobación
    pass


def mostrar_feedback(intento, resultado):
    """
    Muestra el intento en la consola con feedback de colores.

    Parámetros:
        intento (str): palabra intentada
        resultado (list[str]): lista con estados por letra ("verde", "amarillo", "gris")

    Ejemplo:
        intento = "CASA"
        resultado = ["amarillo", "gris", "gris", "verde"]
        => se muestra cada letra con el color correspondiente
    """
    # TODO: mostrar las letras con colores (ANSI o emojis)
    pass


def validar_intento(intento, palabras):
    """
    Valida que el intento:
      - tenga 5 letras
      - esté en la lista de palabras cargadas

    Parámetros:
        intento (str): intento del jugador
        palabras (list): lista de palabras válidas

    Retorna:
        bool: True si es válido, False si no
    """
    # TODO: implementar validación
    pass


# Esto solo se ejecuta si ejecutamos esta librería directamente
# pero no si la importamos en otro fichero
if __name__ == "__main__":

  palabra = "carta"
  intento = "casas"

  resultado = []
  for i, letra in enumerate(intento):
      if letra == palabra[i]:
          resultado.append(colorear_letra(letra, "verde"))
      elif letra in palabra:
          resultado.append(colorear_letra(letra, "amarillo"))
      else:
          resultado.append(colorear_letra(letra, "gris"))

  print("".join(resultado))


