'''
La programadora quiere hacer una cuenta atrás desde 10.
¿Qué es lo que está mal y cómo se puede arreglar?

i = 10
while i == 0:
    print (i)
    i -= 1
'''
i = 10
while i != 0:
    i -= 1
    print (i)

'''
¿Qué es lo que está mal en este código que pretende contar hasta 10?
¿Qué pasará si se ejecuta? ¿Cómo se puede arreglar?

i = 1
while i < 10:
    print (i)
'''

i = 1
while i < 10:
    i += 1
    print (i)