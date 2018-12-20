from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# prepare driver
driver = webdriver.Chrome("C:/Users/DAVID/Desktop/Onepark-py/chromedriver.exe")
driver.

chrome_options = Options()
chrome_options.add_argument("--headless")

# prepare date data type

formatDate = '%y-%m-%d'
today = datetime.date.today()
oneDay = datetime.timedelta(days=1)

startDay = today + 2*oneDay

startDay = startDay.strftime(formatDate)

endDay = today + 9*oneDay
endDay = endDay.strftime(formatDate)

# prepare parkings

parking = 'Geneve'
iata = "GVA"
# open web and set args

u='https://www.onepark.fr/en/parkings?q='+parking+'+airport&begin_date=20'+startDay+'&end_date=20'+endDay+'&order=price'
goWeb = driver.get(u)

# get prices

prices = driver.find_elements_by_class_name('price')
transInfo = driver.find_elements_by_class_name('transport-info')

num_items = len(prices)

#dive in  Google sheets file
#Create API of Googlesheets

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('myProject-b73948492879.json', scope)

gs = gspread.authorize(credentials)


Titlegs = str(today)
wks = gs.open('Test').add_worksheet(str(today + 2*oneDay), 100, 100)

wks.append_row(['Order', 'IATA', 'Distance', 'Price'])

for i in range(num_items):
    wks.append_row([str(i+1), iata,transInfo[i].text, prices[i].text])

driver.quit()

