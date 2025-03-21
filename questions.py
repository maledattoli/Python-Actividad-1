import random
import sys
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#inicio puntaje en 0
puntaje = float(0)
# no se accede a las preguntas con indices
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
for question, answers, correct_one in questions_to_ask:

    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es un numero
        if not user_answer.isdigit():
            print("No es un numero. Por favor ingrese un numero")
            sys.exit(1)
        else:
            user_answer = int(user_answer) - 1
            # Se verifica si la respuesta no es alguna de las respuestas posibles
            if user_answer < 0 or user_answer >= len(answers):
                print("Respuesta no válida")
                sys.exit(1)
            # Se verifica si la respuesta es correcta
            elif user_answer == correct_one:
                print("¡Correcto!")
                #el jugador acertó se le suma su puntaje
                puntaje += 1
                break
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[correct_one])
        # segundo intento fallido por lo tanto resto puntaje
        puntaje -= 0.5

    # Se imprime un blanco al final de la pregunta
    print()
    #imprimo el puntaje del jugador
    print(f"el jugador termino con el puntaje: {puntaje}")

