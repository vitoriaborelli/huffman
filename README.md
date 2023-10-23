# Huffman
Implementação do Código de Huffman, algoritmo utilizado como estratégia para codificar conjuntos de dados já existentes, visando diminuir a média da quantidade de bits utilizada convencionalmente para representá-los, ou seja, comprimindo-os.

São dadas as frequências (ou probabilidades) de aparição de cada elemento, de modo a criar com eles uma árvore binária e, a partir dela, definir os códigos binários correspondentes de acordo com o caminho percorrido da raiz até a respectiva folha que armazena o elemento em questão. Dessa forma, os elementos com maior probabilidade de aparição possuirão um código com menos bits, diminuindo a quantidade média de bits utilizados ao utilizar tais dados.

Sendo assim, ele se mostra mais eficiente que uma codificação padrão, pois, associado ao alfabeto usado, também há uma lista ω de tamanho igual a lista ∝, onde as respectivas probabilidades de ocorrência de cada elemento ∝i são armazenadas. Logo, por meio dessas listas associadas, o algoritmo gera códigos binários de tamanho variável, de forma com que quanto menor ωi, maior len(∝i), que é o comprimento do elemento após ser codificado.
