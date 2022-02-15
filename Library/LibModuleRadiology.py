import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Library.GlobalShareVariables as GSV

########
# danpheEMR = AC.danpheEMR
AppName = GSV.appName


########
# Module:Radiology ***************************
def doRadioScan(danpheEMR, HospitalNo):
    print(">>START: doRadioScan")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Radiology").click()
        time.sleep(5)
        danpheEMR.find_element(By.LINK_TEXT, "List Requests").click()
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Scan Done").click()
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,'Done')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Add Report')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//input[@value='Save']").click()
        time.sleep(5)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(Keys.ESCAPE)
    print("<<END: doRadioScan")


def wait_for_window(danpheEMR, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
