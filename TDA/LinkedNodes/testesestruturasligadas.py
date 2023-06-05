
from LinkedNodes.node import Node
n1 = Node(4)
n2 = Node(7, n1)

# a.	Crie um objeto head do tipo Node sem elementos.
head: Node = None
print(head)

# b.	Acrescente a head a sequência de nós com valores entre 1 e 9.
for i in range(1, 10):
    head = Node(i, head)

# c.	Itere sobre a sequência construída em b, mostrando o valor de cada nó no ecrã
print(head.get_data())
print(head.get_next().get_data())
print(head.get_next().get_next().get_data())
print()
aux = head
while aux != None:
    print(aux.get_data())
    aux = aux.get_next()
print()
print(head.get_data())

# d.	Acrescente no início da sequência um nó com o valor 10 e no fim o nó com valor 0.

# e.	Insira o valor 20 na 2.ª posição.

# f.	Remova o primeiro elemento e o último
 
# g.	Remova o elemento da 2.ª posição.

# h.	Indique o número de elementos da sequência
 
# i.	Indique o valor se encontra na posição 4
 

# j.	Altere o valor do elemento da posição 5 para 100
 
# k.	Troque os valores das posições x e y, em que x<y
