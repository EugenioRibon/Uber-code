import random 
CHAR_VACIO        =  "_........_"     # Símbolo en la matriz para representar una celda vacía
CHAR_UBER         =  "_..oT=o.._"      # Símbolo en la matriz para representar un UBER
CHAR_CLIENTE      =  "_. =:-) ._"      # Símbolo en la matriz para representar un CLIENTE/PASAJERO

COLOR_VERDE = "\033[1;32m"
COLOR_ROJO = "\033[1;31m"
COLOR_AMARILLO = "\033[1;33m"
COLOR_AZUL = "\033[1;34m"
COLOR_DEFECTO = "\033[0m"

celdas = 5
width = 8 
espacio = " "
heading_dis = 9

class Coche:
    def __init__(self, posicionx, posiciony, coste):
        self.posx = posicionx
        self.posy = posiciony
        self.coste = coste

    def buscar_cliente(self, cliente):
        self.coste += 5
        if self.posx != cliente.posx:

            if self.posx < cliente.posx:
                self.posx += 1

            elif self.posx > cliente.posx:
                self.posx -= 1

        elif self.posx == cliente.posx:

            if self.posy < cliente.posy:
                self.posy += 1

            elif self.posy > cliente.posy:
                self.posy -= 1
            
            else:
                pass

    def llevar_cliente(self, cliente):
        self.coste += 5
        if self.posx != cliente.destinox:

            if self.posx < cliente.destinox:
                self.posx += 1
                #posicion_cliente[0] = coche.posy

            elif self.posx > cliente.destinox:
                self.posx -= 1
                #posicion_cliente[0] = coche.posy

        elif self.posx == cliente.destinox:

            if self.posy < cliente.destinoy:
                self.posy += 1
                #posicion_cliente[1] = coche.posy

            if self.posy > cliente.destinoy:
                self.posy -= 1
                #posicion_cliente[1] = coche.posy

    def __str__(self):
        return f"xcoche =  {self.posx}, ycoche = {self.posy}"

class Cliente():
    def __init__(self, posicionx, posiciony):
        self.posx = posicionx
        self.posy = posiciony
        
        error = True
        while error:
            destino = []
            dest = input("introducir destino(x,y): ")
            for valor in dest:
                if valor != " " and valor != ",":
                    valor = int(valor)
                    destino.append(valor)
                    if len(destino) == 2 and 0 <= destino[0] < 5 and 0 <= destino[1] < 5:
                        error = False 
                    
                    else:
                        pass
                
                else: 
                    pass

        self.destinox = destino[0]
        self.destinoy = destino[1]

    def destino():
        pass

    def __str__(self):
        return f"xcliente = {self.posx}, ycliente = {self.posy}"


def mostrar_leyenda():
    print("\n\n### Leyenda:\n")
    print(f"{COLOR_AMARILLO+CHAR_CLIENTE+COLOR_DEFECTO}: Cliente de Uber")
    print(f"{COLOR_VERDE+CHAR_UBER+COLOR_DEFECTO}: Uber libre, no tiene servicio")
    print(f"{COLOR_AZUL+CHAR_UBER+COLOR_DEFECTO}: Uber buscando cliente")
    print(f"{COLOR_ROJO+CHAR_UBER+COLOR_DEFECTO}: Uber llevando cliente")

def crear_ciudad():
    # print("\n\n### Creando ciudad... \n")
    cont0 = 0
    plano_compl = {}
    # Aquí creo cada fila como una lista y despues hago un diccionario con cada una de las listas para poder acceder a todos los elementos
    while cont0 < celdas:
        plano_fila = []

        for j in range(1,celdas+1):
            fila = CHAR_VACIO
            plano_fila.append(fila)
        plano_compl[cont0] = plano_fila
        cont0 += 1
    return plano_compl
    # Ahora mismo mi mapa es un diccionario con listas asiganadas a las coordenadas y se pueden acceder a todos los elementos

def dibujar_ciudad(plano_completo):
    reps = 0
    heading = espacio * (heading_dis+1) + "0"
    for espacios in range(1, celdas):
        heading += espacio * heading_dis + str(espacios) 
    print(heading)

    while reps < celdas:
        dibujo_plano_fila = ""
        for k in range(0, celdas):
            dibujo_plano_fila += plano_completo[reps][k] 
        print(" ", reps, " ", dibujo_plano_fila)
        reps += 1

def posicionar_objetos():
    posicion = []
    posx = random.randint(0,celdas-1)
    posy = random.randint(0,celdas-1)
    posicion.append(posx)
    posicion.append(posy)

    return posicion


def dibujar_objetos(plano_completo, pos_uberx, pos_ubery, pos2x, pos2y, coste):

    plano_completo[pos_uberx][pos_ubery] = COLOR_AZUL+CHAR_UBER+COLOR_DEFECTO
    plano_completo[pos2x][pos2y] = COLOR_AMARILLO+CHAR_CLIENTE+COLOR_DEFECTO

    print(f"\n({pos_uberx}, {pos_ubery}) Coste: {coste}€ -> Buscando a cliente en ({pos2x}, {pos2y})")
    reps = 0
    heading = espacio * (heading_dis+1) + "0"
    for espacios in range(1, celdas):
        heading += espacio * heading_dis + str(espacios) 
    print(heading)
    while reps < celdas:
        dibujo_plano_fila = ""
        for k in range(0, celdas):
            dibujo_plano_fila += plano_completo[reps][k] 
        print(" ", reps, " ", dibujo_plano_fila)
        reps += 1  

def dibujar_trayecto(plano_completo, pos_uberx, pos_ubery, cliente, coste):
    plano_completo[pos_uberx][pos_ubery] = COLOR_ROJO+CHAR_UBER+COLOR_DEFECTO

    print(f"\n({pos_uberx}, {pos_ubery}) Coste: {coste}€ -> Buscando a cliente en ({cliente.destinox}, {cliente.destinoy})")
    reps = 0
    heading = espacio * (heading_dis+1) + "0"
    for espacios in range(1, celdas):
        heading += espacio * heading_dis + str(espacios) 
    print(heading)
    while reps < celdas:
        dibujo_plano_fila = ""
        for k in range(0, celdas):
            dibujo_plano_fila += plano_completo[reps][k] 
        print(" ", reps, " ", dibujo_plano_fila)
        reps += 1  

"""
def recoger_cliente():
    if coche.posx != posicion_cliente[0]:

        if coche.posx < posicion_cliente[0]:
            coche.posx += 1

        elif coche.posx > posicion_cliente[0]:
            coche.posx -= 1

    elif coche.posx == posicion_cliente[0]:

        if coche.posy < posicion_cliente[1]:
            coche.posy += 1

        elif coche.posy > posicion_cliente[1]:
            coche.posy -= 1
        
        else:
            pass
"""


# print(posicion_uber, posicion_cliente)
# dibujar_objetos(posicion_uber, posicion_cliente)
#print(coche.posx)


