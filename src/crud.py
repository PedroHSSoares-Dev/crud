from conexao import criar_conexao
from tabulate import tabulate
import mysql.connector
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        
def exibir_tabelas():
    conn = criar_conexao()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        cursor.execute("SHOW TABLES")
        tabelas = cursor.fetchall()
        print("Tabelas no banco de dados:")
        for tabela in tabelas:
            print(tabela[0])
    except mysql.connector.Error as err:
        print("Erro ao exibir tabelas:", err)
    finally:
        cursor.close()
        conn.close()

def exibir_dados_transacoes():
    conexao = None
    cursor = None
    try:
        # Cria conexão usando sua função (supondo que criar_conexao() retorna uma conexão válida)
        conexao = criar_conexao()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM tbTransacoes")
        resultado = cursor.fetchall()
        
        dados_formatados = []
        for linha in resultado:
            quantia = float(linha[3])  # Conversão para float
            dados_formatados.append([
                linha[0],  # Id da Transacao
                linha[1],  # Id Remetente
                f"R$ {quantia:,.2f}".replace(".", "X").replace(",", ".").replace("X", ","),  # Formatação BR Quantia
                linha[2],  # Id Destinatario
                linha[4]   # Data e Hora
            ])
            
        print(tabulate(
            dados_formatados,
            headers=["ID", "RemetenteId", "Quantia", "DestinatarioId", "Data e Hora"],
            tablefmt="pretty",
            numalign="right"
        ))
        print(f'{len(dados_formatados)} registros encontrados.')
    
    except mysql.connector.Error as e:
        print(f"Erro de banco de dados: {e}")
    finally:
        # Fechar recursos corretamente
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
           
def exibir_dados_user():
    conexao = None
    cursor = None
    try:
        # Cria conexão usando sua função (supondo que criar_conexao() retorna uma conexão válida)
        conexao = criar_conexao()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM tbUser")
        resultado = cursor.fetchall()
        
        dados_formatados = []
        for linha in resultado:
            saldo = float(linha[3])  # Conversão para float
            dados_formatados.append([
                linha[0],  # ID
                linha[1],  # Usuário
                "******",  # Mascarando senha (boas práticas)
                f"R$ {saldo:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")  # Formatação BR
            ])
            
        print(tabulate(
            dados_formatados,
            headers=["ID", "Nome", "Senha", "Saldo"],
            tablefmt="pretty",
            numalign="right"
        ))
        print(f'{len(dados_formatados)} registros encontrados.')
        
    
    except mysql.connector.Error as e:
        print(f"Erro de banco de dados: {e}")
    finally:
        # Fechar recursos corretamente
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()
            
def editar_dados(tabela, coluna, novo_valor, condicao):
    conn = criar_conexao()
    if conn is None:
        return
    
    cursor = conn.cursor()
    try:
        query = f"UPDATE {tabela} SET {coluna} = %s WHERE id = {condicao}"
        cursor.execute(query, (novo_valor,))
        conn.commit()  # Importante para salvar no banco
        print("Dados atualizados com sucesso!")
    except mysql.connector.Error as err:
        print("Erro ao atualizar dados:", err)
    finally:
        cursor.close()
        conn.close()

def apagar_dados(tabela, condicao):
    conn = criar_conexao()
    if conn is None:
        return
    
    cursor = conn.cursor()
    try:
        query = f"DELETE FROM {tabela} WHERE id = {condicao}"
        cursor.execute(query)
        conn.commit()  # Importante para salvar no banco
        print("Dados apagados com sucesso!")
    except mysql.connector.Error as err:
        print("Erro ao apagar dados:", err)
    finally:
        cursor.close()
        conn.close()