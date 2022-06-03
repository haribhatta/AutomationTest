from selenium import webdriver
import time
import random
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

AppName = GSV.appName

########
def EmergencyRegistration(danpheEMR):
    danpheEMR.find_element(By.LINK_TEXT, "Emergency").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'New patient')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'New Registration ')]").click()
    time.sleep(5)
    # danpheEMR.find_element(By.ID, "erPatFirstName").send_keys("ram")
    danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Add Unknown ER-Patient')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "erPatGender").send_keys("M")
    danpheEMR.find_element(By.XPATH, "//button[@id='register']").click()


def wait_for_window(danpheEMR, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
