print("** MINI SISTEMA DE USUÁRIO **\n")

def cadastro_new_user():
    print("CADASTRO DE NOVOS USUÁRIOS: \n")
    new_username = input("Digite seu username: ")
    new_password = input("Olá", new_username, "!Digite sua nova senha: ")

    nova_senha = input(new_username, ", Confirme sua senha: ")

    while new_password != nova_senha:
     new_password = input("Tente novamente! Digite sua nova senha: ")
    print("Olá, ", new_username, ". Você foi cadastrado!")

def definir_opcao(){
opicao_inical = int(input("Digite 1 para fazer LOGIN ou Digite 2 para CADASTRO: \n"))
if opcao_inicial == 1 or opcao_inicial == 2: # type: ignore
    if opcao_inicial == 1:
    user_cadastrado()

    else:
        cadastro_new_user()
else:
    print("Opção não encontrada! Tente novamente mais tarde.")
}

