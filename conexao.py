import mysql.connector

conn = None  # Inicializa conn

try:
    # Conecta ao banco de dados
    conn = mysql.connector.connect(
        host="localhost",        # ou o IP do container, se necessário
        port=3306,
        user="root",
        password="123456",
        database="meu_banco"
    )
    
    if conn.is_connected():
        print("Conexão estabelecida com sucesso!")

    cursor = conn.cursor()
    
except mysql.connector.Error as err:
    print("Erro de conexão:", err)
    
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão encerrada.")