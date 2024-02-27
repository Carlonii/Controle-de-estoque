import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="1234",
    database = "estoque"
)

mycursor = db.cursor()

def main():
    login = 0
    while login != 3:
        login = int(input("1 - Login como ADM \n2 - Login como Funcionario \n3 - Fechar \n"))

        if login == 1:
            username = input("Digite seu username \n")
            passwd = input("Digite sua senha \n")
            if fazer_login(username, passwd) == 1:
                telaAdm()
            else:
                print("Usuario ou senha estao incorretos")
                break
        
        if login == 2:
            username = input("Digite seu username \n")
            passwd = input("Digite sua senha \n")
            if fazer_login_func(username, passwd) == 1:
                telaFunc()
            else:
                print("Usuario ou senha estao incorretos")
                break

        if login == 3:
            return 1
    
    




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

def telaAdm():
    op = 0
    while op != 4:
        op = input("Qual menu deseja acessar ? \n1 - Menu Funcionarios \n2 - Menu Estoque \n3 - Menu Itens \n4 - Fechar Menu \n")
        if op == '1':
           menuFunc()
        elif op == '2':
            pass
            menuEstoq()
        elif op == '3':
            pass
            menuItens()
        elif op == '4':
            return 1
        else :  
            print("Choose a valid option")  

def menuFunc():
    op = 0
    while op != 5 :
        op = input("Qual operacao deseja realizar ? \n1 - Adicionar funcionario \n2 - Remover funcionario \n3 - Editar funcionario \n4 - Verfificar funcionarios \n5 - Fechar \n")
        if op == '1':
            user = input("Qual o username do funcionario que voce deseja adicionar ? \n")
            passwd = input("Qual a senha do funcionario que deseja adicionar ? \n")
            addFunc(user, passwd)
        elif op == '2':
            id = input("Qual o id do funcionario que voce deseja remover ? \n")
            removeFunc(id)
        elif op == '3':
            id = input("Qual o id do funcionario que voce deseja alterar ? \n")
            user = input("Qual o novo username do funcionario ? \n")
            passwd = input("Qual a nova senha do funcionario ? \n")
            alterFunc(id, user, passwd) 
        elif op == '4':
            showFunc()
        elif op == '5':
            pass
        else :  
            print("Choose a valid option") 
        return 1 
    
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

def menuEstoq():
    op = 0
    while op != 4:
        op = input("Qual operacao deseja realizar ? \n 1 - Adicionar ao estoque \n 2 - Remover do estoque \n 3 - Mostrar estoque \n 4 - Fechar Menu \n")
        if op == '1':
            idOp = int(input("Qual o ID do produto que voce deseja adicionar ? \n"))
            qntOp = int(input("Qual a quantidade que deseja adicionar ? \n"))
            addQnt(idOp, qntOp)
        elif op == '2':
            idOp = int(input("Qual o ID do produto que voce deseja remover ? \n"))
            qntOp = int(input("Qual a quantidade que deseja remover ? \n"))
            removeQnt(idOp, qntOp)
        elif op == '3':
            mostrarEstoque() 
        elif op == '4':
            return 1
        else :  
            print("Choose a valid option")  
    
def menuItens():
    op = 0
    while op != 5:
        op = input("Qual operacao deseja realizar ? \n 1 - Adicionar item \n 2 - Remover item \n 3 - Alterar item \n 4 - Mostrar itens 5 - Fechar menu \n")
        if op == '1':
            nomeItem = input("Qual o nome do item que voce deseja adicionar ? \n")
            qntItem = int(input("Qual a quantidade que deseja adicionar ? \n"))
            addItem(nomeItem, qntItem)
        elif op == '2':
            idItem = input("Qual o ID do item que voce deseja remover ? \n")
            removeItem(idItem)
        elif op == '3':
            id = input("Qual o id do item que voce deseja alterar ? \n")
            name = "Qual o novo nome do item ? \n"
            qnt = input("Qual a nova qnt do item ? \n")
            alterarItem(id, name, qnt) 
        elif op == '4':
            mostrarEstoque() 
        elif op == '5':
            return 1
        else :  
            print("Choose a valid option")  

def addItem(nome, qnt):
    mycursor.execute("INSERT INTO Produto (nome , quantidade) VALUES (%s,%s)", (nome, qnt))
    db.commit()

def removeItem(id):
    mycursor.execute("DELETE FROM Produto WHERE id = (%s)", (id,))
    db.commit()

def alterarItem(id , name, qnt):
    mycursor.execute("UPDATE Produto SET nome = (%s) , quantidade = (%s) WHERE id = (%s)", (name, qnt, id))
    db.commit()


def telaFunc():
    op = 0
    while op != 4:
        op = input("Qual operacao deseja realizar ? \n 1 - Adicionar ao estoque \n 2 - Remover do estoque \n 3 - Mostrar estoque \n 4 - Fechar Menu \n")
        if op == '1':
            idOp = int(input("Qual o ID do produto que voce deseja adicionar ? \n"))
            qntOp = int(input("Qual a quantidade que deseja adicionar ? \n"))
            addQnt(idOp, qntOp)
        elif op == '2':
            idOp = int(input("Qual o ID do produto que voce deseja remover ? \n"))
            qntOp = int(input("Qual a quantidade que deseja remover ? \n"))
            removeQnt(idOp, qntOp)
        elif op == '3':
            mostrarEstoque() 
        elif op == '4':
            return 1
        else :  
            print("Choose a valid option")  



main()
    





