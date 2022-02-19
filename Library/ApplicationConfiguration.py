from selenium import webdriver
import time
from Library.LocalShareVariables import LSV
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.by import By


def openBrowser():
    print("START>>openBrowser")
    global danpheEMR
    ChromePath = LSV.ChromeDriverPath
    danpheEMR = webdriver.Chrome(executable_path=ChromePath)
    danpheEMR.set_window_position(-2000, 0)
    danpheEMR.maximize_window()
    danpheEMR.get(GSV.appURL)
    print("END>>openBrowser")
    return danpheEMR


def closeBrowser():
    print("START>>closeBrowser")
    danpheEMR.close()
    print("END>>closeBrowser")
    print("###TEST CASE: PASSED###")


def login(userid, pwd):
    print("START>>login")
    time.sleep(5)
    danpheEMR.find_element(By.ID, "username_id").send_keys(userid)
    danpheEMR.find_element(By.ID, "password").send_keys(pwd)
    danpheEMR.find_element(By.ID, "login").submit()
    print("END>>login")
    time.sleep(5)


def verifyLogIn(danpheEMR):
    print("START>>verifyLogIn")
    title = danpheEMR.title
    print(title)
    assert title == "DanpheHealth"
    print("END>>verifyLogIn")


def logout():
    print("START>>logout")
    time.sleep(3)
    danpheEMR.find_element(By.CSS_SELECTOR, ".dropdown-toggle:nth-child(1) > .fa").click()
    time.sleep(1)
    danpheEMR.find_element(By.LINK_TEXT, "Log Out").click()
    print("END>>logout")


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
