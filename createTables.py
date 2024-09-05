import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="1234",
    database = "estoque_loja"
)

mycursor = db.cursor()

def createalltables():
    mycursor.execute("CREATE TABLE adm (id int PRIMARY KEY AUTO_INCREMENT, userName varchar(50), passwd varchar(50) )")
    db.commit()
    mycursor.execute("CREATE TABLE funcionario (id int PRIMARY KEY AUTO_INCREMENT, userName varchar(50), passwd varchar(50) )")
    db.commit()
    mycursor.execute("CREATE TABLE produto (id int PRIMARY KEY AUTO_INCREMENT, quantidade int, nome varchar(50) )")
    db.commit()
    mycursor.execute("CREATE TABLE trans (id int PRIMARY KEY AUTO_INCREMENT, prodId int, qnt int , operation varchar(50), respoonsavel varchar(50), FOREIGN KEY (prodId) REFERENCES produto(id), horario DATETIME )")
    db.commit()



def insert_data():
    # Inserindo dados na tabela adm
    mycursor.execute("INSERT INTO adm (userName, passwd) VALUES ('admin1', 'senha123')")
    db.commit()
    mycursor.execute("INSERT INTO adm (userName, passwd) VALUES ('admin2', 'senha456')")
    db.commit()

    # Inserindo dados na tabela funcionario
    mycursor.execute("INSERT INTO funcionario (userName, passwd) VALUES ('func1', 'funcsenha123')")
    db.commit()
    mycursor.execute("INSERT INTO funcionario (userName, passwd) VALUES ('func2', 'funcsenha456')")
    db.commit()

    # Inserindo dados na tabela produto
    mycursor.execute("INSERT INTO produto (quantidade, nome) VALUES (100, 'Caneta Bic')")
    db.commit()
    mycursor.execute("INSERT INTO produto (quantidade, nome) VALUES (50, 'Caderno 100 folhas')")
    db.commit()
    mycursor.execute("INSERT INTO produto (quantidade, nome) VALUES (200, 'Borracha Escolar')")
    db.commit()
    mycursor.execute("INSERT INTO produto (quantidade, nome) VALUES (75, 'Lápis HB')")
    db.commit()

    # Inserindo dados na tabela trans
    mycursor.execute("INSERT INTO trans (prodId, qnt, operation, respoonsavel, horario) VALUES (1, 20, 'entrada', 'func1', NOW())")
    db.commit()
    mycursor.execute("INSERT INTO trans (prodId, qnt, operation, respoonsavel, horario) VALUES (2, 5, 'saida', 'func2', NOW())")
    db.commit()
    mycursor.execute("INSERT INTO trans (prodId, qnt, operation, respoonsavel, horario) VALUES (3, 50, 'entrada', 'admin1', NOW())")
    db.commit()
    mycursor.execute("INSERT INTO trans (prodId, qnt, operation, respoonsavel, horario) VALUES (4, 10, 'saida', 'func1', NOW())")
    db.commit()


createalltables()
insert_data()     