#Generar un archivo CSV con los datos de status.txt que nos indique si los senderos estan abiertos o cerrados
#El formato del archivo CSV es: 
#status, blankets_creek y rope_mill (nombres de columnas)
#"open", 0, 0 (1=abierto, 0=cerrado)
#"open",1 ,1

#eliminar entradas repetidas:

#creamos una estructura "set"
status_unicos = set()

#abrimos el archivo "status.txt" ('r' significa "lectura", es decir, no valos a reescribir el texto) 
# y le asignamos la letra 'f' como variable. Por cada linea en 'f', aplicamos las propiedades de set()
#es decir, eliminamos datos repetidos y los datos repetidos no se anaden, por lo que al final se van a 
#eliminar las lineas o entradas repetidas 
with open('status.txt', 'r') as f:
    for line in f.readlines():
        status_unicos.add(line.strip())

print(len(status_unicos))

#De 178 pasamos a 139 lineas 

#Vamos a presentar el documento 'status.txt' de una forma ordenada
for status in status_unicos:
    print(status)

#Podemos ver que se han eliminado las lineas duplicadas 

#ahora vamos a crear una funcion de lo antes ya hecho 
def eliminar_duplicados():
    status_unicos = set()
    with open('status.txt', 'r') as f:
        for line in f.readlines():
            status_unicos.add(line.strip())
    return list(status_unicos) #le convertimos en una lista para no tener problemas con el resto de funciones 

#vamos a crear una funcion para eliminar signos de puntuacion. 
def limpiar_datos(statuses):
    #statuses es una lista de strings que representan los estados de los senderos
    status_limpio=[]
    for status in statuses:
        linea=status.replace(',',' ')
        linea=status.replace('?',' ')
        linea=status.replace('!',' ')
        linea=status.replace('.',' ')
        status_limpio.append(linea) #agregamos, con la funcion "append" las lineas limpias al texto
    return status_limpio

#Vamos a normalizar la escritura cambiando todo a minusculas 
def normalizar_datos(statuses):
    status_normalizados = []
    for status in statuses:
        status_normalizados.append(status.lower())
    return status_normalizados

#Identificamos las frases correctas que nos dicen si los senderos están abiertos o cerrados 
def identificar_status(statuses):
#status, blankets_creek y rope_mill (nombres de columnas)
#"open", 0, 0 (1=abierto, 0=cerrado)
#"open",1 ,1
    valores = [] #lista para almacenar los resultados linea por linea 
    for status in statuses:
        if "all trails are open" in status: # status viene a ser cada oracion en el texto
            valores.append([status, 1, 1])
        elif "all trails are closed" in status:
            valores.append([status, 0, 0])
        elif "blankets creek is closed" in status and "rope mill is closed" in status:
            valores.append([status, 0, 0])
        elif "blankets creek is closed" in status and "rope mill is open" in status:
            valores.append([status, 0, 1])
        elif "blankets creek is open" in status and "rope mill is closed" in status:
            valores.append([status, 1, 0])
        elif "blankets creek is open" in status and "rope mill is open" in status:
            valores.append([status, 1, 1])
        elif "trails are open" in status:
            valores.append([status, 1, 1])
        elif "trails are closed" in status:
            valores.append([status, 0, 0])    
    return valores

#funcion para ver el progreso hasta este momento 
def main():
    status = eliminar_duplicados() #estamos reusando la variable "status" para que no haya problemas al momento de utilizarla
    status = limpiar_datos(status) # en otras funciones. Caso contrario, no se aplican dichas funciones al texto, en este caso 
    status = normalizar_datos(status)

    # a partir de la creacion de la funcion "identificar_status", cambiamos el lazo for que se tenia para el resto de funciones
    # puesto que solo queremos obtener el resultado de esta ultima funcion 
    #for status in status:
    #   print(status)

    #Este es el segundo lazo for creado para obtener los resultados solo de la funcion "identificar_status"
    #for linea in identificar_status(status):
    #   print(linea)

    #Finalmente, creamos el tercer lazo for para obtener un archivo .csv con los resultados finales 
    with open ('status.csv', 'w') as f:  # utlizamos 'w' porque queremos escribir en este archivo nuevo 
        import csv #paquete de python para tratar archivos .csv
        headers = ['status', 'blankets_creek', 'rope_mill'] #cabecera para el archivo 
        writer=csv.writer(f) #modulo para escribir en el archivo .csv
        writer.writerow(headers) # escribimos la primera fila que son los headers 
        writer.writerows(identificar_status(status))


#asignamos a la funcion 'main' como la principal y la que se va a ejecutar en el terminal
if __name__=='__main__':
    main()



