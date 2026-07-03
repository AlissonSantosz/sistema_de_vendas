estoque_produtos = {
    1: { "nome": "Jaquetas", "preco": 350.00, "quantidade": 50 },
    2: { "nome": "Tenis", "preco": 250.00, "quantidade": 20 },
    3: { "nome": "Calças", "preco": 150, "quantidade": 15}
    }

carrinho = []

while True:

    print("*"*30)
    print("Seja Bem Vindo na minha loja")
    print("*"*30)
    print("[1] Vizualizar estoque.")
    print("[2] Adicionar item ao carrinho.")
    print("[3] Vizualizar Carrinho.")
    print("[4] Finalizar Compra.")
    print("[5] Sair do sistema.")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("ID | NOME | VALOR | QUANTIDADE")
        for chave, valor in estoque_produtos.items():
            print(f"{chave}:{valor}")

    elif opcao == 2:
        print("Adiconar item ao carrinho!")
        id_produto = int(input("Qual ID do produto voçe deseja comprar? "))
        if id_produto in estoque_produtos:
           qtd_produto = int(input("Quantas unifdades voçe deseja?"))
           if qtd_produto <= 0:
              print("Quantidade inválida!")
           elif qtd_produto <= estoque_produtos[id_produto]["quantidade"]:
                item = {
                    "qtd" : qtd_produto,
                    "nome" : estoque_produtos[id_produto]["nome"],
                    "preco" : estoque_produtos[id_produto]["preco"],
                    "preco_total": qtd_produto * estoque_produtos[id_produto]["preco"]
                }
                carrinho.append(item)
                estoque_produtos[id_produto]["quantidade"] -= qtd_produto
                print(item)
           else:
               print(f"Quantidade indisponivel, temos apenas {estoque_produtos[id_produto]["quantidade"]} no estoque.")

        else:
            print("Id informado não existe no estoque!")


    elif opcao == 3:
        if carrinho:
            print(" Vizualizar Carrinho!")
            subtotal = 0
            for i in carrinho:
                print (f"{i["qtd"]}x {i["nome"]} no valor de R$ {i["preco"]}(cada)\nTotal R${i["preco_total"]}")
                subtotal += i["preco_total"]
                print(f"Subtotal da Compra R${subtotal}")
        else:
             print("Carrinho Vazio!")



    elif opcao == 4:
        print("Finalizar compra!")

    elif opcao == 0:
        print("Sair do sistema...")
        break