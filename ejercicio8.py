"""1.creo un arbol de Huffman
    2.creo la tabla de codigos
    3. comprimo y descomprimo el mensaje
"""

from collenctions import defaultdict 
import heapq

def arbol_Huffman(frec): 
    heap [[peso, [simbolo, ""]] for simbolo, peso in frec.items()]
        heapq.heapify(heap)
            while len(heap)>1
            menor = heapq.heappop(heap)
            mayor = heapq.heappop(heap)
            for par in menor[1]:
                pair[1] = '0' + par[1]
            for par in mayor [1]:
                pair[1] = '1' + par [1]
        heapq.heappush(heap, [menor[0] + mayor[0]] + menor[1:] + mayor[1:])
        return heap

def codigo_huffman(frec):
    heap = arbol_huffman(frec)
        codigos = {}

def comprimir (mensaje,frec):
    codigos = codigoshuffman(frec)

def descomprimir (mensaje,frec):
    codigos
    mensaje = ""
    
    i = 0
    while i < len(comp)




