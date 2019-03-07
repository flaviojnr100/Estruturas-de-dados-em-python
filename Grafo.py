class Grafo:
    def __init__(self):
        self.__tamanho_maximo = 20
        self.__totalvertices = 0
        self.__listavertices = []
        self.__matrizadjacencia = []
        for i in range(self.__tamanho_maximo):
            linhamatriz = []
            for j in range(self.__tamanho_maximo):
                linhamatriz.append(0)
            self.__matrizadjacencia.append(linhamatriz)
    class Vertice:
        def __init__(self,rotulo):
            self.rotulo = rotulo
            self.visitado = False

        def igual(self,r):
            return r==self.rotulo
        def obtemvisitado(self):
            return self.visitado
        def foivisitado(self):
            self.visitado = True
        def limpar(self):
            self.visitado = False

    def retornarIndice(self,vertice):
        for y,i in enumerate(self.__listavertices):
            if i.rotulo == vertice:
                return y
        return -1
    def adicionarVertice(self,rotulo):
        self.__totalvertices+=1
        self.__listavertices.append(self.Vertice(rotulo))
    def adicionarArco(self,inicio,fim):
        self.__matrizadjacencia[inicio][fim] = 1
        self.__matrizadjacencia[fim][inicio] = 1

    def ImprimirMatriz(self):
        print(" ",end=" ")
        for y,i in enumerate(self.__listavertices):
            if y==self.__totalvertices-1:
                print(i.rotulo)
            else:
                print(i.rotulo,end=" ")

        for i in range(self.__totalvertices):
            print(self.__listavertices[i].rotulo,end=" ")
            for j in range(self.__totalvertices):
                print(self.__matrizadjacencia[i][j],end=" ")
            print()

    def obtemadjacentenaovisitado(self,vertice):
        for i in range(self.__totalvertices):
            if self.__matrizadjacencia[vertice][i] == 1 and self.__listavertices[i].visitado == False:
                return i
        return -1

    def Busca_profundidade(self,inicio,fim):
        pilha = []
        self.__listavertices[inicio].foivisitado()
        pilha.append(inicio)
        while len(pilha)!=0:
            elementoanalisar = pilha[len(pilha)-1]
            if elementoanalisar ==fim:
                print("Meta encontrado, o caminho é: ",end=" ")
                for i in pilha:
                    print(self.__listavertices[i].rotulo,end=", ")
                print()
                break
            v = self.obtemadjacentenaovisitado(elementoanalisar)
            if v==-1:
                pilha.pop()
            else:
                self.__listavertices[v].foivisitado()
                pilha.append(v)
        else:
            print("Caminho não encontrado. Busca sem sucesso!!")
        for i in self.__listavertices:
            i.limpar()


grafo = Grafo()

grafo.adicionarVertice("A")
grafo.adicionarVertice("B")
grafo.adicionarVertice("C")
grafo.adicionarArco(0,1)
grafo.adicionarArco(0,2)
grafo.adicionarArco(2,2)
grafo.Busca_profundidade(0,2)
