
from random import shuffle
class Heap:
    def __init__(self,heap=None):
        if heap is None:
            self.__heap = []
        else:
            self.__heap = heap

    def __getitem__(self,i):
        return  self.__heap[i]

    def __len__(self):
        return len(self.__heap)
    def __str__(self):
        return self.__heap.__str__()

    @property
    def heap(self):
        return self.__heap
    @heap.setter
    def heap(self, obj):
        self.__heap = list(obj)

    def pai(self, i):
        _pai = (i-1)/2

        return int(_pai) if _pai>=0 else None

    def esquerda(self,i):
        _esquerda = (2 * i)+1
        return  _esquerda if _esquerda <len(self) else None
    def direita(self,i):
        _direita = (2*i +1)+1
        return _direita if _direita <len(self) else None

    def construir_heap(self):
        i = (len(self)//2) -1
        while i>=0:
            self.heapfy(i)
            i-=1

    def heapfy(self,i):
        e = self.esquerda(i)
        d = self.direita(i)

        if not e is None and self[e]> self[i]:
            maior = e

        else:
            maior = i

        if not d is None and self[d]>self[maior]:
            maior = d

        if maior!=i:
            self.__heap[i],self.__heap[maior] = self.__heap[maior],self.__heap[i]

            self.heapfy(maior)

v = list(range(0,5))
shuffle(v)

heap = Heap(v)
heap.construir_heap()
print(v)



