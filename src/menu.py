from crud import limpar_tela, conferir_usuario, criar_usuario, exibir_tabelas, exibir_dados_user, editar_dados

while True:
    limpar_tela()
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
            
            if usuario == "admin":
                limpar_tela()
                
                while True:
                    print("\n===== MENU ADMINISTRADOR =====")
                    print("1. Editar dados")
                    print("2. Apagar dados")
                    print("3. Voltar")
                    opcao = input("Escolha uma opção: ")
                    
                    if opcao == "1":
                        exibir_tabelas()
                        tbEscolhida = input("Escolha a tabela que você quer editar: ").strip()
                        if tbEscolhida == "tbUser":
                            exibir_dados_user()
                        idEscolhido = input("Digite o ID do registro que você quer editar: ").strip()
                        colunaEscolhida = input("Escolha a coluna que você quer editar: ").strip().capitalize()
                        novoValor = input("Digite o novo valor: ").strip()
                        editar_dados(tbEscolhida, colunaEscolhida, novoValor, idEscolhido)
                        if tbEscolhida == "tbUser":
                            exibir_dados_user()
                        print("Dados editados com sucesso!")
                        input("Pressione Enter para continuar...")
                        
                        
                    elif opcao == "2":
                        limpar_tela()
                        print("Apagando dados...")
                        # Aqui você pode adicionar a lógica para apagar os dados
                        
                    elif opcao == "3":
                        break
                        
                    else:
                        print("Opção inválida. Tente novamente.")
            else:
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