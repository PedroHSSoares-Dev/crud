from conexao import criar_conexao
import mysql.connector

def conferir_usuario(user, senha):
    conn = criar_conexao()
    if conn is None:
        return False
    
    cursor = conn.cursor()
    try:
        # Verifica usuário e senha juntos
        cursor.execute(
            "SELECT * FROM tbUser WHERE Nome = %s AND Senha = %s",  # Correção aqui
            (user, senha)  # Faltava o parêntese de fechamento
        )
        resultado = cursor.fetchone()
        return resultado is not None
    except mysql.connector.Error as err:
        print("Erro ao verificar usuário:", err)
        return False
    finally:
        cursor.close()
        conn.close()

def criar_usuario(user, senha, saldo):
    conn = criar_conexao()
    if conn is None:
        return False

    cursor = conn.cursor()
    try:
        # Verifica se usuário já existe
        cursor.execute("SELECT * FROM tbUser WHERE Nome = %s", (user,))
        if cursor.fetchone():
            print("Usuário já existe!")
            return False

        # Cria novo usuário
        cursor.execute(
            "INSERT INTO tbUser (Nome, Senha, Saldo) VALUES (%s, %s, %s)",
            (user, senha, saldo)
        )
        conn.commit()  # Importante para salvar no banco
        print("Usuário criado com sucesso!")
        return True
    except mysql.connector.Error as err:
        print("Erro ao criar usuário:", err)
        return False
    finally:
        cursor.close()
        conn.close()