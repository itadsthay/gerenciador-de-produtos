from datetime import datetime

# Lista que armazena os produtos
produtos = []

# Menu principal
def menu():
    print(" Gerenciador de Produtos ".center(100, ' '))
    print("\t1 - Cadastrar produto")
    print("\t2 - Remover produto")
    print("\t3 - Procurar produto")
    print("\t4 - Ver produtos")
    print("\t5 - Sair")

# Função para adicionar produtos
def adicionar_produto():
    print("Quantos produtos deseja adicionar?")
    num = int(input('>> '))
    for i in range(1, num + 1):
        data = datetime.now().strftime("%d/%m/%Y")
        nome = input("Nome: ")
        estoque = int(input("Quantidade em estoque: "))
        preco = float(input("Preço: "))
        descricao = input("Descrição do produto: ")
        produtos.append([nome, estoque, preco, data, descricao])

# Função para remover um produto
def remover_produto():
    if len(produtos) > 0:
        nome = input("Digite o nome do produto que deseja remover: ")
        for produto in produtos:
            if nome == produto[0]:
                produtos.remove(produto)
                print(f'O produto {nome.lower()} foi removido.')
                return
        print('Produto não encontrado.')
    else:
        print("Não há produtos cadastrados.")

# Função para procurar um produto específico
def procurar_produto():
    if len(produtos) > 0:
        nome = input("Qual produto deseja pesquisar? ")
        for produto in produtos:
            if nome == produto[0]:
                print(f'Nome: {produto[0]}')
                print(f'Preço: R$ {produto[2]}')
                print(f'Estoque: {produto[1]}')
                return
        print('Produto não encontrado.')
    else:
        print("Não há produtos cadastrados.")

# Função para exibir todos os produtos
def ver_produtos():
    if len(produtos) > 0:
        for produto in produtos:
            print()
            print(f'Nome: {produto[0]}')
            print(f'Estoque: {produto[1]}')
            print(f'Preço: R$ {produto[2]}')
            print(f'Descrição: {produto[4]}')
            print(f'Data de registro: {produto[3]}')
            print()
        print(f'Total de produtos cadastrados: {len(produtos)}')
    else:
        print("Não há produtos cadastrados.")

# Função principal que controla o menu
def main():
    escolha = ''
    while escolha != '5':
        menu()
        escolha = input('>> ')
        if escolha == '1':
            adicionar_produto()
        elif escolha == '2':
            remover_produto()
        elif escolha == '3':
            procurar_produto()
        elif escolha == '4':
            ver_produtos()
        elif escolha == '5':
            print("Saindo do programa...")
        else:
            print("Opção inválida.")

# Executa o programa
if __name__ == "__main__":
    main()
