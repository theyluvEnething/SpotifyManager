import time
import pickle
import pyautogui
import pytesseract
import os
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


email = ""
password = ""
song_path = ""
cover_path = ""
musician_first_name = ""
musician_last_name = ""

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

def upload_cover_art(driver: webdriver.Chrome, file_path: str):
    try:
        file_input = driver.find_element(By.NAME, "artwork")
        driver.execute_script("arguments[0].scrollIntoView();", file_input)
        file_input.send_keys(file_path)
    except Exception as e:
        print("Element not found or unable to click:", str(e)) 

def input_track_title(driver: webdriver.Chrome, track_title: str):
    try:
        title_element = driver.find_element(By.CSS_SELECTOR, ".coolInput.cool-input-text.uploadFileTitle.track_1")
        driver.execute_script("arguments[0].scrollIntoView();", title_element)
        title_element.click()
        time.sleep(0.5)
        pyautogui.typewrite(track_title)
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

def upload_song(driver: webdriver.Chrome, file_path: str):
    try:
        file_input = driver.find_element(By.NAME, "file")
        driver.execute_script("arguments[0].scrollIntoView();", file_input)
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


def delete_assets():
    for filename in os.listdir(cover_path):
        file_path = os.path.join(cover_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    for filename in os.listdir(song_path):
        file_path = os.path.join(song_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("Sucesfully removed all temp files.")


def init_driver():
    chrome_options = Options()
    #chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def main(driver: webdriver.Chrome):
    try:
        driver.get("https://distrokid.com/")
        print("Page Title:", driver.title)

        cookie_button_click(driver=driver)
        add_cookies(driver=driver)

        login_click(driver=driver)

        time.sleep(2)
        driver.get("https://distrokid.com/new-upload/")
        time.sleep(1)

        while (driver.current_url != "https://distrokid.com/mymusic/"):
            time.sleep(1)




        songs = os.listdir(song_path)
        for song in songs:
            driver.get("https://distrokid.com/new-upload/")

            song_file_path = os.path.join(song_path, song)
            print("AUDIO PATH: ", song_file_path)
            
            cover_file_path = os.path.join(cover_path, song.replace(".mp3", ".jpeg"))
            print("COVER PATH: ", cover_file_path)

            song_tile = song.replace(".mp3", "").split("-", 1)[1]
            print("TITLE: ", song_tile, "\n")

            time.sleep(0.5)
            choose_genre(driver=driver) 
            
            time.sleep(0.5)
            upload_cover_art(driver=driver, file_path=cover_file_path)

            time.sleep(0.5)
            input_musician(driver=driver, first_name=musician_first_name, last_name=musician_last_name)

            time.sleep(0.5)
            upload_song(driver=driver, file_path=song_file_path)

            time.sleep(0.5)
            input_track_title(driver=driver, track_title=song_tile)

            time.sleep(0.5)
            accept_requrirements(driver)

            time.sleep(1)
            upload_finished_button(driver)
            time.sleep(5)
            print(f"Fninished uploading {song_tile}.\n")
            time.sleep(2)

        time.sleep(1)
        print("\n\nFinished uploading all songs.\n")
        time.sleep(1)
        delete_assets()

    except Exception as e: 
        print("An error occurred:", str(e))

    



def run():
    email = "***REMOVED***"
    password = "***REMOVED***"
    song_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "songs")
    cover_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cover-art")
    musician_first_name = "enething"
    musician_last_name = "."

    driver = init_driver()
    main(driver)


if __name__ == "__main__":
    run()