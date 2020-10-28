import twitter_bot
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#def getLineRow(info):
#    line = 2
#    col = 1
#    for x in range(len(info)):        
#        print("O numero de acidentes no dia", cell ,"foi de", sheet.cell(line,col+1).value)
#        line += 1
            
line = 2
col = 1

#Credenciais do JSON gerada pelo google
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("Sheets-ad827ad1a99d.json", scope)
client = gspread.authorize(creds)

#Trabalhando com a planilha
sheet = client.open("databike").sheet1  # abre a planilha
data = sheet.get_all_records()  # gera uma lista com todas as informações
cell = sheet.cell(line,col)

texto = "No dia " + cell.value + " foi constatado um total de " + sheet.cell(line, col+1).value + " acidentes envolvendo ciclistas pela cidade do Recife. Também foi percebido que a rua com maior índice de acidentes ou relatos de queixas foi a ..."

try:
    twitter_bot.post_text(texto)
    print("Autenticação OK.")
except:
    print("Error")
    exit(1)
