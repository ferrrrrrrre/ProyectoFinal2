import csv
lista_datos=[]
with open("sinergia.csv", "r") as archivo:
  lector = csv.DictReader(archivo)

  for registro in lector:
    lista_datos.append(registro)

#Opción 1
#def rutas_exportacion_importacion (direccion):
  #contador = 0
  #rutas_contadas = []
  #rutas_conteo = []

  #for ruta in lista_datos:
    #if ruta["direction"] == direccion:
      #ruta_actual = [ruta["origin"], ruta["destination"]]
      #if ruta_actual not in rutas_contadas:
        #for ruta_bd in lista_datos:
          #if ruta_actual == [ruta_bd["origin"], ruta_bd["destination"]]:
            #contador += 1
        #rutas_contadas.append(ruta_actual)
        #rutas_conteo.append([ruta["origin"], ruta["destination"], contador])
        #contador = 0
  #rutas_conteo.sort(reverse = True, key = lambda x:x[2])     
  #return rutas_conteo

#conteo_exportaciones = rutas_exportacion_importacion("Exports")
#conteo_importaciones = rutas_exportacion_importacion ("Imports")

#print(conteo_exportaciones)
#print(conteo_importaciones)

#Opción 2
#def transporte_utilizado (direccion):
  #contador = 0
  #transporte_contadas = []
  #transporte_conteo = []

  #for transporte in lista_datos:
    #if transporte["direction"] == direccion:
      #transporte_actual = [transporte["transport_mode"]]
      #if transporte_actual not in transporte_contadas:
        #for transporte_bd in lista_datos:
          #if transporte_actual == [transporte_bd["transport_mode"]]:
            #contador += 1
        #transporte_contadas.append(transporte_actual)
        #transporte_conteo.append([transporte["transport_mode"], contador])
        #contador = 0
  #transporte_conteo.sort(reverse = True, key = lambda x:x[1])     
  #return transporte_conteo

#conteo_transporte_importaciones = transporte_utilizado("Imports")
#conteo_transporte_exportaciones = transporte_utilizado("Exports")
#print(conteo_transporte_importaciones)
#print(conteo_transporte_exportaciones)

#Opcion 3

#def valor_movimiento(direccion):
  #contados = []
  #valores_paises = []

  #for viaje in lista_datos:
    #actual = [direccion, viaje["origin"]] #["Exports", "Mexico"]
    #valor = 0
    #operaciones = 0

    #if actual in contados:
      #continue
    
    #for movimiento in lista_datos:
      #if actual == [movimiento["direction"], movimiento["origin"]]:
        #valor += int(movimiento["total_value"])
        #operaciones +=1
    
    #contados.append(actual)
    #valores_paises.append([direccion, viaje["origin"], valor, operaciones])

  #valores_paises.sort(reverse = True, key = lambda x:x[2]) #el 2 depende de qué quiera analizar
  #return valores_paises  

#valores_paises = valor_movimiento("Exports")
#print(valores_paises) #valor de exportaciones, operaciones

#def porcentaje_pais(lista_paises, porcentaje = 0.8):
  #valor_total = 0
  #for pais in lista_paises:
   #valor_total += pais [2]

  #paises = []
  #porcentajes_calculados = []
  #valor_actual = 0

  #for pais in lista_paises:
    #valor_actual += pais [2]
    #porcentaje_actual = round(valor_actual/valor_total, 3) #acota a 3 decimales
    #paises.append(pais)
    #porcentajes_calculados.append(porcentaje_actual)

    #if porcentaje_actual <= porcentaje:
      #continue
    #else:
      #if porcentaje_actual - porcentaje <= porcentajes_calculados[-2] - porcentaje:
        #break
      #else:
        #paises.pop(-1)
        #porcentajes_calculados.pop(-1)
        #break  
  #return paises

#paises_80 = porcentaje_pais(valor_movimiento("Exports")) 

#for pais in paises_80:
  #print(pais)


#Opcion 3.1
def valor_movimiento(direccion):
  contados = []
  valores_paises = []

  for viaje in lista_datos:
    actual = [direccion, viaje["destination"]] #["Imports", "Mexico"]
    valor = 0
    operaciones = 0

    if actual in contados:
      continue
    
    for movimiento in lista_datos:
      if actual == [movimiento["direction"], movimiento["destination"]]:
        valor += int(movimiento["total_value"])
        operaciones +=1
    
    contados.append(actual)
    valores_paises.append([direccion, viaje["destination"], valor, operaciones])

  valores_paises.sort(reverse = True, key = lambda x:x[2]) #el 2 depende de qué quiera analizar
  return valores_paises  

valores_paises = valor_movimiento("Imports")
print(valores_paises) #valor de importaciones, operaciones

def porcentaje_pais(lista_paises, porcentaje = 0.8):
  valor_total = 0
  for pais in lista_paises:
   valor_total += pais [2]

  paises = []
  porcentajes_calculados = []
  valor_actual = 0

  for pais in lista_paises:
    valor_actual += pais [2]
    porcentaje_actual = round(valor_actual/valor_total, 3) #acota a 3 decimales
    paises.append(pais)
    porcentajes_calculados.append(porcentaje_actual)

    if porcentaje_actual <= porcentaje:
      continue
    else:
      if porcentaje_actual - porcentaje <= porcentajes_calculados[-2] - porcentaje:
        break
      else:
        paises.pop(-1)
        porcentajes_calculados.pop(-1)
        break  
  return paises

paises_80 = porcentaje_pais(valor_movimiento("Imports")) 

for pais in paises_80:
  print(pais)