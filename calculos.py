#Todas las funciones retornan m2
def calcular_volumen(longitud,ancho,espesor):
    #Los valores de los parametros tienen que estar en mts
    #El volumen sale en m3
    volumen = round(longitud * ancho * espesor,2)
    return volumen
def calcular_cemento(volumen,tipo_piso):
    #utilizo el match para saber que cantidad de cemento se utiliza en relacion a la tabla
    match tipo_piso:
        case 1:
            cant_cemento = 210
        case 2: 
            cant_cemento = 260
        case 3:
            cant_cemento = 300 #MODIFICAR NUEVAMENTE LOS RESULTADOS DE LOS MATERIALES
        case 4:
            cant_cemento = 350
        case 5:
            cant_cemento = 420
    #Se toma como referencia al cemento con bolsas de 50kg por eso se divide la cantidad de cemento por 50
    cemento = round((volumen*(cant_cemento)/50)*1.05)
    #la funcion retorna la cantidad de bolsas de 50kg que se necesitan
    return cemento
def calcular_arena(volumen,tipo_piso):
    #utilizo el match para saber que cantidad de arena se utiliza en relacion a la tabla
    match tipo_piso:
        case 1:
            cant_arena = 0.5
        case 2: 
            cant_arena = 0.63
        case 3:
            cant_arena = 0.48
        case 4:
            cant_arena = 0.56
        case 5:
            cant_arena = 0.67
    #Calculo la arena a utilizar con la formula que esta en el video         
    arena = round(volumen*cant_arena,2)
    return arena
def calcular_grava(volumen,tipo_piso):
    #utilizo el match para saber que cantidad de grava se utiliza en relacion a la tabla
    match tipo_piso:
        case 1:
            cant_grava = 1.0
        case 2: 
            cant_grava = 0.84
        case 3:
            cant_grava = 0.96
        case 4:
            cant_grava = 0.84
        case 5:
            cant_grava = 0.67
    #Calculo la grava a utilizar con la formula que esta en el video
    grava = round(volumen*cant_grava,2)
    return grava
def calcular_agua(volumen,tipo_piso):
    #utilizo el match para saber que cantidad de grava se utiliza en relacion a la tabla
    match tipo_piso:
        case 1:
            cant_agua = 160
        case 2: 
            cant_agua = 170
        case 3:
            cant_agua = 170
        case 4:
            cant_agua = 180
        case 5:
            cant_agua = 220
    #Calculo el agua a utilizar con la formula que esta en el video
    agua = round(volumen*cant_agua)
    #el valor del agua está en litros
    return agua
def calcular_hormigon (cemento,arena,grava,agua,tipo_piso):
    match tipo_piso:
        case 1:
            #divide los materiales en partes y luego se suman para crear el volumen del hormigón
            volumen_cemento = (cemento*0.035) * (1/10)
            volumen_arena = arena * (3/10)
            volumen_grava = grava * (6/10)
            volumen_agua = agua *0.001 #pasa el agua a m3
        case 2:
            #paso las bolsas de 50 kg a m3 
            volumen_cemento = (cemento*0.035) * (1/8)
            volumen_arena = arena * (3/8)
            volumen_grava = grava * (4/8)
            volumen_agua = agua *0.001
        case 3:
            volumen_cemento = (cemento*0.035) * (1/7)
            volumen_arena = arena * (2/7)
            volumen_grava = grava * (4/7)
            volumen_agua = agua *0.001
        case 4:
            volumen_cemento = (cemento*0.035) * (1/6)
            volumen_arena = arena * (2/6)
            volumen_grava = grava * (3/6)
            volumen_agua = agua *0.001
        case 5:
            volumen_cemento = (cemento*0.035) * (1/5)
            volumen_arena = arena * (2/5)
            volumen_grava = grava * (2/5)
            volumen_agua = agua *0.001
   
    volumen_hormigon = round(volumen_cemento+volumen_arena+volumen_grava+volumen_agua)
    return volumen_hormigon
