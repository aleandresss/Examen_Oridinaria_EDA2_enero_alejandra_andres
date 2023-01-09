"""1.creo un arbol de Huffman
    2.creo la tabla de codigos
    3. comprimo y descomprimo el mensaje
"""

from collenctions import defaultdict 
import heapq

def arbol_Huffman(frec): 
    heap [[peso, [simbolo, ""]] for simbolo, peso in frec.items()]
        heapq.heapify
