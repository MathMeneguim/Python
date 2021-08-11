#Bem vindo(a) a aula 14 de Python! Aqui testaremos as tuplas, duplas e (talvez) funcoes. Continuaremos os estudos em python depois de tanto tempo.

print ("Esta e a aula 14 de python, escolha a opcao que deseja rodar: ")

escolha = (int(input("1 - Crie uma tupla de números inteiros positivos com valores que você quiser, no mínimo 15 valores. \n2 - Imprima todos os números da tupla anterior na tela, um de cada vez. \n3 - Faça uma função que recebe uma tupla de números inteiros e retorna o maior valor contido dentro da tupla. \n4 - Faça uma função que recebe uma tupla de números reais e retorna a média aritmética de todos os valores contidos dentro da tupla.\n5 - Faça uma função que recebe uma tupla de Strings e retorna a maior String de todos os valores contidos dentro da tupla. ")))

if (escolha == 1):
#como criar uma tupla >>>
	numeros = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20', '30', '40', '50')
#criar tupla com funcao tuple()
#numeros = '123456789'
#numeros = tuple(numeros)
#print(numeros) #('1', '2', '3', '4', '5', '6', '7', '8', '9')
	for n in numeros:
		print (n)

elif (escolha == 3):
	def maior_tupla	(tupla):
		maior_numero = max(tupla)
		return maior_numero

	tupla_teste = (15, 8, 1997, 21, 9, 2003)

	print("Maior numero na tupla:", maior_tupla(tupla_teste))

elif (escolha == 4):
	def media(tupla):	 
		media_tupla = (sum(tupla) / len(tupla))
		return media_tupla
	
	tupla_aleatoria = (50, 60, 75, 35, 80)
	print("Media da tupla aleatoria: ", media(tupla_aleatoria))
#elif (escolha == 5): #Error
	#def maior_string(tupla):
	#	for n in tupla:
	#		string = (max(len(n)))
	#		return string		
	
	#tupla_random = ('Meu','Nome','eh','Matheus',) 
	#print ("maior string", maior_string(tupla_random))
#	meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho']
#	
#	meses_ordenados = sorted(meses, reverse=True)
#	#print (max(len(meses_list)))
#	
#	print (meses_ordenados)
#	for n in meses: 
#		lista_letras = list (n)	
#		lista_numeros = len(n)
#		print (lista_letras)
#		
#		meses_list = list(str(lista_numeros))
#		for i in meses_list:
#			print (i)
#			receber_meses = []
#			receber_meses.append 
#	print (receber_meses)	
		#printar os valores do lista_numeros em outra lista, a partir dai verificar o maior numero
		#maior_numero = max(lista_numeros)
		#print (maior_numero)
		
		#print(max(len(n)))
		
		
elif (escoha == 6):
	

else :
	print ("ainda nao terminado")
