import base64
import gspread 

from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)
def logar():
    auth = True
    flag = 0
    cont = 0
    email = input("Insira seu email: \n")

    sheet = client.open("usuarios").sheet1
    emails = sheet.col_values(1)

    for x in emails:
        if x != email:
            flag =1
            continue
        else: 
            cont+=1

    if flag != 0 and cont > 1:
        print("O usuário não existe!\n")
        auth = False
    else: 
        senha = input("Insira sua senha: \n")
        correct = sheet.cell(cont, 3)
        coded = base64.b64encode(senha.encode("utf-8"))

    return auth

def criarConta():
    auth = True
    cont = 0
    sheet = client.open("usuarios").sheet1

    nome = input("Insira o seu nome: \n")

    emails = sheet.col_values(1)

    email = input("Insira seu e-mail: \n")
    for x in emails:
        if email == x:
            email = input("Insira seu e-mail novamente: \n")
            continue
    
    for x in emails:
        if email == x:
            auth = False
            print("E-mail repetido!")
    
    if auth == True:
        senha = input("Insira sua senha(maior de 6 digitos): \n")

        while len(senha) < 6 and auth == True:
            senha = input("Senha muito curta, escreva uma maior \n")
            cont+=1
            if cont > 3:
                auth = False
                continue

        senha2 = input("Confirme sua senha: \n")

        while senha != senha2 and auth == True:
            senha2 = input("Senha incorreta, por favor insira confirme sua senha novamente: \n")
            cont+=1
            if cont > 3:
                auth = False
                continue

        if auth == True:
            coded = base64.b64encode(senha.encode("utf-8"))

            body = [email, nome, str(coded)]

            sheet.insert_row(body, 2)
            print("Cadastro feito com sucesso!\n")
        else:
            print("Falha no cadastro!\n")

