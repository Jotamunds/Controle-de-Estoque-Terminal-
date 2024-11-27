import admin
import user
from time import sleep

def main():
    login_sistema()

def login_sistema():
    usuario_admin = "admin"
    usuario_user = "user"
    senha_admin = "1234"
    senha_user = "4321"

    while True:
        print("----- CONTROLE DE ESTOQUE -----")
        print("LOGIN E SENHA (digite 'sair' para sair)")
        login = input("Usuario: ")

        if login == usuario_admin:
            senha = input("Senha: ")
            if senha == senha_admin:
                print("ACESSANDO...")
                sleep(2)
                print()
                admin.main()
            else:
                print("Senha incorreta")
                print()
            
        elif login == usuario_user:
            senha = input("Senha: ")
            if senha == senha_user:
                print("ACESSANDO...")
                sleep(2)
                print()
                user.main()
            else:
                print("Senha incorreta")
                print()
            
        elif login == "sair":
            print("Saindo do programa...")
            print()
            break
        else:
            print("ERRO = Usuário inexistente")
            print()


if __name__ == "__main__":
    main()
