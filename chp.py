from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import csv
# prepare driver
driver = webdriver.Chrome('/Users/macuser/Downloads/chromedriver')
#driver.fullscreen_window()

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

#dive in  csv file

with open('checkprice.csv', 'w', newline='') as f:
    fieldnames = ['Order', 'IATA', 'Distance', 'Price']
    theValue = csv.DictWriter(f, fieldnames=fieldnames)

    theValue.writeheader()
    for i in range(num_items):

        values = str(i + 1) + ')' + '' + transInfo[i].text + ',' + prices[i].text + '\n'
        #theValue.writerow(values)
        theValue.writerow({'Order': str(i+1), 'IATA' : iata, 'Distance': transInfo[i].text, 'Price': prices[i].text})
        #print(values)


# with open('checkprice.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#
#     for line in csv_reader:
#         print(line)
#






driver.quit()




