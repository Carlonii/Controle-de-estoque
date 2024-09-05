import mysql.connector
from createTables import *
from functions import *
from datetime import datetime

db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="1234",
    database = "estoque_loja"
)

mycursor = db.cursor()

def main():
    login = 0
    while login != 3:
        login = int(input("1 - Login como ADM \n2 - Login como Funcionario \n3 - Fechar \n"))

        if login == 1:
            username = input("Digite seu username \n")
            passwd = input("Digite sua senha \n")
            responsavel = fazer_login(username, passwd)
            if responsavel != 0:
                telaAdm(username)
            else:
                print("Usuario ou senha estao incorretos")
                break
        
        if login == 2:
            username = input("Digite seu username \n")
            passwd = input("Digite sua senha \n")
            responsavel = fazer_login_func(username, passwd)
            if responsavel != 0:
                telaFunc(username)
            else:
                print("Usuario ou senha estao incorretos")
                break

        if login == 3:
            return 1
    
    

def telaAdm(username):
    op = 0
    while op != 4:
        op = input("Qual menu deseja acessar ? \n1 - Menu Funcionarios \n2 - Menu Estoque \n3 - Menu Itens \n4 - Fechar Menu \n")
        if op == '1':
           menuFunc()
        elif op == '2':
            pass
            menuEstoq(username)
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
            mycursor.execute("SELECT id from Funcionario where id = %s", (id,))
            idcheck = mycursor.fetchone()
            if idcheck:
                removeFunc(id)
            else:
                print("ID selecionado nao consta no banco de dados")
            
        elif op == '3':
            id = input("Qual o id do funcionario que voce deseja alterar ? \n")
            mycursor.execute("SELECT id from Funcionario where id = %s", (id,))
            idcheck = mycursor.fetchone()
            if idcheck:
                user = input("Qual o novo username do funcionario ? \n")
                passwd = input("Qual a nova senha do funcionario ? \n")
                alterFunc(id, user, passwd)
            else:
                print("ID selecionado nao consta no banco de dados")
             
        elif op == '4':
            showFunc()
        elif op == '5':
            pass
        else :  
            print("Choose a valid option") 
        return 1 
    


def menuEstoq(username):
    op = 0
    while op != 4:
        op = input("Qual operacao deseja realizar ? \n 1 - Adicionar ao estoque \n 2 - Remover do estoque \n 3 - Mostrar estoque \n 4 - Fechar Menu \n")
        if op == '1':
            idOp = int(input("Qual o ID do produto que voce deseja adicionar ? \n"))
            qntOp = int(input("Qual a quantidade que deseja adicionar ? \n"))
            mycursor.execute("SELECT id from Produto where id = %s", (idOp,))
            idcheck = mycursor.fetchone()
            if idcheck:
                idcheck = int(idcheck[0])
                addQnt(idOp, qntOp,username)
            else:
                print("ID selecionado nao consta no banco de dados")
        elif op == '2':
            idOp = int(input("Qual o ID do produto que voce deseja remover ? \n"))
            qntOp = int(input("Qual a quantidade que deseja remover ? \n"))
            mycursor.execute("SELECT id from Produto where id = %s", (idOp,))
            idcheck = mycursor.fetchone()
            if idcheck:
                idcheck = int(idcheck[0])
                removeQnt(idOp, qntOp,username)
            else:
                print("ID selecionado nao consta no banco de dados")
            
        elif op == '3':
            mostrarEstoque() 
        elif op == '4':
            return 1
        else :  
            print("Choose a valid option")  
    
def menuItens():
    op = 0
    while op != 5:
        op = input("Qual operacao deseja realizar ? \n 1 - Adicionar item \n 2 - Remover item \n 3 - Alterar item \n 4 - Mostrar itens \n 5 - Fechar menu \n")
        if op == '1':
            nomeItem = input("Qual o nome do item que voce deseja adicionar ? \n")
            nomeItem = nomeItem.lower()
            mycursor.execute("SELECT nome from Produto where nome = %s", (nomeItem,))
            nomecheck = mycursor.fetchone()
            if nomecheck:
                print("Este nome ja esta associado a um item no banco de dados")
            else:
                qntItem = int(input("Qual a quantidade que deseja adicionar ? \n"))
                addItem(nomeItem, qntItem)
            
        elif op == '2':
            idItem = input("Qual o ID do item que voce deseja remover ? \n")
            mycursor.execute("SELECT id from Produto where id = %s", (idItem,))
            idcheck = mycursor.fetchone()
            if idcheck:
                removeItem(idItem)
            else:
                print("Item nao encontrado no banco de dados")
            
        elif op == '3':
            id = input("Qual o id do item que voce deseja alterar ? \n")
            mycursor.execute("SELECT id from Produto where id = %s", (id,))
            idcheck = mycursor.fetchone()
            if idcheck:
                name = input("Qual o novo nome do item ? \n")
                qnt = input("Qual a nova qnt do item ? \n")
                alterarItem(id, name, qnt) 
            else:
                print("Item nao encontrado no banco de dados")
            
        elif op == '4':
            mostrarEstoque() 
        elif op == '5':
            return 1
        else :  
            print("Choose a valid option")  


def telaFunc(username):
    op = 0
    while op != 4:
        op = input("Qual operacao deseja realizar ? \n 1 - Adicionar ao estoque \n 2 - Remover do estoque \n 3 - Mostrar estoque \n 4 - Fechar Menu \n")
        if op == '1':
            idOp = int(input("Qual o ID do produto que voce deseja adicionar ? \n"))
            qntOp = int(input("Qual a quantidade que deseja adicionar ? \n"))
            mycursor.execute("SELECT id from Produto where id = %s", (idOp,))
            idcheck = mycursor.fetchone()
            if idcheck:
                idcheck = int(idcheck[0])
                addQnt(idOp, qntOp,username)
            else:
                print("ID selecionado nao consta no banco de dados")
        elif op == '2':
            idOp = int(input("Qual o ID do produto que voce deseja remover ? \n"))
            qntOp = int(input("Qual a quantidade que deseja remover ? \n"))
            mycursor.execute("SELECT id from Produto where id = %s", (idOp,))
            idcheck = mycursor.fetchone()
            if idcheck:
                idcheck = int(idcheck[0])
                removeQnt(idOp, qntOp,username)
            else:
                print("ID selecionado nao consta no banco de dados")
        elif op == '3':
            mostrarEstoque() 
        elif op == '4':
            return 1
        else :  
            print("Choose a valid option")  


main()
            

    





