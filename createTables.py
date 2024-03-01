import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="1234",
    database = "estoque"
)

mycursor = db.cursor()

def createalltables():
    mycursor.execute("CREATE TABLE adm (id int PRIMARY KEY AUTO_INCREMENT, userName varchar(50), passwd varchar(50) )")
    db.commit()
    mycursor.execute("CREATE TABLE funcionario (id int PRIMARY KEY AUTO_INCREMENT, userName varchar(50), passwd varchar(50) )")
    db.commit()
    mycursor.execute("CREATE TABLE produto (id int PRIMARY KEY AUTO_INCREMENT, quantidade int, nome varchar(50) )")
    db.commit()
    mycursor.execute("CREATE TABLE trans (id int PRIMARY KEY AUTO_INCREMENT, prodId int, qnt int , operation varchar(50), respoonsavel varchar(50), FOREIGN KEY (prodId) REFERENCES produto(id) )")
    db.commit()

