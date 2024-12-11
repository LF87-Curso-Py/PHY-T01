# import time
# tempo = 3600
#
# while tempo > -1:
#     print("\r",end = f"{tempo//3600}:{tempo//60}:{tempo%60}")
#     time.sleep(0.1)
#     tempo -= 1
#
#
# while True:
#     email = input("Insira um email válido: ")
#
#     if email[-4:] != ".com":
#         print("Falta o .com")
#         continue
#     else:
#         print("Bem-vindo")
#         break

acesso = "Thiago_001"
controle_acesso = False
contador = 0

while not controle_acesso:

    if contador < 3:
        chave_acesso = input("Informe sua credencial: ")
        contador += 1

        if chave_acesso == acesso:
            chave_acesso = True
            print("Acesso autorizado")
            break
        else:
            continue

    else:
        print("Já era!")
        break