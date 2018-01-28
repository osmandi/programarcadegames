'''
Estas son las características que debe tener tu cuestionario:

Créalo con cinco o más preguntas. Puedes preguntar cosas que requieran:
    un número como respuesta (por ejemplo; ¿Cuánto es 1+1?)
    texto (Por ejemplo; ¿Cuál es el apellido de Harry Potter?)
    una selección (¿Cuál de estas opciones son las correctas A, B, o C?)
Si permites que el usuario introduzca respuestas no numéricas, piensa y cubre
las distintas formas en que podría contestar.
Por ejemplo, si la respuesta es “a”, sería aceptable también “A”? Échale un
vistazo a la Sección 3.6 para que refresques
cómo conseguir esto.
Debes permitir que el usuario sepa que ha acertado con la respuesta correcta.
Imprime un mensaje basado en esa respuesta.
Debes llevar la cuenta del número de respuestas acertadas.
Al final del programa, deberás mostrar el porcentaje de respuestas contestadas
correctamente por el usuario.
'''

resp_correctas = 0
preg_totales = 0
print ("¡A jugar!")
print ("")

#Primera pregunta

pregunta_1 = float(input("¿Cuánto es 5x5? \n Resp. "))
preg_totales = preg_totales + 1
if pregunta_1 == 25:
    resp_correctas = resp_correctas +1
    print("¡Es correcto!")
else:
    print ("Eso es incorrecto")

print ("")

#Segunda pregunta

pregunta_2 = input("¿Cómo se llama la hija de Maléfica? \n Resp. ")
preg_totales = preg_totales + 1
if pregunta_2.lower() == "mal":
    resp_correctas = resp_correctas +  1
    print("¡Es correcto!")
else:
    print ("Eso es incorrecto")
print ("")

#Tercera pregunta

pregunta_3 = float(input("¿Cuántos libros componen la saga de Harry Potter? \n 1 \n 2 \n 5 \n 7 \n 8 \nResp. "))
preg_totales = preg_totales + 1
if pregunta_3 == 7:
    resp_correctas = resp_correctas +  1
    print("¡Es correcto!")
else:
    print ("Eso es incorrecto")
print ("")

#Cuarta pregunta
pregunta_4 = input("¿Las personas negras le cambian el color de pelo cuando envejecen? \nResp. ")
preg_totales = preg_totales + 1
if pregunta_4.lower() == "no":
    resp_correctas = resp_correctas +  1
    print("¡Es correcto!")
else:
    print ("Eso es incorrecto")
print ("")

#Quinta pregunta

pregunta_5 = input("¿El tomate es un vegetal? \nResp. ")
preg_totales = preg_totales + 1
if pregunta_5.lower() == "no":
    resp_correctas = resp_correctas +  1
    print("¡Es correcto!")
else:
    print ("Eso es incorrecto")
print ("")


#Valoración de preguntas

if resp_correctas == 0:
    print ("Fallaste en todas las respuestas")

else:
    porcentaje = (resp_correctas/preg_totales)*100
    print ("Acertastes", resp_correctas, "preguntas")
    print ("Tu puntuación es de", porcentaje,"%")


#print ("Preguntas totales", preg_totales)
#print ("Respuestas correctas", resp_correctas)

print ("")

#Valoraciones finales:

if resp_correctas != 0:
    porcentaje = (resp_correctas//preg_totales)*100
    if porcentaje == 100:
        print ("¡Felicitaciones! Acertaste todas las respuestas")
    elif porcentaje > 90:
        print ("¡Por poco aciertas todas!")
    elif porcentaje > 70:
        print ("¡Es un buen resultado pero puedes mejorar!")
    else:
        print ("Buen intento")
