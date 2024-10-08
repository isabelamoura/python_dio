def cadastro():
    # Solicita as informações do usuário
    nome = input("Digite seu nome completo: ")
    cpf = input("Digite seu CPF: ")
    telefone = input("Digite seu número de telefone: ")

    # Informa que o cadastro foi realizado com sucesso
    print("\nCadastro realizado com sucesso!")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Telefone: {telefone}")

# Chama a função para executar o cadastro
cadastro()
