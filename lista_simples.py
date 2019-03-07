
class Lista:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__iterando =None
    class No:
        def __init__(self,elemento):
            self.proximo = None
            self.elemento = elemento
    def __len__(self):
        return self.__tamanho
    def __iter__(self):
        return self
    def __next__(self):

        if self.__iterando is None:
            self.__iterando = self.__primeiro
        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not None:
            return self.__iterando.elemento

        raise StopIteration
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        formato = "["
        atual = self.__primeiro
        i = 0
        while i<self.__tamanho:
            formato+=atual.elemento.__repr__()
            if i<self.__tamanho - 1:
                formato+=", "
            atual = atual.proximo
            i+=1
        formato+="]"
        return formato

    def inserir(self,indice,elemento):
        novo = self.No(elemento)
        if self.__tamanho ==0:
            self.__primeiro = self.__ultimo = novo
        elif indice == self.__tamanho:
            self.__ultimo.proximo = novo
            self.__ultimo = novo
        elif indice == 0:
            novo.proximo = self.__primeiro
            self.__primeiro = novo
        elif 0<indice<self.__tamanho:
            i = 0
            atual = self.__primeiro
            anterior = None
            while i <indice:
                anterior = atual
                atual = atual.proximo
                i+=1
            anterior.proximo = novo
            novo.proximo = atual
        else:
            raise IndexError("Indice inválido!!")
        self.__iterando = None
        self.__tamanho+=1

    def append(self,elemento):
        self.inserir(self.__tamanho,elemento)
    def inserir_inicio(self,elemento):
        self.inserir(0,elemento)

    def remover(self,elemento):

        if self.__tamanho == 0:
            raise ValueError("Não há elementos na lista")
        elif self.__tamanho == 1:
            if elemento == self.__primeiro.elemento:
                self.__primeiro = self.__ultimo = None
        elif self.__primeiro.elemento == elemento:
            proximo = self.__primeiro.proximo
            self.__primeiro.proximo = None
            self.__primeiro = proximo

        else:
            i = 0
            atual = self.__primeiro
            anterior = None
            while i<self.__tamanho:
                if atual.elemento == elemento:
                    anterior.proximo = atual.proximo
                    atual.proximo = None
                    break
                anterior = atual
                atual = atual.proximo
                i+=1



        self.__iterando = None
        self.__tamanho-=1

    def pop(self,indice):
        retorno = 0
        if self.__tamanho == 0:
            raise ValueError("Não há elementos na lista")
        elif indice == 0:
            retorno = self.__primeiro.elemento
            proximo = self.__primeiro.proximo
            self.__primeiro.proximo = None
            self.__primeiro = proximo


        elif indice == self.__tamanho-1:
            atual = self.__primeiro
            i = 0
            while i<self.__tamanho-1:
                atual = atual.proximo
                i+=1
            atual.proximo = None
            retorno = self.__ultimo.elemento
            self.__ultimo = atual
        elif 0<indice<self.__tamanho:
            i = 0
            atual = self.__primeiro
            anterior = None
            while i<indice:
                anterior = atual
                atual = atual.proximo
                i+=1
            retorno = atual.elemento
            anterior.proximo = atual.proximo
            atual.proximo = None
        else:
            raise IndexError("Indice inválido!!")
        self.__iterando = None
        self.__tamanho -= 1
        return retorno



lista = Lista()
lista.append(1)
lista.append(2)
lista.inserir(0,5)
lista.inserir(0,89)
lista.inserir_inicio(100)

for i in lista:
    print(i)
