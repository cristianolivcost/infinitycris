usuario_correto = "admin"
senha_correta = "1234"

tentativas_max = 3

for tentativa in range(1, tentativas_max + 1):
    usuario = input("Digite o nome de usuario: ")
    senha = input("Digite a senha: ")
    if usuario == usuario_correto and senha == senha_correta: 
        print("Bem-vindo, você fez login com sucesso!")
        break
    else:
        tentativa_restantes = tentativas_max - tentativa
        if tentativa_restantes > 0:
           print(f"Credenciais incorretas. Você ainda tem {tentativa_restantes} tentativa(s). ")
        else:
            print("Você exedeu o número de tentativas.")
            for _ in range(3):
                print("Acesso bloqueado.")
