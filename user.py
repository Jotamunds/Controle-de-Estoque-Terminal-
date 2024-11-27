import sqlite3

def main():
    escolhas()

def escolhas():
    while True:
        # Variáveis
        caminho_banco = r'C:\Users\jotin\OneDrive\Documentos\João Gabriel\programacao\Python\dados\sql_lite\controle_de_estoque\controle_de_estoque.db'
        conexao = sqlite3.connect(caminho_banco)
        conexao.execute("PRAGMA journal_mode=WAL;") # não cria o arquivo db-journal
        cursor = conexao.cursor()

        # Sistema
        print("----- USUÁRIO CONECTADO -----")
        print("1 - Mostrar dados")
        print("2 - Sair")
        escolha = int(input("Escolha: "))
        print()
        
        if escolha == 1:
            mostrar_dados(cursor, conexao)
        elif escolha == 2:
            print("Saindo do programa...")
            print()
            break
        else:
            print("ERRO - Opção inválida")
            print()
            break


def mostrar_dados(cursor, conexao):
    cursor.execute("SELECT * FROM Produtos")
    conexao.commit()
    produtos = cursor.fetchall()

    # Tabela
    print(f"{'ID':<5} {'Produto':<30} {'Preço':<10}") # :<20 deixa os elementos no canto esquerdo da tela com 20 de distância
    print("-" * 40)

    # Exibir os dados
    for produto in produtos:
        print(f"{produto[0]:<5} {produto[1]:<30} {produto[2]:<10.2f}")
    print()