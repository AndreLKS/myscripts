import random

num = random.randint(1, 100)
while True:
	n = int(input("Digite um número: "))
	if n > num:
		print('Mais para baixo')
	elif n < num:
		print('Mais para cima')
	else:
		print('ACERTOU!!!')
		break
print('Jogo finalizado!')
