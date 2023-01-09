#sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
def usar_la_fuerza (mochila,objeto,sable_luz)
    class pila:
        def __init__(self):
            self.objetos = objetos 

        def extraer (self)
        if len(self.objetos)>0: 
            self.fichas.pop(0)
                if objeto == sable_luz or objeto==mochila[0]:
                    return objeto


#Determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;



#Utilizar una lista para representar la mochila.
mochila = ["objetovalioso1","objetovalioso2","objetovalioso2"]
cant_objetosfuera = usar_la_fuerza (mochila)
print ("se han sacado una cantidad de objetos de",cant_objetosfuera)

