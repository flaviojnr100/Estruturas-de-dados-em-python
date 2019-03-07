
class Lista:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__iterando = None
    class No:
        def __init__(self,valor):
            self.chave = valor
            self.anterior = None
            self.proximo = None

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.__tamanho

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.__primeiro
        else:
            self.__iterando = self.__iterando.proximo
        if not self.__iterando is None:
            return self.__iterando.chave
        raise StopIteration
    def __str__(self):
        formato = "["
        atual = self.__primeiro
        i=0
        while not atual is None:
            formato+=atual.chave.__repr__()
            if i<self.__tamanho-1:
                formato+=", "
            i+=1
            atual = atual.proximo
        formato+="]"
        return formato

    def inserir(self,posicao,valor):
        novo = self.No(valor)
        if self.__primeiro is None:
            self.__primeiro = novo
            self.__ultimo = novo
        elif posicao==0:
            novo.proximo = self.__primeiro
            self.__primeiro.anterior = novo
            self.__primeiro = novo
        elif posicao==self.__tamanho:
            self.__ultimo.proximo = novo
            novo.anterior = self.__ultimo
            self.__ultimo = novo
        elif 0<posicao<self.__tamanho:
            atual = self.__primeiro
            i=0
            while i!=posicao:
                atual = atual.proximo
                i+=1
            anterior = atual.anterior
            anterior.proximo = novo
            novo.anterior = anterior
            novo.proximo = atual
            atual.anterior = novo
        else:
            raise IndexError("Erro de indice!!")
        self.__tamanho+=1
        self.__iterando = None
    def remover(self,valor):
        atual = self.__primeiro
        i = 0
        while i<self.__tamanho:
            if atual.chave == valor:
                break
            atual = atual.proximo
            i+=1
        if self.__tamanho == 0:
            raise IOError("Não há elementos na lista")
        elif i==0:
            proximo = self.__primeiro.proximo
            proximo.anterior = None
            self.__primeiro.proximo = None
            self.__primeiro = proximo
        elif i==self.__tamanho-1:
            anterior = self.__ultimo.anterior
            anterior.proximo = None
            self.__ultimo.anterior = None
            self.__ultimo = anterior
        elif i>0 and i<self.__tamanho-1:
            anterior = atual.anterior
            proximo = atual.proximo
            atual.proximo = atual.anterior = None
            anterior.proximo = proximo
            proximo.anterior = anterior
        else:
            raise IOError("Erro de valor!!")

        self.__tamanho-=1
        self.__iterando = None
    def index(self,valor):
        i=0
        atual = self.__primeiro
        while i<self.__tamanho:
            if atual.chave == valor:
                break
            i+=1
            atual = atual.proximo
        return i
    def clear(self):
        self.__primeiro = self.__ultimo = None
        self.__tamanho = 0
        self.__iterando = None

    def Pop(self,indice):
        atual = self.__primeiro
        i=0
        while i<self.__tamanho:
            if i==indice:
                break
            atual = atual.proximo
            i+=1
        self.remover(atual.chave)



lista = Lista()
lista.inserir(0,1)
lista.inserir(0,2)
lista.inserir(0,3)
lista.inserir(0,4)
lista.inserir(0,5)
lista.inserir(0,6)
lista.inserir(2,56)
print(lista)

