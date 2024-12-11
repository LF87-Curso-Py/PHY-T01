import time

tempo = 3600

for i in range (tempo,-1, -1):
    print("\r",end = f"{i//3600}:{i//60}:{i%60}")
    time.sleep(0.1)
#
# # Tabuada
# numero = int(input("Insira um numero para calcular a tabuada: "))
# for i in range (1,11):
#     print(numero * i)
#