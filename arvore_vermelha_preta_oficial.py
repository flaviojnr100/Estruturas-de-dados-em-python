
class ArvoreRB:
    def __init__(self):
        self.__none = self.No(None)
        self.__none.pai = self.__none
        self.__none.esquerda = self.__none
        self.__none.direita = self.__none
        self.__none.cor = 'black'
        self.__root = self.__none

    class No:
        def __init__(self, chave):

            self.chave = chave
            self.cor = 'red'
            self.pai = None
            self.esquerda = None
            self.direita = None




    def getRoot(self):
        return self.__root



    def maximo(self, x):
        while x.direita != self.__none:
            x = x.direita
        return x

    def minimo(self, x):
        while x.esquerda != self.__none:
            x = x.esquerda
        return x

    def sucessor(self, x):
        if x.direita != self.__none:
            return self.minimo(x.direita)
        y = x.pai
        while y != self.__none and x == y.direita:
            x = y
            y = y.pai
        return y

    def antecessor(self, x):
        if x.esquerda != self.__none:
            return self.maximo(x.esquerda)
        y = x.pai
        while y != self.__none and x == y.esquerda:
            x = y
            y = y.pai
        return y

    def rotateLeft(self, x):
        y = x.direita
        x.direita = y.esquerda
        if y.esquerda != self.__none:
            y.esquerda.pai = x
        y.pai = x.pai
        if x.pai == self.__none:
            self.__root = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
        y.esquerda = x
        x.pai = y

    def rotateRight(self, x):
        y = x.esquerda
        x.esquerda = y.direita
        if y.direita != self.__none:
            y.direita.pai = x
        y.pai = x.pai
        if x.pai == self.__none:
            self.__root = y
        elif x == x.pai.direita:
            x.pai.direita = y
        else:
            x.pai.esquerda = y
        y.direita = x
        x.pai = y

    def RBinsert(self, z):
        z = self.No(z)
        y = self.__none
        x = self.__root
        while x != self.__none:
            y = x
            if z.chave < x.chave:
                x = x.esquerda
            else:
                x = x.direita
        z.pai = y
        if y == self.__none:
            self.__root = z
        elif z.chave < y.chave:
            y.esquerda = z
        else:
            y.direita = z
        z.esquerda = self.__none
        z.direita = self.__none
        z.cor = 'red'
        self.insertFixUp(z)

    def insertFixUp(self, z):
        while z.pai.cor == 'red':
            if z.pai == z.pai.pai.esquerda:
                y = z.pai.pai.pai
                if y.cor == 'red':
                    z.pai.cor = 'black'
                    y.cor = 'black'
                    z.pai.pai.cor = 'red'
                    z = z.pai.pai
                else:
                    if z == z.pai.direita:
                        z = z.pai
                        self.rotateLeft(z)
                    z.pai.cor = 'black'
                    z.pai.pai.cor = 'red'
                    self.rotateRight(z.pai.pai)
            else:
                y = z.pai.pai.esquerda
                if y.cor == 'red':
                    z.pai.cor = 'black'
                    y.cor = 'black'
                    z.pai.pai.cor = 'red'
                    z = z.pai.pai
                else:
                    if z == z.pai.esquerda:
                        z = z.pai
                        self.rotateRight(z)
                    z.pai.cor = 'black'
                    z.pai.pai.cor = 'red'
                    self.rotateLeft(z.pai.pai)
        self.__root.cor = 'black'

    def RBdelete(self, z):
        if z.esquerda == self.__none or z.direita == self.__none:
            y = z
        else:
            y = self.sucessor(z)
        if y.esquerda != self.__none:
            x = y.esquerda
        else:
            x = y.direita
        x.pai = y.pai
        if y.pai == self.__none:
            self.__root = x
        else:
            if y == y.pai.esquerda:
                y.pai.esquerda = x
            else:
                y.pai.direita = x
        if y != z:
            z.chave = y.chave
        if y.cor == 'black':
            self.deleteFixUp(x)
        return y

    def deleteFixUp(self, x):
        while x != self.__root and x.cor == 'black':
            if x == x.pai.esquerda:
                w = x.pai.direita
                if w.cor == 'red':
                    w.cor = 'black'
                    x.pai.cor = 'red'
                    self.rotateLeft(x.pai)
                    w = x.pai.direita
                if w.esquerda.cor == 'black' and w.direita.cor == 'black':
                    w.cor = 'red'
                    x = x.pai
                else:
                    if w.direita.cor == 'black':
                        w.esquerda.cor = 'black'
                        w.cor = 'red'
                        self.rotateRight(w)
                        w = x.pai.direita
                    w.cor = x.pai.cor
                    x.pai.cor = 'black'
                    w.direita.cor = 'black'
                    self.rotateLeft(x.pai)
                    x = self.__root
            else:
                w = x.pai.esquerda
                if w.cor == 'red':
                    w.cor = 'black'
                    x.pai.cor = 'red'
                    self.rotateRight(x.pai)
                    w = x.pai.esquerda
                if w.direita.cor == 'black' and w.esquerda.cor == 'black':
                    w.cor = 'red'
                    x = x.pai
                else:
                    if w.esquerda.cor == 'black':
                        w.direita.cor = 'black'
                        w.cor = 'red'
                        self.rotateLeft(w)
                        w = x.pai.esquerda
                    w.cor = x.pai.cor
                    x.pai.cor = 'black'
                    w.esquerda.cor = 'black'
                    self.rotateRight(x.pai)
                    x = self.__root
        x.cor = 'black'

    def percorrerEmOrdem(self, x):
        if x != self.__none:
            self.percorrerEmOrdem(x.esquerda)
            print(x.chave)
            self.percorrerEmOrdem(x.direita)

    def buscar(self, valor):
        x = self.__root
        while (x != self.__none) and (valor != x.chave):
            if valor > x.chave:
                x = x.direita
            else:
                x = x.esquerda
        return x


a = ArvoreRB()
a.RBinsert(10)
a.RBinsert(20)
a.RBinsert(30)
a.RBinsert(40)
a.percorrerEmOrdem(a.getRoot())