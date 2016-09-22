import string

def estadoMal():
        print('por que, te ha pasado algo?')
        razonMal = raw_input()
        if('clases' in razonMal.lower()):
                print('no te preocupes tienes tiempo para mejorar tu notas')
        elif('papá' in razonMal.lower() or 'mamá' in razonMal.lower()):
                print('los problemas con los padres son bien dificiles de tratar')
                raw_input()
        elif('herman' in razonMal.lower()):
                print('los hermanos siempre dan problemas, pero son familia')
                raw_input()
        elif('famili' in razonMal.lower()):
                print('la familia es familia, estan en las buenas y las malas')
                raw_input()
        elif('trabajo' in razonMal.lower()):
                print('huy que mal, bastante atareado?')
                trabajo = raw_input()
                if('si' in trabajo.lower() or 'imagina' in trabajo.lower()):
                        print('pero toca, para llevar pan a la mesa, jajaja')
                        raw_input()
                elif('jef' in trabajo.lower()):
                        print('y no has hablado con alguien mas para solucionar')
                        razonTrabajo = raw_input()
                        if('si' in razonTrabajo.lower()):
                                print('no te precoupes ya veras que todo solucionara')
                                raw_input()
                        elif('no' in razonTrabajo.lower()):
                                print('Y que estas esperando no hay nada que una buena conversasion no ayude a mejorar')
                                raw_input()
        elif('hij' in razonMal.lower()):
                print('no te preocupes ya veras que todo se solucionara')
                raw_input()
                                

                
                        
        #controlar la situacion para la charla de mal momento
	
def estadoBien():
                print('me alegro mucho, ¿Cuentame estas haciendo algun deporte?')
                deporte = raw_input()
                if('si' in deporte.lower()):
                        print('que bien que practiques un deporte')
                        deportePractica()
                else:
                        print('y que haces en tus tiempos libres?')
                        pasatiempo = raw_input()
                        if('leer' in pasatiempo.lower() or 'leo' in pasatiempo.lower()):
                                print('y que libro estas leyendo?')
                                libro = raw_input()
                                print('quien es el autor?')
                                autor = raw_input()
                        elif('peliculas' in pasatiempo.lower()):
                                print('que bien, cual es la ultima pelicula que has visto')
                                pelicula = raw_input()
                                print(pelicula + ', tengo planes de verla que tan buena es?')
                                criticaPelicula = raw_input()
                                if('mal' in criticaPelicula.lower()):
                                        print('Que mal, ya no la voy a ir a ver')
                                        raw_input()
                                elif('buena' in criticaPelicula.lower() or 'genial' in criticaPelicula.lower() or 'cool' in criticaPelicula.lower() or 'pinta' in criticaPelicula.lower()):
                                        print('oh genial, manana mismo la ire a ver')
                                        raw_input()
                        elif('nada' in pasatiempo.lower()):
                                print('que improductivo eres tiens que buscar algo que hacer en tus tiempos libres')
                                raw_input()
                                        
                        
                
        #Continuar los pasatiempos


def isInt( s ):
   try:
      int(s)
      return True
   except ValueError:
      return False

def deportePractica():
        print('y que deporte estas practicando')
        tipoDeporte = raw_input()
        if('futbol' in tipoDeporte.lower()):
                print('que bien practiques futbol en que posicion juegas')
                posicionFutbol = raw_input()
        elif('basquet' in tipoDeporte.lower()):
                print('')
        #continuar platica de deportes

                
print("Hola Como te llamas? ")
nombre = raw_input()
print('hola '+ nombre)
print('¿como has estado?')
estadoAnimo = raw_input()
if('bien' in estadoAnimo.lower() or 'excelente' in estadoAnimo.lower()):
        estadoBien()
elif('mal' in estadoAnimo.lower() or 'pesimo' in estadoAnimo.lower()):
        estadoMal()
else:
        print('eres raro Adios')

exit()
