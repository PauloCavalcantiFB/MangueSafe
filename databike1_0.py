import twitter_bot
import gspread
import TesteSMTP
from oauth2client.service_account import ServiceAccountCredentials

#def getLineRow(info):
#    line = 2
#    col = 1
#    for x in range(len(info)):        
#        print("O numero de acidentes no dia", cell ,"foi de", sheet.cell(line,col+1).value)
#        line += 1
        
data_base = open("data_base_sheet.txt", "r")

line = int(data_base.read())

data_base.close()

#Credenciais do JSON gerada pelo google
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("Sheets-ad827ad1a99d.json", scope)
client = gspread.authorize(creds)

#Trabalhando com a planilha
sheet = client.open("databike").sheet1  # abre a planilha
data = sheet.get_all_records()  # gera uma lista com todas as informações

texto = "No dia " + sheet.cell(line, 1).value + ", houve uma denúncia de um problema no local: " + sheet.cell(line, 2).value + ", através do app DataBike_PE. O acontecido foi: " + sheet.cell(line, 3).value

data_base = open("data_base_sheet.txt", "w")
line += 1
data_base.write(str(line))
data_base.close()

TesteSMTP.smtpsend(texto)
twitter_bot.post_text(texto)
print("Autenticação OK.")