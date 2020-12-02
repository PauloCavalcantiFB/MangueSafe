import gspread
from oauth2client.service_account import ServiceAccountCredentials
import login

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("Sheets-ad827ad1a99d.json", scope)

client = gspread.authorize(creds)

sheet = client.open("databike").sheet1  # abre a planilha

dados = sheet.get_all_records()  # gera uma lista com todas as informações

print("")
print("----------------------------------------------------------------")
print("Bem vindo, ao programa de denuncias!")
print("Se é sua primeira vez, escolha a opção de cadastro(Numero 0), caso ja esteja cadastrado, escolha a opção de Login(Numero 1)!")

inicio = int(input("Digite o numero de sua opção: "))


if inicio == 1:
    log = logar()
else:
    criarConta()
    
start = False
if log == True:
    start = True

while start == True:
    row = []
    problema = ""
    print("")
    print("----------------------------------------------------------------")
    print("")
    data = input("para começar, por favor digite a data do ocorrido: ")
    print("")
    local = input("agora por favor, digite o local do ocorrido: ")
    print("")
    print("----------------------------------------------------------------")
    print("agora por favor, registre sua denuncia de acordo com o numero abaixo:")
    print("")
    print("1- Problemas na estrutura na cidade")
    print("2- Assalto ou furto")
    print("3- Problemas com motoristas")
    print("4- Outro")
    print("")
    print("----------------------------------------------------------------")
    denuncia = int(input("agora por favor, digite seu numero: "))7777

    if denuncia == 1:
        problema = "problema na estrutura"
    if denuncia == 2:
        problema = "Assalto ou furto"
    if denuncia == 3:
        problema = "Problemas com motoristas"
    if denuncia == 4:
        problema = "Outro"

    
    row.append(data)
    row.append(local)
    row.append(problema)
    print(row)
    sheet.insert_row(row,2)
    
    print("----------------------------------------------------------------")
    print("")
    print("Obrigado por sua denuncia! para registrar outra denuncia, digite 1, caso queira sair, digite 0.")

    opc = int(input("Sua opcao: "))
    if opc != 1:
        break
    
    
    
    
    
    
    
    
