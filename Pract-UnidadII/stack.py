historial_navegacion=[]

##Operacion para apilar(PUSH)
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.com")
print("historial cargado", historial_navegacion)

#Operacion cima(TOP-PEEK)
pagina_actual=historial_navegacion[-1]
print("pagian actual en pantalla: ", pagina_actual)

#Operacion para desapilar(POP)
pagina_cerrada=historial_navegacion.pop()
print("saliendo de:",pagina_cerrada)
print("historial despues de presionar 'Atras' ", historial_navegacion)

#Operacion tamaño(SIZE)
total_paginas=len(historial_navegacion)
print("paginas guardadas", total_paginas)

#Operacion vacia(EMPTY)
sin_paginas=len(historial_navegacion)
print("¿El historial esta vacio", sin_paginas)

#