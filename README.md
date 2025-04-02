# Sistema Bancário Simples (CRUD com Docker)

Um sistema bancário básico com funcionalidades de CRUD, autenticação de usuários, transferências (PIX), e gestão de transações. Desenvolvido em Python com MySQL e Docker.

---

## 📋 Descrição do Projeto

Este projeto simula operações bancárias básicas, como:
- **Criação de usuários** (comum e admin).
- **Depósitos, saques e transferências (PIX)**.
- **Gestão de saldo e extrato**.
- **Interface administrativa** para gerenciar dados.

---

## 🚀 Funcionalidades

### 👤 Usuário Comum
- **Depositar/Sacar** dinheiro.
- **Transferir (PIX)** para outros usuários.
- **Consultar saldo** e extrato.

### 👑 Administrador
- **Visualizar/Editar/Excluir** dados de usuários e transações.
- **Acessar todas as transações** do sistema.

---

## 🛠️ Tecnologias Utilizadas
- **Python** (CLI Interface)
- **MySQL** (Banco de Dados)
- **Docker** (Containerização)
- **Bibliotecas**: `mysql-connector-python`, `tabulate`

---

## ⚙️ Estrutura do Projeto
CRUD/  
├── docker/ -> Pasta com arquivos do Docker para configurar o banco de dados  
│   ├── docker-compose.yml -> # Arquivo para subir o banco MySQL com Docker  
│   ├── init.sql -> # Script SQL para criar tabelas e inserir dados iniciais  
├── src/ -> # Código-fonte principal do projeto  
│   ├── conexao.py -> # Lida com a conexão ao banco de dados MySQL  
│   ├── crud.py -> # Contém as funções de manipulação do banco de dados (CRUD)  
│   ├── menu.py -> # Script principal que exibe o menu e interage com o usuário  
├── .gitignore -> # Arquivo para ignorar arquivos desnecessários no Git (como `__pycache__`)  
├── README.md ->  # Documentação do projeto, explicando como rodar e usar  

---
## 🚀 Como Executar

### Pré-requisitos
- **Docker** e **Docker Compose** instalados.
- **Python 3.8+**.

### Passo a Passo

1. **Inicie o Banco de Dados (Docker):**
   ```bash
   docker compose -f docker/docker-compose.yml up -d
   ```
2. **Instale as Dependências:**
    ```bash
    pip install mysql-connector-python tabulate
    ```
3. **Execute o sistema:**
    ```bash
    python src/menu.py
    ```
---
## 📋 Funcionalidades Principais
### 👤 Menu do Usuário Comum
- Depósito: depositar(usuario, valor)

- Saque: saque(usuario, valor)

- PIX: pix(remetente_id, destinatario_id, valor)

- Extrato: exibir_dados_transacoes(usuario)

### 👑 Menu do Administrador
- Visualizar Tabelas: exibir_tabelas()

- Editar Dados: editar_dados(tabela, coluna, novo_valor, condicao)

- Excluir Dados: apagar_dados(tabela, condicao)

---
## 🔍 Detalhes Técnicos
- Procedimento Armazenado (MySQL)
```sql
CREATE PROCEDURE TransferirDinheiro(
    IN p_RemetenteId INT,
    IN p_DestinatarioId INT,
    IN p_Quantia DECIMAL(10,2)
)
BEGIN
    -- Verificação de saldo e transação atômica
    START TRANSACTION;
    -- [...]
    COMMIT;
END
```

- Configuração do Docker Compose
```yml
    version: '3'
    services:
      mysql:
        image: mysql:8.0
        environment:
          MYSQL_ROOT_PASSWORD: root
          MYSQL_DATABASE: banco
        ports:
          - "3306:3306"
        volumes:
          - ./intlsql:/docker-entrypoint-initdb.d
```

---

## 🛠️ Solução de Problemas

### Erro Comum: "Usuário não encontrado"
- Causa: IDs incorretos ou nomes digitados errados.
- Solução: Use ```pegar_id_usuario(nome)``` para validar o destinatário.

### Erro de Conexão ao MySQL
- Verifique o container:
```bash
  docker ps -a
  docker logs mysql_container
```
---
## 📝 Notas de Desenvolvimento

- Segurança: As senhas são armazenadas em texto plano (⚠️ não adequado para produção).
- Melhorias Sugeridas:
  - Adicionar criptografia de senhas com ```bcrypt```.
  - Implementar histórico detalhado de transações.
  - Adicionar autenticação via token JWT.