import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("data/creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1ABGauhlgMio0t5pwmK-xRrLXC3MUhEv2ZpZ36zimZ4A/edit?usp=sharing').sheet1
