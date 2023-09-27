import time
import pickle
import pyautogui
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


email = "***REMOVED***"
password = "***REMOVED***"
website_url = "https://distrokid.com/mymusic/"


def confirm_alert(driver: webdriver.Chrome):
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()
    except Exception as e:
        print(f"Failed to confirm alert: {str(e)}")

def cookie_button_click(driver: webdriver.Chrome):
    try:
        button = driver.find_element(By.CLASS_NAME, "swal2-confirm.cookieModalConfirmButton.swal2-styled")
        button.click()
    except Exception as e:
        print("Element not found or unable to click:", str(e))   

def add_cookies(driver: webdriver.Chrome):
    try:
        with open("D:\Programmieren\Python\SpotifyManager\cookies.txt", 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                driver.add_cookie(cookie)

    except Exception as e:
        print("Element not found or unable to click:", str(e))   

def login_click(driver: webdriver.Chrome):
    try:
        driver.execute_script("openSignIn();")

        email_button = driver.find_element(By.ID, "inputSigninEmail")
        email_button.click()
        pyautogui.typewrite(email.split('@')[0])
        pyautogui.hotkey('ctrl', 'alt', 'q')
        pyautogui.typewrite(email.split('@')[1])

        password_button = driver.find_element(By.ID, "inputSigninPassword")
        password_button.click()
        pyautogui.typewrite(password)

        signin_button = driver.find_element(By.ID, "signinButton")
        signin_button.click()
    
    except Exception as e:
        print("Element not found or unable to click:", str(e))   

def cookie_button_click(driver: webdriver.Chrome):
    try:
        button = driver.find_element(By.CLASS_NAME, "swal2-confirm.cookieModalConfirmButton.swal2-styled")
        button.click()
    except Exception as e:
        print("Element not found or unable to click:", str(e))   

def uncheck_platforms(driver: webdriver.Chrome):
    try:
        #checkboxes = driver.find_elements(By.NAME, "store")
        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

        for checkbox in checkboxes:
            print("Checkbox Text:", checkbox.text)
            checkbox.click()

    except Exception as e:
        print("Element not found or unable to click:", str(e))   

def choose_genre(driver: webdriver.Chrome):
    try:
        dropdown_menu = driver.find_element(By.ID, "genrePrimary")
        driver.execute_script("arguments[0].scrollIntoView();", dropdown_menu)
        dropdown_menu.click()
        time.sleep(1)

        try:
            image_path = 'D:\Programmieren\Python\SpotifyManager\hiphop.png'
            image_location = pyautogui.locateOnScreen(image_path, confidence=0.7)
            x, y = pyautogui.center(image_location)
            pyautogui.click(x, y)
        except Exception as e:
            print("error - ", str(e))

        driver.execute_script("genreChange();")

    except Exception as e:
        print("Element not found or unable to click:", str(e))   

def upload_cover_art(driver: webdriver.Chrome):
    try:
        file_input = driver.find_element(By.NAME, "artwork")
        driver.execute_script("arguments[0].scrollIntoView();", file_input)
        file_path = "D:\Programmieren\Python\SpotifyManager\cover-art\APEIRON - Me Gustas Tu - Sped Up_cover.jpeg"
        file_input.send_keys(file_path)
    except Exception as e:
        print("Element not found or unable to click:", str(e)) 

def input_track_title(driver: webdriver.Chrome):
    try:
        title_element = driver.find_element(By.CSS_SELECTOR, ".coolInput.cool-input-text.uploadFileTitle.track_1")
        driver.execute_script("arguments[0].scrollIntoView();", title_element)
        title_element.click()

        time.sleep(0.5)
        title = "D:\Programmieren\Python\SpotifyManager\cover-art\APEIRON - Me Gustas Tu - Sped Up_cover.jpeg"
        print(title.split("\\")[5].replace(".jpeg", ""))
        pyautogui.typewrite(title.split("\\")[-1].replace(".jpeg", "").replace("_cover", ""))
        time.sleep(0.5)
        pyautogui.click(500, 500)
        confirm_alert(driver)


    except Exception as e:
        print("Element not found or unable to click:", str(e)) 

def input_musician(driver: webdriver.Chrome, first_name : str, last_name : str):
    try:
        first_name_element = driver.find_element(By.NAME, "songwriter_real_name_first1")
        driver.execute_script("arguments[0].scrollIntoView();", first_name_element)
        first_name_element.click()
        time.sleep(1)
        pyautogui.typewrite(first_name)

        last_name_element = driver.find_element(By.NAME, "songwriter_real_name_last1")
        last_name_element.click()
        time.sleep(1)
        pyautogui.typewrite(last_name)


    except Exception as e:
        print("Element not found or unable to click:", str(e)) 

def upload_song(driver: webdriver.Chrome):
    try:
        file_input = driver.find_element(By.NAME, "file")
        driver.execute_script("arguments[0].scrollIntoView();", file_input)
        file_path = "D:\Programmieren\Python\SpotifyManager\downloads\APEIRON - Me Gustas Tu - Sped Up.mp3"
        file_input.send_keys(file_path)

    except Exception as e:
        print("Element not found or unable to click:", str(e))   

def accept_requrirements(driver: webdriver.Chrome):
    try:
        checkbox0 = driver.find_element(By.ID, "areyousureyoutube")
        driver.execute_script("arguments[0].scrollIntoView();", checkbox0)
        checkbox0.click()

        checkbox1 = driver.find_element(By.ID, "areyousurerecorded")
        checkbox1.click()

        checkbox2 = driver.find_element(By.ID, "areyousurenonstandardscaps")
        checkbox2.click()

        checkbox3 = driver.find_element(By.ID, "areyousuretandc")
        checkbox3.click()

        checkbox4 = driver.find_element(By.ID, "areyousureotherartist")
        checkbox4.click()

    except Exception as e:
        print("Element not found or unable to click:", str(e))   

def upload_finished_button(driver: webdriver.Chrome):
    try:
        doneButton = driver.find_element(By.ID, "doneButton")
        doneButton.click()

    except Exception as e:
        print("Element not found or unable to click:", str(e))   

chrome_options = Options()
#chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(website_url)
    print("Page Title:", driver.title)

    cookie_button_click(driver=driver)
    add_cookies(driver=driver)

    login_click(driver=driver)

    time.sleep(2)
    driver.get("https://distrokid.com/new-upload/")
    time.sleep(1)

    while (driver.current_url != "https://distrokid.com/mymusic/"):
        time.sleep(1)
    
    driver.get("https://distrokid.com/new-upload/")

    # Wait for upload page
    # element = WebDriverWait(driver, 10e100).until(
    #     EC.visibility_of_element_located((By.ID, "allStoreCheckboxes"))
    # )

    # NOT IMPLEMENTED FOR NOW

    #Uncheck all boxes except spotify 
    #uncheck_platforms(driver=driver)

    # ========================


    time.sleep(0.5)
    choose_genre(driver=driver) 
    
    time.sleep(0.5)
    upload_cover_art(driver=driver)

    time.sleep(0.5)
    input_musician(driver, "enething", ".")

    time.sleep(0.5)
    upload_song(driver=driver)

    time.sleep(0.5)
    input_track_title(driver=driver)

    time.sleep(0.5)
    accept_requrirements(driver)

    time.sleep(1)
    upload_finished_button(driver)

except Exception as e: 
    print("An error occurred:", str(e))

input()
# time.sleep(5)
# driver.quit()
