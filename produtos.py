PRODUTOS = {'Leite': {
    'preco': 2.99,
    'categoria': 'Bebidas',
    'quantidade': 10,
}, 'Farinha': {
    'preco': 5.40,
    'categoria': 'Ingredientes',
    'quantidade': 4,
}}


def listar_todos():
    if PRODUTOS:
        for produto in PRODUTOS:
            listar_produto(produto)
    else:
        print()
        print('*Nenhum produto cadastrado!*')
        print()


def listar_produto(produto):
    try:
        print('=========================================')
        print(produto)
        print('Preço:', PRODUTOS[produto]['preco'])
        print('Categoria:', PRODUTOS[produto]['categoria'])
        print('Quantidade:', PRODUTOS[produto]['quantidade'])
        print('=========================================')
    except KeyError:
        print()
        print('*Produto não encontrado!*')
        print()
    except:
        print()
        print('*Algum erro inesperado ocorreu!*')
        print()


def incluir_editar_produto(produto):
    preco, categoria, quantidade = ler_dados()
    PRODUTOS[produto] = {
        'preco': preco,
        'categoria': categoria,
        'quantidade': quantidade
    }
    salvar()
    print()
    print('{} editado/incluido com sucesso!'.format(produto))
    print()


def ler_dados():
    preco = float(input('Informe o preço: '))
    categoria = input('Informe a categoria: ')
    quantidade = float(input('Informe a quantidade: '))
    return preco, categoria, quantidade


def excluir_produto(produto):
    try:
        PRODUTOS.pop(produto)
        print()
        print('*{} excluido com sucesso*'.format(produto))
        print()
    except KeyError:
        print()
        print('*O produto não existe!*')
        print()
    salvar()

def exportar_produtos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for produto in PRODUTOS:
                preco = PRODUTOS[produto]['preco']
                categoria = PRODUTOS[produto]['categoria']
                quantidade = PRODUTOS[produto]['quantidade']
                arquivo.write('{},{},{},{}\n'.format(produto, preco, categoria, quantidade))
        print()
        print('*Produtos exportados com sucesso*')
        print()
    except:
        print()
        print('*Algum erro inesperado ocorreu*')
        print()


def importar_produtos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                print(dados)
                nome = dados[0]
                preco = dados[1]
                categoria = dados[2]
                quantidade = dados[3]
                incluir_editar_produto(nome, preco, categoria, quantidade)
        print()
        print('*Produtos importados com sucesso*')
        print()
    except FileNotFoundError:
        print()
        print('*Arquivo não encontrado*')
        print()


def salvar():
    exportar_produtos('database.csv')


def importar():
    importar_produtos('database.csv')


def mostrar_menu():
    print('=========================================')
    print('1 - Mostrar todos produtos')
    print('2 - Buscar produto')
    print('3 - Incluir produto')
    print('4 - Editar produto')
    print('5 - Excluir produto')
    print('6 - Exportar produtos para CSV')
    print('7 - Importar produtos CSV')
    print('0 - Sair do programa')
    print('=========================================')


importar()
while True:
    mostrar_menu()
    opcao = input('Informe a opção selecionada: ')

    if opcao == '1':
        listar_todos()
    elif opcao == '2':
        produto = input('Informe o nome do produto: ')
        listar_produto(produto)
    elif opcao == '3':
        produto = input('Informe o nome do produto: ')
        try:
            PRODUTOS[produto]
            listar_produto(produto)
            escolha = input('O produto já existe, deseja editá-lo? ').lower()
            if escolha == 's':
                incluir_editar_produto(produto)
        except KeyError:
            incluir_editar_produto(produto)
    elif opcao == '4':
        produto = input('Informe o nome do produto: ')
        try:
            PRODUTOS[produto]
            preco, categoria, quantidade = ler_dados()
            incluir_editar_produto(produto, preco, categoria, quantidade)
        except KeyError:
            escolha = input('O produto não existe, deseja adicioná-lo? ').lower()
            if escolha == 's':
                preco, categoria, quantidade = ler_dados()
                incluir_editar_produto(produto, preco, categoria, quantidade)
    elif opcao == '5':
        produto = input('Informe o nome do produto: ')
        excluir_produto(produto)
    elif opcao == '6':
        exportar_produtos()
    elif opcao == '7':
        arquivo = input('Informe o nome do arquivo: ')
        importar_produtos(arquivo)
    elif opcao == '0':
        print('*Saindo do programa*')
        break
    else:
        print()
        print('*Informe uma opção válida!*')
        print()
