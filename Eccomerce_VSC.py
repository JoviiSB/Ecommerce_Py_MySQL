import mysql.connector

class Produto:
    def __init__(self, nome, preco, quantidade_disponivel):
        self.nome = nome
        self.preco = preco
        self.quantidade_disponivel = quantidade_disponivel

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class EcommerceDB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="ecommerce"
        )
        self.cursor = self.conn.cursor()

    def adicionar_produto(self, produto):
        sql = "INSERT INTO produtos (nome, preco, quantidade_disponivel) VALUES (%s, %s, %s)"
        val = (produto.nome, produto.preco, produto.quantidade_disponivel)
        self.cursor.execute(sql, val)
        self.conn.commit()
        print("Produto adicionado com sucesso.")

    def mostrar_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        produtos = self.cursor.fetchall()
        for produto in produtos:
            print(produto)

    def adicionar_cliente(self, cliente):
        sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
        val = (cliente.nome, cliente.email)
        self.cursor.execute(sql, val)
        self.conn.commit()
        print("Cliente adicionado com sucesso.")

    def mostrar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()
        print("Conexão fechada.")

def menu():
    print("1. Adicionar Produto;")
    print("2. Mostrar Produtos;")
    print("3. Adicionar Cliente;")
    print("4. Mostrar Clientes;")
    print("5. Sair.")

if __name__ == "__main__":
    ecommerce_db = EcommerceDB()

    while True:
        menu()
        escolha = input("Escolha uma opção (1 a 5): ")

        if escolha == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade disponível: "))
            produto = Produto(nome, preco, quantidade)
            ecommerce_db.adicionar_produto(produto)
        elif escolha == "2":
            print("Produtos disponíveis:")
            ecommerce_db.mostrar_produtos()
        elif escolha == "3":
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            cliente = Cliente(nome, email)
            ecommerce_db.adicionar_cliente(cliente)
        elif escolha == "4":
            print("Clientes registrados:")
            ecommerce_db.mostrar_clientes()
        elif escolha == "5":
            print("Saindo...")
            ecommerce_db.fechar_conexao()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
