from crud import limpar_tela, conferir_usuario, criar_usuario, exibir_tabelas, exibir_dados_user, exibir_dados_transacoes, editar_dados, apagar_dados
from time import sleep

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
            sleep(1)
            
            if usuario == "admin":                                                                      # MENU ADMINISTRADOR
                
                while True:
                    limpar_tela()
                    print("\n===== MENU ADMINISTRADOR =====")
                    print("1. Exibir dados")
                    print("2. Editar dados")
                    print("3. Apagar dados")
                    print("4. Voltar")
                    opcao = input("Escolha uma opção: ")
                    
                    if opcao == "1":
                        limpar_tela()
                        print("Exibindo dados...")
                        exibir_tabelas()
                        tbEscolhida = input("Escolha a tabela que você quer visualizar: ").strip()
                        if tbEscolhida == "tbUser":
                            exibir_dados_user()
                        else:
                            exibir_dados_transacoes()
                        input("Pressione Enter para continuar...")
                        
                    elif opcao == "2":
                        limpar_tela()
                        exibir_tabelas()
                        tbEscolhida = input("Escolha a tabela que você quer editar: ").strip()
                        if tbEscolhida == "tbUser":
                            exibir_dados_user()
                        elif tbEscolhida == "tbTransacoes":
                            exibir_dados_transacoes()
                        else:
                            print("Tabela inválida.")
                            break
                        idEscolhido = input("Digite o ID do registro que você quer editar: ").strip()
                        colunaEscolhida = input("Escolha a coluna que você quer editar: ").strip().capitalize()
                        novoValor = input("Digite o novo valor: ").strip()
                        editar_dados(tbEscolhida, colunaEscolhida, novoValor, idEscolhido)
                        if tbEscolhida == "tbUser":
                            exibir_dados_user()
                        print("Dados editados com sucesso!")
                        input("Pressione Enter para continuar...")
                        
                    elif opcao == "3":
                        limpar_tela()
                        print("Apagando dados...")
                        exibir_tabelas()
                        tbEscolhida = input("Escolha a tabela que você quer apagar: ").strip()
                        if tbEscolhida == "tbUser":
                            exibir_dados_user()
                        elif tbEscolhida == "tbTransacoes":
                            exibir_dados_transacoes()
                        else:
                            print("Tabela inválida.")
                            break
                        idEscolhido = input("Digite o ID do registro que você quer apagar: ").strip()
                        apagar_dados(tbEscolhida, idEscolhido)
                        limpar_tela()
                        print("Dados apagados com sucesso!")
                        if tbEscolhida == "tbUser":
                            exibir_dados_user()
                        else:
                            exibir_dados_transacoes()
                        input("Pressione Enter para continuar...")
                        
                    elif opcao == "4":
                        break
                        
                    else:
                        print("Opção inválida. Tente novamente.")
            
            else:                                                                                   # MENU USUÁRIO COMUM
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