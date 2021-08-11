lista = [2, 4, 1, 7, 9]
print("tamanho da lista: ", len(lista))
print(lista)
print(lista[0])
print(lista[2])
print(lista[::-1])

print("\n")

# lista = [2, 4, 1, 7, 9]
for numero in lista:# for i in range [...]
    print(numero)

print("--------------------------------------------")
# a lista pode receber diferentes datatypes
lista2 = [2.8, 4, "FIAP"]
print("\n")

print("Tamanho da lista:", len(lista2))
print(lista2)
print("\n")

for i in lista2:
    print(i)
print("\n")

print("Aqui adicionaos um elemento com .append")
lista2.append("2021")
print("Tamanho da lista: ", len(lista2))

print("\n")

print("Aqui excluimos o item 1 da lista2")
del lista2[1]
print("Tamanho da lista: ",len(lista2))

for i in lista2:
    print(i)

print("---------------------------------------------")

#receber valores numa lista
lista_nomes = []
lista_idades = []

for i in range(5):
    lista_nomes.append(input("Digite seu nome: "))
    lista_idades.append(int(input("Digite sua idade: ")))

print("Pessoas com mais de 18 anos: ")

for i in range(5):
    if(lista_idades[i]>18):
        print(lista_nomes[i])
