#Classe nó que será usada para criação da árvore
class No(object):
    def __init__(self, esquerda=None, direita=None):
        self.esquerda = esquerda
        self.direita = direita

    def filhos(self):
        #Retorna os filhos do nó como uma tupla contendo o filho esquerdo e o filho direito
        return self.esquerda, self.direita

    def __str__(self):
        #Retorna uma representação em string do nó, que é a concatenação das representações em string do filho esquerdo e do filho direito.
        return self.esquerda, self.direita

def criar_arvore(nos):
    while len(nos) > 1:
        #Seleciona os dois nós com menor valor 
        (chave1, valor1) = nos[-1]
        (chave2, valor2) = nos[-2]
        nos = nos[:-2]
        #Cria nó auxiliar com nós selcionados como filhos
        no = No(chave1, chave2)
        nos.append((no, valor1 + valor2)) #valor nó aux. = soma dos dois selecionados
        nos = sorted(nos, key=lambda x: x[1], reverse=True)
    return nos[0][0]

def codificar_arvore(no, string_binaria=''):
    if type(no) is str:
        return {no: string_binaria}
    (esquerda, direita) = no.filhos()
    dicionario = dict() #cria dicionário
    dicionario.update(codificar_arvore(esquerda, string_binaria + '0'))
    dicionario.update(codificar_arvore(direita, string_binaria + '1'))
    
    #Retorna um dicionário no formato 'caractere' : 'bin'
    return dicionario
