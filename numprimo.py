a = int(input("Informe um número: "))

qtd = 0

for x in range(1, a + 1):
	resto = a % x
	if resto == 0:
		qtd += 1
if qtd == 2:
	print("O número {} é primo".format(a))

else:
	print("O número {} não é primo".format(a))
