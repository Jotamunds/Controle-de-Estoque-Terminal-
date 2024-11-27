import sqlite3

def main():
    escolhas()


def escolhas():
    while True:
        # Variáveis
        caminho_banco = r'controle_de_estoque.db'
        conexao = sqlite3.connect(caminho_banco)
        conexao.execute("PRAGMA journal_mode=WAL;")
        cursor = conexao.cursor()

        # Sistema
        print("----- ADMIN -----")
        print("1 - Adicionar dados")
        print("2 - Editar dados")
        print("3 - Remover dados")
        print("4 - Mostrar dados")
        print("5 - Sair")
        escolha = int(input("Escolha: "))
        print()

        match escolha:
            case 1:
                produto = input("Nome do produto: ")
                preco = float(input("Preço: R$ "))

                cursor.execute(f"INSERT INTO Produtos (PRODUTO, PRECO) VALUES (?, ?)", (produto, preco))
                conexao.commit()
                print("Produto adicionado com sucesso!")
                print()
            case 2:
                editar_dados(cursor, conexao)
            case 3:
                id = int(input("ID do produto: "))
                cursor.execute(f"DELETE FROM Produtos WHERE id = ?", (id,))
                conexao.commit()
                print("Produto removido com sucesso!")
                print()
            case 4:
                mostrar_dados(cursor, conexao)
            
            case 5:
                print("Saindo do ADMIN...")
                print()
                break
            case _:
                print("ERRO - Opção inválida")
                print()
                break


def editar_dados(cursor, conexao):
    id = input("ID do Produto: ")
    escolha = int(input("1 - Alterar Preço\n2 - Alterar nome\n3 - Sair\nEscolha: "))
    match escolha:
        case 1:
            novo_preco = float(input("Digite o novo preço: R$ "))
            cursor.execute(f"UPDATE Produtos SET PRECO = ? WHERE ID = ?", (novo_preco, id))
            conexao.commit()
            print("Preço alterado com sucesso!")
            print()
        case 2:
            novo_nome = (input("Digite o novo nome: "))
            cursor.execute(f"UPDATE Produtos SET PRODUTO = ? WHERE ID = ?", (novo_nome, id))
            conexao.commit()
            print("Nome alterado com sucesso!")
            print()
        case 3:
            print("Saindo do ADMIN...")
            print()
        case _:
            print("ERRO - OPÇÃO INVÁLIDA")
            print()


def mostrar_dados(cursor, conexao):
    cursor.execute("SELECT * FROM Produtos")
    conexao.commit()
    produtos = cursor.fetchall()

    # Tabela
    print(f"{'ID':<5} {'Produto':<30} {'Preço':<10}")
    print("-" * 40)

    # Exibir os dados
    for produto in produtos:
        print(f"{produto[0]:<5} {produto[1]:<30} {produto[2]:<10.2f}")
    print()
