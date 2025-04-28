
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

import sys
sys.stdout.reconfigure(encoding='utf-8')



# 🔧 Function to build and return the driver
def buildDriver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    absher = "https://www.absher.sa/wps/portal/individuals/Home/homepublic/!ut/p/z1/hY6xDoIwEIafhYGVu5agxK041BgSI4vYxYApBVMoKRVe3yZOJBhv--__vsuBgBLEUM2dqlxnhkr7fBe7ByeEnSjHnPOC4vXISLxnGUlJArd_gPA1_hiG3hcbCMOsoFmMyC90E1jdOINQ2tTfd9lQx6kCYWUjrbTR2_p169w4HUIMcVmWSBmjtIyepg9xS2nN5KBckzD2Jb4SPecsCD5ltjEP/dz/d5/L0lDUmlTUSEhL3dHa0FKRnNBLzROV3FpQSEhL2Vu/"

    driver.get(absher)
    
    print("✅ Opened Absher:", driver.title)


    return driver

# 🔐 Function to perform login using provided credentials
def fillUsernamePassword(driver, user_id, password):
    # Wait for and fill ID
    id_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "LoginPortletIDField1"))
    )
    id_input.clear()
    id_input.send_keys(user_id)

    # Wait for and fill Password
    password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "LoginPortletSecretField1"))
    )
    password_input.clear()
    password_input.send_keys(password)
    
    print("🔓 Entered login credentials.")


#Click login button
def clickSubmit(driver):
         
    driver.find_element(By.ID, "LoginPortletFormSubmit").click()

# 🧪 Usage
driver = buildDriver()
fillUsernamePassword(driver, wrongUsermame, wrongPassword)
clickSubmit(driver)
time.sleep(1)

fillUsernamePassword(driver, wrongUsermame, wrongPassword)
clickSubmit(driver)
time.sleep(1)

fillUsernamePassword(driver, wrongUsermame, wrongPassword)
clickSubmit(driver)
time.sleep(20)
driver.quit()


# #step 3
# fillUsernamePassword(driver, correctID, correctPassword+"wrong",)

# #step 4
# fillUsernamePassword(driver, correctPassword, correctPassword+"wrong",)

# #step 5
# fillUsernamePassword(driver, correctID+"2", correctPassword)

# #step 6
# fillUsernamePassword(driver, emptyUsername, emptyPassword)

# #step 9:
# fillUsernamePassword(driver, correctID, emptyPassword + "1")

# #step 10:
# fillUsernamePassword(driver, wrongUsermame, wrongPassword)
# clickSubmit(driver)
# time.sleep(1)

# fillUsernamePassword(driver, wrongUsermame, wrongPassword)
# clickSubmit(driver)
# time.sleep(1)

# fillUsernamePassword(driver, wrongUsermame, wrongPassword)
# clickSubmit(driver)
# time.sleep(20)








