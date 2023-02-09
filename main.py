from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import base64
from datetime import datetime
import time

desired_caps = {
    "deviceName": "Pixel_4",
    "platformName": "Android",
    "version" : "11",
    "browserName": "Chrome",
    "chromedriverExecutable": 'C:\\Users\\AYU FM. PRADINI\\Documents\\Kerja\\appium\\latihan1\\chromedriver.exe',
}


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
path = '/storage/emulated/0/Download'
with open('telkomsel1.png', 'rb') as file:
    driver.push_file("{}/telkomsel1.png".format(path), base64.b64encode(file.read()).decode('utf-8'))
with open('telkomsel2.png', 'rb') as file:
    driver.push_file("{}/telkomsel2.png".format(path), base64.b64encode(file.read()).decode('utf-8'))
driver.get('https://tsel.id/touristg20')
driver.implicitly_wait(30)
driver.switch_to.context('NATIVE_APP')
time.sleep(2)
driver.find_element(AppiumBy.XPATH, ".//android.widget.Button[@text='Allow']").click()
driver.switch_to.context('CHROMIUM')
driver.find_element(AppiumBy.CSS_SELECTOR, 'button.btn-primary-submit.w-full').click()
driver.find_element(AppiumBy.CSS_SELECTOR, 'input[placeholder="Enter your fullname"').send_keys('Testing Nama')
driver.find_element(AppiumBy.CSS_SELECTOR, 'input[placeholder="Enter your passport number"]').send_keys('Abcd1234')
driver.find_element(AppiumBy.TAG_NAME, 'body').click()

# driver.find_element(AppiumBy.CSS_SELECTOR, 'div > button.btn-primary-submit.w-full').click()
driver.find_element(AppiumBy.CSS_SELECTOR, 'shared-dropdown div > img').click()
driver.find_element(AppiumBy.CSS_SELECTOR, 'shared-dropdown input[type=text]').send_keys('United States of America')
driver.find_element(AppiumBy.CSS_SELECTOR, 'shared-dropdown > div div > ul > li:nth-child(1)').click()
driver.find_element(AppiumBy.CSS_SELECTOR, 'shared-date-picker img').click()
year = int('1995')
month = 'Mar'.lower()
day = '18'
current_year = datetime.now().year
year_header = int(driver.find_element(AppiumBy.CSS_SELECTOR, 'mat-calendar-header div.mat-calendar-controls button[mat-button] span > span').text)
    
if year != year_header and year < current_year:
    driver.find_element(AppiumBy.CSS_SELECTOR, 'mat-calendar-header button.mat-focus-indicator:first-child').click()
    while True:
        row_first_year = int(driver.find_element(AppiumBy.CSS_SELECTOR, 'mat-multi-year-view tbody tr:nth-child(1) td:nth-child(1) > button > div.mat-calendar-body-cell-content').text)
        row_last_year = int(driver.find_element(AppiumBy.CSS_SELECTOR, 'mat-multi-year-view tbody tr:last-child td:last-child > button > div.mat-calendar-body-cell-content').text)
        if year > row_first_year and year < row_last_year:
            rows = driver.find_elements(AppiumBy.CSS_SELECTOR, 'mat-multi-year-view tbody tr')
            found = False
            for row in rows:
                if found:
                    break
                columns = row.find_elements(AppiumBy.CSS_SELECTOR, 'td')
                for column in columns:
                    if int(column.text) == year:
                        column.click()
                        found = True
                        break
            break
        elif row_first_year > year:
            # Mundurin tahunnya
            driver.find_element(AppiumBy.CSS_SELECTOR, 'button.mat-calendar-previous-button').click()
        elif row_last_year < year:
            # Majuin tahunnya
            driver.find_element(AppiumBy.CSS_SELECTOR, 'button.mat-calendar-next-button').click()

row_months = driver.find_elements(AppiumBy.CSS_SELECTOR, 'mat-year-view tbody tr td div.mat-calendar-body-cell-content')
for row in row_months:
    row_month = row.text
    if row_month.lower() == month:
        row.click()
        break
row_dates = driver.find_elements(AppiumBy.CSS_SELECTOR, 'mat-month-view tbody tr td div.mat-calendar-body-cell-content')
for row in row_dates:
    row_date = row.text
    if int(row_date.lower()) == int(day):
        row.click()
        break
driver.find_element(AppiumBy.CSS_SELECTOR, 'div.mat-datepicker-actions button:nth-child(2)').click()

driver.find_element(AppiumBy.CSS_SELECTOR, 'shared-basic-input[formcontrolname=email] input[type=text]').send_keys('testing1234@gmail.com')
driver.find_element(AppiumBy.CSS_SELECTOR, 'shared-file-input div:nth-child(3)').click()

driver.switch_to.context('NATIVE_APP')
time.sleep(1)
driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
time.sleep(3)
driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/X3/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]').click()
driver.find_element(AppiumBy.ID, 'com.android.chrome:id/done').click()
driver.switch_to.context('CHROMIUM')
driver.find_element(AppiumBy.CSS_SELECTOR, 'shared-number-input[formcontrolname=imei_number_1] input[type=text]').send_keys('123456789012345')
driver.find_element(AppiumBy.CSS_SELECTOR, 'shared-number-input[formcontrolname=imei_number_2] input[type=text]').send_keys('098765432109876')
# driver.find_element(AppiumBy.CSS_SELECTOR, 'shared-number-input[formcontrolname=imei_number_2] input[type=text]').
driver.execute_script('document.activeElement.blur()')
time.sleep(5)
driver.quit()