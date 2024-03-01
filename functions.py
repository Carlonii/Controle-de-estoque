import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="1234",
    database = "estoque"
)

mycursor = db.cursor()

def showProd():
    mycursor.execute("SELECT * FROM  Produto")
    for x in mycursor:
        print(x)

def showTrans():
    mycursor.execute("SELECT * FROM  Trans")
    for x in mycursor:
        print(x)

def showTables():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

def mostrarEstoque():
    mycursor.execute("SELECT * FROM  Produto")
    for x in mycursor:
        print(x)

def addQnt(id,qnt):
    mycursor.execute("INSERT INTO Trans (prodId, qnt , operation) VALUES (%s,%s,%s)", (id, qnt, "add"))
    db.commit()
    adicionarProduto(id,qnt)

def removeQnt(id,qnt):
    mycursor.execute("INSERT INTO Trans (prodId, qnt , operation) VALUES (%s,%s,%s)", (id, qnt, "remove"))
    db.commit()
    removerProduto(id,qnt)

def removerProduto(id,qnt):
    mycursor.execute("SELECT quantidade from Produto where id = %s", (id,))
    qntAntiga = mycursor.fetchone()
    qntAntiga = int(qntAntiga[0])
    qntNova = qntAntiga - qnt
    mycursor.execute("UPDATE Produto SET quantidade = %s WHERE id = %s", (qntNova, id))
    db.commit()

def adicionarProduto(id,qnt):
    mycursor.execute("SELECT quantidade from Produto where id = %s", (id,))
    qntAntiga = mycursor.fetchone()
    qntAntiga = int(qntAntiga[0])
    qntNova = qntAntiga + qnt
    mycursor.execute("UPDATE Produto SET quantidade = %s WHERE id = %s", (qntNova, id))
    db.commit()

def fazer_login(username, passwd):
    mycursor.execute("SELECT userName, passwd FROM Adm WHERE userName = %s AND passwd = %s", (username, passwd))
    result = mycursor.fetchone()

    if result:
        return 1
    else:
        return 0
    
def fazer_login_func(username, passwd):
    mycursor.execute("SELECT userName, passwd FROM Funcionario WHERE userName = %s AND passwd = %s", (username, passwd))
    result = mycursor.fetchone()

    if result:
        return 1
    else:
        return 0
    
def addFunc(user, passwd):
    mycursor.execute("INSERT INTO Funcionario (userName, passwd) VALUES (%s,%s)", (user, passwd))
    db.commit()

def removeFunc(id):
    mycursor.execute("DELETE FROM Funcionario WHERE id = (%s)", (id,))
    db.commit()

def alterFunc(id, user , passwd):
    mycursor.execute("UPDATE Funcionario SET userName = (%s) , passwd = (%s) WHERE id = (%s)", (user, passwd, id))
    db.commit()

def showFunc():
    mycursor.execute("SELECT * FROM  Funcionario")
    for x in mycursor:
        print(x)

def addItem(nome, qnt):
    mycursor.execute("INSERT INTO Produto (nome , quantidade) VALUES (%s,%s)", (nome, qnt))
    db.commit()

def removeItem(id):
    mycursor.execute("DELETE FROM Produto WHERE id = (%s)", (id,))
    db.commit()

def alterarItem(id , name, qnt):
    mycursor.execute("UPDATE Produto SET nome = (%s) , quantidade = (%s) WHERE id = (%s)", (name, qnt, id))
    db.commit()