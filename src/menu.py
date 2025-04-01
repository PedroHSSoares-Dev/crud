from crud import conferir_usuario, criar_usuario

while True:
    print("\n===== MENU =====")
    print("1. Fazer login")
    print("2. Criar usuário")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuario = input("Usuário: ").strip()
        senha = input("Senha: ").strip()
        
        if conferir_usuario(usuario, senha):
            print("\nLogin realizado com sucesso!")
            print(f"Bem-vindo, {usuario}!")
        else:
            print("\nFalha no login. Verifique seus dados.")

    elif opcao == "2":
        novo_usuario = input("Novo usuário: ").strip()
        nova_senha = input("Nova senha: ").strip()
        
        if not novo_usuario or not nova_senha:
            print("Usuário e senha não podem estar vazios!")
            continue
            
        if criar_usuario(novo_usuario, nova_senha, 0.0):
            print("Conta criada com sucesso!")
        else:
            print("Não foi possível criar a conta.")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Digite 1, 2 ou 3.")