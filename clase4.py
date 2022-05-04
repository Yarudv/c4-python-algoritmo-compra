import sched
import time
stock_producto_1 = 120
stock_producto_2 = 150
contador = 0

def controltime(tiempo, mensaje):
    cada_cuanto = sched.scheduler(time.time, time.sleep)
    cada_cuanto.enterabs(tiempo,1,print,argument=(mensaje,))
    print("Bienvenidos")
    cada_cuanto.run()

while True: 
    controltime(time.time()+3,"Ejecutando aplicación de compra")
    compra_producto = int(input("¿Qué producto desea comprar? (1/2):"))
    if compra_producto == 1:
        cantidad_1 = int(input("Ingrese cantidad a comprar del producto_1: " ))
        stock_producto_1 = stock_producto_1 - cantidad_1
        print(stock_producto_1)
        if stock_producto_1 <= 100:
            acu1 = stock_producto_1 + 50
            stock_producto_1 = acu1
    else:
        cantidad_2 = int(input("Ingrese cantidad a comprar del producto_2: " ))
        stock_producto_2 = stock_producto_2 -cantidad_2
        print(stock_producto_2)
        if stock_producto_2 <= 100:
            acu2 = stock_producto_2 + 50
            stock_producto_2 = acu2
    contador = contador + 1
    if contador >= 10:
        print("Stock producto_1 es:",stock_producto_1)
        print("Stock producto_2 es:",stock_producto_2)         
       




