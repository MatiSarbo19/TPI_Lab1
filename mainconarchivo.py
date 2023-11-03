import calculos
import os

nombre_cliente = input("Ingrese su nombre completo: ")
os.system('cls')
        
dni_cliente = input("Ingrese su número de DNI: ")
os.system('cls')

telefono_cliente = input("Ingrese su número de teléfono: ")
os.system('cls')

while True:
    print('En qué medida quiere ingresar la Longitud?: \n1)Metros \n2)Centimetros \n3)Pies \n4)Pulgadas ')
    try:
        medida = int(input("Ingrese el Número: "))
        if 1<= medida <=4:
            break
        else:
            os.system('cls')
            print('Ingrese un número entre 1 y 4.')
    except ValueError:
        os.system('cls')
        print('Ingrese un número Válido.')
while True:
    try:
        longitud = float(input('Ingrese la longitud de la superficie a rellenar: '))
        if longitud > 0:
            break
        else:
            os.system('cls')
            print('Ingrese un número Positivo.')
    except ValueError:
        os.system('cls')
        print('Ingrese un número Válido.')
match medida:
    case 2:
        longitud = longitud * 0.01
    case 3: 
        longitud = longitud * 0.3048
    case 4:
        longitud = longitud * 0.0254
os.system('cls')
while True:
    print('En qué medida quiere ingresar el Ancho?: \n1)Metros \n2)Centimetros \n3)Pies \n4)Pulgadas ')
    try:
        medida = int(input("Ingrese el Número: "))
        if 1<= medida <= 4:
            break
        else:
            os.system('cls')
            print('Ingrese un número entre 1 y 4.')
    except ValueError:
        os.system('cls')
        print('Ingrese un número Válido.')
while True:
    try:
        ancho = float(input('Ingrese el ancho de la superficie a rellenar: '))
        if ancho > 0:
            break
        else:
            os.system('cls')
            print('Ingrese un número Positivo.')
    except ValueError:
        os.system('cls')
        print('Ingrese un número Válido.')
match medida:
    case 2:
        ancho = ancho * 0.01
    case 3: 
        ancho = ancho * 0.3048
    case 4:
        ancho = ancho * 0.0254
os.system('cls')
while True:
    print('En qué medida quiere ingresar el Espesor / Altura?: \n1)Metros \n2)Centimetros \n3)Pies \n4)Pulgadas ')
    try:
        medida = int(input("Ingrese el Número: "))
        if 1 <= medida <= 4:
            break
        else:
            os.system('cls')
            print('Ingrese un número entre 1 y 4.')
    except ValueError:
        os.system('cls')
        print('Ingrese un número Válido.')
while True:
    try:
        espesor = float(input('Ingrese el espesor / altura de la superficie a rellenar: '))
        if espesor > 0:
            break
        else:
            os.system('cls')
            print('Ingrese un número Positivo.')
    except ValueError:
        os.system('cls')
        print('Ingrese un número Válido.')
match medida:
    case 2:
        espesor = espesor * 0.01
    case 3: 
        espesor = espesor * 0.3048
    case 4:
        espesor = espesor * 0.0254
os.system('cls')
while True:
    print('¿Que tipo de concreto quiere?, en base a su resistencia: ') 
    print('(Cemento) : (Arena) : (Grava)')
    print('1)| 1     :    3    :    6   | Resistencia (kg/cm2) = 105')
    print('2)| 1     :    3    :    4   | Resistencia (kg/cm2) = 140')
    print('3)| 1     :    2    :    4   | Resistencia (kg/cm2) = 175')
    print('4)| 1     :    2    :    3   | Resistencia (kg/cm2) = 210 (Normal, Para contrapiso)' )
    print('5)| 1     :    2    :    2   | Resistencia (kg/cm2) = 246')
    try:
        tipo_piso = int(input('Ingrese el Número (1 a 5): '))
        if 1<= tipo_piso <=5 :
            break
        else:
            os.system('cls')
            print('Ingrese un número entre 1 y 5.')
    except ValueError:
        os.system('cls')
        print('Ingrese un número Válido.')

volumen = calculos.calcular_volumen(longitud,ancho,espesor)

cemento = calculos.calcular_cemento(volumen,tipo_piso)
arena = calculos.calcular_arena(volumen,tipo_piso)
grava = calculos.calcular_grava(volumen,tipo_piso)
agua = calculos.calcular_agua(volumen,tipo_piso)
hormigon = calculos.calcular_hormigon(cemento,arena,grava,agua,tipo_piso)

print(f'La cantidad de bolsas de cemento que se necesitan es: {cemento} bolsas de 50 kg.')

print(f'La cantidad de arena que se necesita es: {arena} m3.')

print(f'La cantidad de grava que necesitan es: {grava} m3.')

print(f'La cantidad de agua que se necesita es: {agua} lts.')

print(f'volumen = {volumen}')

print(f'El total de hormigón es: {hormigon} m3.')

print(f'La Longitud del piso es: {longitud} metros')
print(f'El ancho del piso es: {ancho} metros')
print(f'El espesor / altura del piso es: {espesor} metros')

if not os.path.exists("./facturas"):
    os.mkdir("./facturas")
os.chdir("./facturas")
f = open(f"Factura-{nombre_cliente}.txt","w+")

ticket = f"""
--------------------------------------------------
                DETALLES DEL CLIENTE
--------------------------------------------------

Nombre: {nombre_cliente}
DNI: {dni_cliente}
Teléfono: {telefono_cliente}

--------------------------------------------------
                DETALLES DE LA SOLICITUD
--------------------------------------------------

Para una superficie en la cual:

La Longitud del piso: {longitud} metros.
El ancho del piso: {ancho} metros.
Espesor / altura del piso: {espesor} metros.
Tipo de concreto elegido: {tipo_piso}.

--------------------------------------------------
                CANTIDADES NECESARIAS
--------------------------------------------------

Bolsas de cemento (50 kg.): {cemento} 
Arena: {arena} m3.
Grava: {grava} m3.
Agua: {agua} lts.

Total de hormigón: {hormigon} m3.

--------------------------------------------------


"""

print(f"La factura ha sido creada y guardada para su impresión como Factura-{nombre_cliente}.txt")

f.write(ticket)