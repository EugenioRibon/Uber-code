import time
import random
from Funciones import mostrar_leyenda, crear_ciudad, dibujar_ciudad, posicionar_objetos, dibujar_objetos, Coche, Cliente, dibujar_trayecto


mostrar_leyenda()
plano_completo = crear_ciudad()
dibujar_ciudad(plano_completo)
posicion_uber = posicionar_objetos()
posicion_cliente = posicionar_objetos()
coche = Coche(posicion_uber[0], posicion_uber[1], 5)
dibujar_objetos(plano_completo, coche.posx, coche.posy, posicion_cliente[0], posicion_cliente[1], coche.coste)
cliente = Cliente(posicion_cliente[0], posicion_cliente[1])
while coche.posx != cliente.posx or coche.posy != cliente.posy:
    time.sleep(1)
    plano_completo = crear_ciudad()
    coche.buscar_cliente(cliente)
    dibujar_objetos(plano_completo, coche.posx, coche.posy, cliente.posx, cliente.posy, coche.coste)

plano_completo = crear_ciudad()
dibujar_trayecto(plano_completo, coche.posx, coche.posy, cliente, coche.coste)

while coche.posx != cliente.destinox or coche.posy != cliente.destinoy:
    time.sleep(1)
    coche.llevar_cliente(cliente)
    plano_completo = crear_ciudad()
    dibujar_trayecto(plano_completo, coche.posx, coche.posy, cliente, coche.coste)

print(f"\n ({coche.posx}, {coche.posy}) Coste: {coche.coste}€ -> Fin del servicio ")

