from selenium import webdriver
import time
from Library.LocalShareVariables import LSV
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.by import By


def openBrowser():
    print(">>Open Browser: START")
    global danpheEMR
    ChromePath = LSV.ChromeDriverPath
    danpheEMR = webdriver.Chrome(executable_path=ChromePath)
    danpheEMR.set_window_position(-2000, 0)
    danpheEMR.maximize_window()
    danpheEMR.get(GSV.appURL)
    print("Open Browser: END<<")
    return danpheEMR


def closeBrowser():
    print(">>Close Browser: START")
    danpheEMR.close()
    print("###TEST CASE: PASSED###")
    # print("Close Browser: END<<")


def login(userid, pwd):
    print(">>LogIn: START")
    time.sleep(5)
    danpheEMR.find_element(By.ID, "username_id").send_keys(userid)
    danpheEMR.find_element(By.ID, "password").send_keys(pwd)
    danpheEMR.find_element(By.ID, "login").submit()
    print("LogIn: END<<")


def verifyLogIn(danpheEMR):
    print("Start:verifyLogIn")
    title = danpheEMR.title
    print(title)
    assert title == "DanpheHealth"
    print("End: verifyLogin")


def logout():
    print(">>LogOut: START")
    time.sleep(3)
    danpheEMR.find_element(By.CSS_SELECTOR, ".dropdown-toggle:nth-child(1) > .fa").click()
    time.sleep(1)
    danpheEMR.find_element(By.LINK_TEXT, "Log Out").click()
    print("LogOut: END<<")


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
