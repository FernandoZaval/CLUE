import random
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)


def juego0(caso, nom_jugador):
	asesino_real = caso[0]
	arma_real = caso [1]
	lugar_real = caso [2]
	#print(asesino_real,arma_real,lugar_real)
	oportunidades = 0
	

	while oportunidades < 7:

		print("Ahora es tu oportunidad de recolectar informacion. Elige sobre lo que quieres preguntar con el teclado y presiona enter")
		print("\n 1.- Armas\n 2.- Sospechosos\n 3.- Lugares")
		op = int(input())
		clearConsole()

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("Haz elegido preguntar sobre armas, ahora elige sobre cúal quieres saber. \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
			opcion_arma = int(input())
			clearConsole()
			if opcion_arma <= 0 or opcion_arma>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_arma == 1: 
				print("La Cantinera asegura haber dejado todas las botellas bajo llave, por lo que nadie pudo haberlas utilizado ")
				oportunidades = oportunidades+1
			if opcion_arma == 2: 
				print("El Sacerdote confiscó la escopeta dentro de la Iglesia por un accidente reciente. Dice haber mantenido la Iglesia bajo llave durante toda la noche")
				oportunidades = oportunidades+1
			if opcion_arma == 3: 
				print("La Doctora dijo estar toda la noche en la enfermería buscando unas tijeras faltantes. Dice haber visto pasar a la Cantinera por la enfermeria")
				oportunidades = oportunidades+1
			if opcion_arma == 4: 
				print("El Sheriff dijo estar trabajando toda la noche sin parar y haber tomado presatdo el canddelabro porque no tenía luz en la comisaría")
				oportunidades = oportunidades+1
			if opcion_arma == 5: 
				print("La cuerda debido a recientes robos ha sido utilizada para mantener la tienda cerrada por las noches")
				oportunidades = oportunidades+1

		if op == 2:
			print("Haz elegido preguntar sobre sospechosos, ahora elige sobre cúal quieres saber. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero ")
			opcion_sus = int(input())
			clearConsole()
			if opcion_sus <= 0 or opcion_sus>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_sus == 1: 
				print("La cantinera confesó tomar las tijeras de la enfermería para arreglar su vestido, ya que recibiría al vaquero para cenar en su casa. Después de cenar y que el vaquero se fuera asegura haber dormido toda la noche")
				oportunidades = oportunidades+1
			if opcion_sus == 2: 
				print("El Sheriff dijo estar trabajando toda la noche sin parar y haber tomado presatdo el canddelabro porque no tenía luz en la comisaría")
				oportunidades = oportunidades+1
			if opcion_sus == 3: 
				print("El Sacerdote nos cuenta que debido al insomnio que sufre estuvo caminando por el pueblo durante la noche y escuhó ruidos en la cantina")
				oportunidades = oportunidades+1
			if opcion_sus == 4: 
				print("La Doctora dijo estar toda la noche en la enfermería buscando unas tijeras faltantes. Dice haber visto pasar a la Cantinera por la enfermeria")
				oportunidades = oportunidades+1
			if opcion_sus == 5: 
				print("El vaquero asegura haber pasado la noche con la cantinera y muy temprano por la mañana, antes de que la cantinera despertara dirigirse a la iglesia a rezar")
				oportunidades = oportunidades+1

		if op == 3:
			print("Haz elegido preguntar sobre Lugares, ahora elige sobre cúal quieres saber. \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
			opcion_lugar = int(input())
			clearConsole()
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_lugar == 1: 
				print("El Sacerdote nos cuenta que debido al insomnio que sufre estuvo caminando por el pueblo durante la noche y escuhó ruidos en la cantina")
				oportunidades = oportunidades+1
			if opcion_lugar == 2: 
				print("El Sheriff dijo estar trabajando toda la noche sin parar y haber tomado presatdo el candelabro porque no tenía luz en la comisaría")
				oportunidades = oportunidades+1
			if opcion_lugar == 3: 
				print("La Doctora dijo estar toda la noche en la enfermería buscando unas tijeras faltantes. Dice haber visto pasar a la Cantinera por la enfermeria")
				oportunidades = oportunidades+1
			if opcion_lugar == 4: 
				print("La cuerda debido a recientes robos ha sido utilizada para mantener la tienda cerrada por las noches")
				oportunidades = oportunidades+1
			if opcion_lugar == 5: 
				print("El Sacerdote confizcó la escopeta dentro de la Iglesia por un accidente reciente. Dice haber mantenido la Iglesia bajo llave durante toda la noche")
				oportunidades = oportunidades+1

	
	print("Tus preguntas han terminado, es momento de elegir al culpable. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero  ")
	asesino_usuario = int(input())
	clearConsole()
	print("Ahora dinos cual arma utilizó el culpable \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
	arma_usuario = int(input())
	clearConsole()
	print("Por último dinos donde crees que realizó el asesinato \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
	lugar_usuario = int(input())
	clearConsole()

	resultado_asesino = (personajes[asesino_usuario-1] == asesino_real )
	resultado_arma =  (armas[arma_usuario-1] == arma_real)
	resultado_lugar =  (lugares[lugar_usuario-1] == lugar_real)

	if resultado_asesino == True and resultado_arma == True and resultado_lugar == True:
		print("¡Felicidades! El vaquero confesó haber matado al esposo de la cantinera en un frenesí de celos. Él tomó las tijeras que vio en la casa de la cantinera")
	else:
		print("Haz fallado en por lo menos una opción. Recuerda que realizar las preguntas correctas te puede llevar a la verdad mas rápido de lo que crees")

def juego1(caso, nom_jugador):
	asesino_real = caso[0]
	arma_real = caso [1]
	lugar_real = caso [2]
	#print(asesino_real,arma_real,lugar_real)
	oportunidades = 0
	

	while oportunidades < 7:

		print("Ahora es tu oportunidad de recolectar informacion. Elige sobre lo que quieres preguntar con el teclado y presiona enter")
		print("\n 1.- Armas\n 2.- Sospechosos\n 3.- Lugares")
		op = int(input())
		clearConsole()

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("Haz elegido preguntar sobre armas, ahora elige sobre cúal quieres saber. \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
			opcion_arma = int(input())
			clearConsole()
			if opcion_arma <= 0 or opcion_arma>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_arma == 1: 
				print("Debido a que la noche anterior hubo una pelea en la cantina, se perdieron y rompieron muchas botellas, la cantinera se quedó sola toda la noche limpiando el desorden")
				oportunidades = oportunidades+1
			if opcion_arma == 2: 
				print("El sacerdote dijo estar retenido toda la noche como testigo en la comisaria por la pelea de la cantina. También dice no haber visto la escopeta en la oficina del sheriff")
				oportunidades = oportunidades+1
			if opcion_arma == 3: 
				print("La doctora estuvo toda la noche en la enfermería ocupada curando a los heridos de la pelea de la cantina con sus utensilios ")
				oportunidades = oportunidades+1
			if opcion_arma == 4: 
				print("El vaquero dijo utilizar el candelabro para buscar al sacerdote en la iglesia pero no lo encontró")
				oportunidades = oportunidades+1
			if opcion_arma == 5: 
				print("La cuerda que era utilizada para cerrar la tienda se encontró en el lugar pero trozada")
				oportunidades = oportunidades+1

		if op == 2:
			print("Haz elegido preguntar sobre sospechosos, ahora elige sobre cúal quieres saber. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero ")
			opcion_sus = int(input())
			clearConsole()
			if opcion_sus <= 0 or opcion_sus>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_sus == 1: 
				print("Debido a que la noche anterior hubo una pelea en la cantina, se perdieron y rompieron muchas botellas, la cantinera se quedó sola toda la noche limpiando el desorden")
				oportunidades = oportunidades+1
			if opcion_sus == 2: 
				print("El sheriff dice haber estado en la cantina invesitgando la pelea y después interrogar a los involucrados en la pelea ")
				oportunidades = oportunidades+1
			if opcion_sus == 3: 
				print("El sacerdote dijo estar en la comisaria testificando sobre la pelea de la cantina y no haber visto al sheriff en ningun momento")
				oportunidades = oportunidades+1
			if opcion_sus == 4: 
				print("La doctora dijo estar ocupada en la enfermería curando a los heridos pero que al vaquero después de curarlo ya no lo vio en toda la noche")
				oportunidades = oportunidades+1
			if opcion_sus == 5: 
				print("El vaquero dice que después de ser curado fue en busca del sacerdote para disculparse por iniciar la pelea pero al no encontrarlo se fue a su casa")
				oportunidades = oportunidades+1

		if op == 3:
			print("Haz elegido preguntar sobre Lugares, ahora elige sobre cúal quieres saber. \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
			opcion_lugar = int(input())
			clearConsole()
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_lugar == 1: 
				print("Debido a que la noche anterior hubo una pelea en la cantina, se perdieron y rompieron muchas botellas, la cantinera se quedó sola toda la noche limpiando el desorden")
				oportunidades = oportunidades+1
			if opcion_lugar == 2: 
				print("El sacerdote dijo estar retenido toda la noche como testigo en la comisaria por la pelea de la cantina. También dice no haber visto la escopeta en la oficina del sheriff")
				oportunidades = oportunidades+1
			if opcion_lugar == 3: 
				print("La doctora estuvo toda la noche en la enfermería ocupada curando a los heridos de la pelea de la cantina con sus utensilios")
				oportunidades = oportunidades+1
			if opcion_lugar == 4: 
				print("La cuerda que era utilizada para cerrar la tienda se encontró en el lugar pero trozada")
				oportunidades = oportunidades+1
			if opcion_lugar == 5: 
				print("El vaquero asegura que la iglesia estaba vacia, ya que al buscar al sacerdote no vio a nadie más")
				oportunidades = oportunidades+1

	
	print("Tus preguntas han terminado, es momento de elegir al culpable. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero  ")
	asesino_usuario = int(input())
	clearConsole()
	print("Ahora dinos cual arma utilizó el culpable \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
	arma_usuario = int(input())
	clearConsole()
	print("Por último dinos donde crees que realizó el asesinato \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
	lugar_usuario = int(input())
	clearConsole()

	resultado_asesino = (personajes[asesino_usuario-1] == asesino_real )
	resultado_arma =  (armas[arma_usuario-1] == arma_real)
	resultado_lugar =  (lugares[lugar_usuario-1] == lugar_real)

	if resultado_asesino == True and resultado_arma == True and resultado_lugar == True:
		print("¡Felicidades! Después de descubrir al sheriff ha confesado que en la pelea de la cantina habían herido a su hijo de gravedad y decidió tomar venganza con una botella que robó de la cantina")
	else:
		print("Haz fallado en por lo menos una opción. Recuerda que realizar las preguntas correctas te puede llevar a la verdad mas rápido de lo que crees")

def juego2(caso, nom_jugador):
	asesino_real = caso[0]
	arma_real = caso [1]
	lugar_real = caso [2]
	#print(asesino_real,arma_real,lugar_real)
	oportunidades = 0
	

	while oportunidades < 7:

		print("Ahora es tu oportunidad de recolectar informacion. Elige sobre lo que quieres preguntar con el teclado y presiona enter")
		print("\n 1.- Armas\n 2.- Sospechosos\n 3.- Lugares")
		op = int(input())
		clearConsole()

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("Haz elegido preguntar sobre armas, ahora elige sobre cúal quieres saber. \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
			opcion_arma = int(input())
			clearConsole()
			if opcion_arma <= 0 or opcion_arma>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_arma == 1: 
				print("La cantinera asegura que todas sus botellas están en su lugar")
				oportunidades = oportunidades+1
			if opcion_arma == 2: 
				print("El sheriff dice que su escopeta no funciona y que la mandó a arreglar, por eso no la tiene")
				oportunidades = oportunidades+1
			if opcion_arma == 3: 
				print("La doctora dice haber dejado todo su equipo bajo llave antes de salir")
				oportunidades = oportunidades+1
			if opcion_arma == 4: 
				print("El candelabro no estaba en su lugar habitual, sino en la zona de limpieza de la iglesia")
				oportunidades = oportunidades+1
			if opcion_arma == 5: 
				print("La cuerda fue utilizada por el sheriff para detener a un delincuente toda la noche")
				oportunidades = oportunidades+1

		if op == 2:
			print("Haz elegido preguntar sobre sospechosos, ahora elige sobre cúal quieres saber. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero ")
			opcion_sus = int(input())
			clearConsole()
			if opcion_sus <= 0 or opcion_sus>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_sus == 1: 
				print("La cantinera dice haber estado platicando toda la noche en la cantina con la doctora")
				oportunidades = oportunidades+1
			if opcion_sus == 2: 
				print("El sheriff asegura haber estado trabajando toda la noche y solo dejar la comisaria para ir a la tienda")
				oportunidades = oportunidades+1
			if opcion_sus == 3: 
				print("El sacerdote asegura solo dejar la iglesia para ir a la tienda")
				oportunidades = oportunidades+1
			if opcion_sus == 4: 
				print("La doctora dice haber pasado toda la noche en la cantida platicando con la cantinera")
				oportunidades = oportunidades+1
			if opcion_sus == 5: 
				print("El vaquero pasó toda la noche cuidando la tienda dice solo haber visto al sheriff")
				oportunidades = oportunidades+1

		if op == 3:
			print("Haz elegido preguntar sobre Lugares, ahora elige sobre cúal quieres saber. \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
			opcion_lugar = int(input())
			clearConsole()
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_lugar == 1: 
				print("En la cantina permanecieron la doctora y la cantinera platicando toda la noche")
				oportunidades = oportunidades+1
			if opcion_lugar == 2: 
				print("La comisaria se mantuvo ocupada toda la noche y el sheriff dice solo haber salido cuando fue a la tienda")
				oportunidades = oportunidades+1
			if opcion_lugar == 3: 
				print("La doctora dice haber cerrado la enfermería toda la noche")
				oportunidades = oportunidades+1
			if opcion_lugar == 4: 
				print("La tienda la custodió toda la noche el vaquero")
				oportunidades = oportunidades+1
			if opcion_lugar == 5: 
				print("El sacerdote dice solo dejar la iglesa para ir a la tienda")
				oportunidades = oportunidades+1

	
	print("Tus preguntas han terminado, es momento de elegir al culpable. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero  ")
	asesino_usuario = int(input())
	clearConsole()
	print("Ahora dinos cual arma utilizó el culpable \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
	arma_usuario = int(input())
	clearConsole()
	print("Por último dinos donde crees que realizó el asesinato \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
	lugar_usuario = int(input())
	clearConsole()

	resultado_asesino = (personajes[asesino_usuario-1] == asesino_real )
	resultado_arma =  (armas[arma_usuario-1] == arma_real)
	resultado_lugar =  (lugares[lugar_usuario-1] == lugar_real)

	if resultado_asesino == True and resultado_arma == True and resultado_lugar == True:
		print("¡Felicidades! Después de presionar con tus preguntas al sacerdote ha confesado que alguien se había metido a robar a la iglesia y al quererlo detener lo golpeó con el candelabro, matandolo por error.")
	else:
		print("Haz fallado en por lo menos una opción. Recuerda que realizar las preguntas correctas te puede llevar a la verdad mas rápido de lo que crees")

def juego3(caso, nom_jugador):
	asesino_real = caso[0]
	arma_real = caso [1]
	lugar_real = caso [2]
	#print(asesino_real,arma_real,lugar_real)
	oportunidades = 0
	

	while oportunidades < 7:

		print("Ahora es tu oportunidad de recolectar informacion. Elige sobre lo que quieres preguntar con el teclado y presiona enter")
		print("\n 1.- Armas\n 2.- Sospechosos\n 3.- Lugares")
		op = int(input())
		clearConsole()

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("Haz elegido preguntar sobre armas, ahora elige sobre cúal quieres saber. \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
			opcion_arma = int(input())
			clearConsole()
			if opcion_arma <= 0 or opcion_arma>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_arma == 1: 
				print("La cantinera dice todo en su inventario salió completo")
				oportunidades = oportunidades+1
			if opcion_arma == 2: 
				print("El sheriff nos informa que alguien a robado su escopeta, dejando solo un fuerte olor a alcohol")
				oportunidades = oportunidades+1
			if opcion_arma == 3: 
				print("La doctora dice que después de terminar su turno guardo sus instrumentos bajo llave")
				oportunidades = oportunidades+1
			if opcion_arma == 4: 
				print("El sacerdote pasó la noche limpiando sus candelabros ")
				oportunidades = oportunidades+1
			if opcion_arma == 5: 
				print("La cuerda fue utilizada para cerrar la tienda durante toda la noche")
				oportunidades = oportunidades+1

		if op == 2:
			print("Haz elegido preguntar sobre sospechosos, ahora elige sobre cúal quieres saber. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero ")
			opcion_sus = int(input())
			clearConsole()
			if opcion_sus <= 0 or opcion_sus>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_sus == 1: 
				print("La cantinera después de terminar su inventario fue directo a su casa, dijo escuchar ruidos en la enfermeria")
				oportunidades = oportunidades+1
			if opcion_sus == 2: 
				print("El sheriff dijo pasar la noche en la comisaria por todo el trabajo que tenía. También dice que en la madrugada llegó la doctora y sin decir nada se fue después de unos minutos")
				oportunidades = oportunidades+1
			if opcion_sus == 3: 
				print("El sacerdote asegura haber pasado la noche en la iglesia haciendo limpieza")
				oportunidades = oportunidades+1
			if opcion_sus == 4: 
				print("La doctora dice haber pasado la noche en la enfermería")
				oportunidades = oportunidades+1
			if opcion_sus == 5: 
				print("El vaquero dice que fue herido en una pelea e ir a la enfermería para ser curado pero cuando tocó la puerta nadie le abrió")
				oportunidades = oportunidades+1

		if op == 3:
			print("Haz elegido preguntar sobre Lugares, ahora elige sobre cúal quieres saber. \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
			opcion_lugar = int(input())
			clearConsole()
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_lugar == 1: 
				print("La Cantina estuvo cerrada toda la noche por inventario")
				oportunidades = oportunidades+1
			if opcion_lugar == 2: 
				print("Fue una noche ocupada en la comisaría así que nada pudo haber pasado ahí, dice el sheriff")
				oportunidades = oportunidades+1
			if opcion_lugar == 3: 
				print("La doctora dice que la enfermería estuvo abierta como de costumbre")
				oportunidades = oportunidades+1
			if opcion_lugar == 4: 
				print("La tienda permaneció cerrada por la noche con la cuerda")
				oportunidades = oportunidades+1
			if opcion_lugar == 5: 
				print("El padre dijo estar en la iglesia toda la noche ")
				oportunidades = oportunidades+1

	
	print("Tus preguntas han terminado, es momento de elegir al culpable. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero  ")
	asesino_usuario = int(input())
	clearConsole()
	print("Ahora dinos cual arma utilizó el culpable \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
	arma_usuario = int(input())
	clearConsole()
	print("Por último dinos donde crees que realizó el asesinato \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
	lugar_usuario = int(input())
	clearConsole()

	resultado_asesino = (personajes[asesino_usuario-1] == asesino_real )
	resultado_arma =  (armas[arma_usuario-1] == arma_real)
	resultado_lugar =  (lugares[lugar_usuario-1] == lugar_real)

	if resultado_asesino == True and resultado_arma == True and resultado_lugar == True:
		print("¡Felicidades!, La doctora ha confesado ella cerró la enfermeria para cometer una atroz crimen con la escopeta que robó del sheriff")
	else:
		print("Haz fallado en por lo menos una opción. Recuerda que realizar las preguntas correctas te puede llevar a la verdad mas rápido de lo que crees")

def juego4(caso, nom_jugador):
	asesino_real = caso[0]
	arma_real = caso [1]
	lugar_real = caso [2]
	#print(asesino_real,arma_real,lugar_real)
	oportunidades = 0
	

	while oportunidades < 7:

		print("Ahora es tu oportunidad de recolectar informacion. Elige sobre lo que quieres preguntar con el teclado y presiona enter")
		print("\n 1.- Armas\n 2.- Sospechosos\n 3.- Lugares")
		op = int(input())
		clearConsole()

		if op <= 0 or op>3:
			print("Ingresa un número válido")

		if op == 1:
			print("Haz elegido preguntar sobre armas, ahora elige sobre cúal quieres saber. \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
			opcion_arma = int(input())
			clearConsole()
			if opcion_arma <= 0 or opcion_arma>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_arma == 1: 
				print("En el conteo nocturno todas las botellas fueron contadas sin falta")
				oportunidades = oportunidades+1
			if opcion_arma == 2: 
				print("El sheriff tuvo la escopeta consigo toda la noche, la enfermera confirma esa historia")
				oportunidades = oportunidades+1
			if opcion_arma == 3: 
				print("La doctora estuvo tuvo su equipo consigo toda la noche, el sheriff confirma la historia")
				oportunidades = oportunidades+1
			if opcion_arma == 4: 
				print("El candelabro fue utilizado para iluminar la iglesia durante la misa")
				oportunidades = oportunidades+1
			if opcion_arma == 5: 
				print("El dueño de la tienda dice haber prestado la cuerda para cerrar la comisaría")
				oportunidades = oportunidades+1

		if op == 2:
			print("Haz elegido preguntar sobre sospechosos, ahora elige sobre cúal quieres saber. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero ")
			opcion_sus = int(input())
			clearConsole()
			if opcion_sus <= 0 or opcion_sus>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_sus == 1: 
				print("La cantinera dijo salir a fumar, y perder la noción del tiempo para cerrar la cantina y por eso cerrar tarde")
				oportunidades = oportunidades+1
			if opcion_sus == 2: 
				print("El sheriff dice haber estado la noche en la nueva comisaría")
				oportunidades = oportunidades+1
			if opcion_sus == 3: 
				print("Varios testigos aseguran ver al sacerdote ofertar la misa nocturna")
				oportunidades = oportunidades+1
			if opcion_sus == 4: 
				print("La doctora dice haber estado platicando con el sheriff la mayoria de la noche")
				oportunidades = oportunidades+1
			if opcion_sus == 5: 
				print("El vaquero dice haber estado en la cantina hasta que llegó la cantinera a cerrarla")
				oportunidades = oportunidades+1

		if op == 3:
			print("Haz elegido preguntar sobre Lugares, ahora elige sobre cúal quieres saber. \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
			opcion_lugar = int(input())
			clearConsole()
			if opcion_lugar <= 0 or opcion_lugar>5:
				print("Por no elegir una opcion válida haz perdido una oportunidad de preguntar. Más atención a la próxima")
				oportunidades = oportunidades+1
			if opcion_lugar == 1: 
				print("Según testigos la cantina estuvo abierta hasta altas horas de la noche, hasta que la cantinera llegó a cerrar más tarde que de costumbre")
				oportunidades = oportunidades+1
			if opcion_lugar == 2: 
				print("La comisaría se mantuvo cerrada una noche por problema de ratas")
				oportunidades = oportunidades+1
			if opcion_lugar == 3: 
				print("La enfermería fue utilizada también como comisaria y estuvo bastante concurrida")
				oportunidades = oportunidades+1
			if opcion_lugar == 4: 
				print("La tienda permaneció cerrada toda la noche pero con una cadena, ya que la cuerda fue prestada al sheriff")
				oportunidades = oportunidades+1
			if opcion_lugar == 5: 
				print("Por cuestiones religiosas se ofreció una misa nocturna que duró varias horas")
				oportunidades = oportunidades+1

	
	print("Tus preguntas han terminado, es momento de elegir al culpable. \n 1.- Cantinera\n 2.- Sheriff\n 3.- Sacerdote\n 4.- Doctora\n 5.- Vaquero  ")
	asesino_usuario = int(input())
	clearConsole()
	print("Ahora dinos cual arma utilizó el culpable \n 1.- Botella\n 2.- Escopeta\n 3.- Tijeras quirurjicas\n 4.- Candelabro\n 5.- Cuerda")
	arma_usuario = int(input())
	clearConsole()
	print("Por último dinos donde crees que realizó el asesinato \n 1.- Cantina\n 2.- Comisaría \n 3.- Enfermería\n 4.- Tienda\n 5.- Iglesia ")
	lugar_usuario = int(input())
	clearConsole()

	resultado_asesino = (personajes[asesino_usuario-1] == asesino_real )
	resultado_arma =  (armas[arma_usuario-1] == arma_real)
	resultado_lugar =  (lugares[lugar_usuario-1] == lugar_real)

	if resultado_asesino == True and resultado_arma == True and resultado_lugar == True:
		print("¡Felicidades!, la Cantinera ha confesado haber olvidado sus llaves en la comisaria, asi que quitó la cuerda y mientras estaba dentro un vandido la atacó asi que se defendió y lo mató")
	else:
		print("Haz fallado en por lo menos una opción. Recuerda que realizar las preguntas correctas te puede llevar a la verdad mas rápido de lo que crees")

	

personajes = ["Cantinera", "Sheriff", "Sacerdote", "Doctora", "Vaquero "]
armas = ["Botella", "Escopeta","Tijeras quirurjicas", "Candelabro", "Cuerda"]
lugares = ["Cantina","Comisaría ","Enfermería","Tienda","Iglesia "]

c = random.randrange(4)

print ("¡Hola! Ha ocurrido un asesinato en pueblo en el transcurso de la noche y nos informar los jefes que eres el nuevo detective\n Pero primero necesitamos confirmar tu identidad")

nombre_jugador = input("Introduce tu nombre:")
clearConsole()
print("Ok",nombre_jugador,"Tenemos 5 sospechosos, 5 armas y 5 locaciones. \nPor tradiciones solo puedes realizar 7 preguntas, así que debes elegir con cuidado cada opción, ya que, si te equivocas puedes perder una oportunidad. Para elegir una opcion debes teclear el NUMERO y presionar enter ¡Todo el pueblo cuenta contgo! no nos falles")


if c == 0:
	caso = [personajes[4], armas[2], lugares[0]]
	juego0(caso,nombre_jugador)
	#print(caso[:])
if c == 1:
	caso = [personajes[1], armas[0], lugares[3]]
	juego1(caso,nombre_jugador)
	#print(caso[:])
if c == 2:
	caso = [personajes[2], armas[3], lugares[4]]
	juego2(caso,nombre_jugador)
	#print(caso[:])
if c == 3:
	caso = [personajes[3], armas[1], lugares[2]]
	juego3(caso,nombre_jugador)
	#print(caso[:])
if c == 4:
	caso = [personajes[0], armas[4], lugares[1]]
	juego4(caso,nombre_jugador)
	#print(caso[:])


