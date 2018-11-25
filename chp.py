from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

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

# open web and set args

u='https://www.onepark.fr/en/parkings?q='+parking+'+airport&begin_date=20'+startDay+'&end_date=20'+endDay+'&order=price'
goWeb = driver.get(u)

# get prices

prices = driver.find_elements_by_class_name('price')
transInfo = driver.find_elements_by_class_name('transport-info')

num_items = len(prices)

print("There are " + str(num_items) + " available parking")
for i in range(num_items):
    print(str(i+1) + ')' + '\n' + transInfo[i].text + '\n' + prices[i].text + '\n' )

driver.quit()

# just for check pull 







