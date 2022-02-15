import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Library.GlobalShareVariables as GSV

# danpheEMR = AC.danpheEMR
# print("DanpheEMR", danpheEMR)
AppName = GSV.appName


##########################
def collectLabSample(danpheEMR, HospitalNo, testname):
    global barcodeno
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Laboratory").click()
    time.sleep(5)
    try:
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'op-lab')]").click()
    except:
        print("No OP lab to select")
    time.sleep(5)
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),' Sample Collection ')]").click()
        danpheEMR.find_element(By.ID, "quickFilterInput").click()
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(Keys.RETURN)
        time.sleep(5)
        danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
        time.sleep(9)
        danpheEMR.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(9)
        barcodeno = danpheEMR.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) td:nth-child(3)").text
        print(barcodeno)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,'Close')]").click()


def addLabResult(danpheEMR):
    print("Starting>Adding Lab Report")
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Laboratory").click()
        time.sleep(1)
        danpheEMR.find_element(By.LINK_TEXT, "Add Results").click()
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(barcodeno)
        time.sleep(2)
        time.sleep(2)
        danpheEMR.find_element(By.LINK_TEXT, "Add Result").click()
        time.sleep(7)
        # ---------------this is hardcoded for TFT test-----------
        danpheEMR.find_element(By.ID, "inputbox000").send_keys("2.23")
        danpheEMR.find_element(By.ID, "inputbox001").send_keys("15.0")
        danpheEMR.find_element(By.ID, "inputbox002").send_keys("4.05")
        time.sleep(7)
        danpheEMR.find_element(By.XPATH, "//div[3]/button").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,'Proceed')]").click()  # proced for abnormal result
        time.sleep(3)
        danpheEMR.find_element(By.CSS_SELECTOR, ".c-btn > .fa").click()
        danpheEMR.find_element(By.ID, "btnUpdateSignatories").click()
        time.sleep(2)


def verifyLabReport(danpheEMR, HospitalNo):
    print("verifyLabReport:", verifyLabReport)
    if AppName == "LPH" or "SNCH":
        danpheEMR.find_element(By.LINK_TEXT, "PendingReports").click()
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        time.sleep(5)
        danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,'Verify ')]").click()


def printLabReport(danpheEMR, HospitalNo, t3, t4, tsh):
    danpheEMR.find_element(By.LINK_TEXT, "Laboratory").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Final Reports").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(7)
    # isprinted = danpheEMR.find_element(By.CSS_SELECTOR, "span > b").text
    # print(isprinted)
    # assert isprinted == "NO"
    # danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View Details')]").click()
    time.sleep(2)
    assert t3 == danpheEMR.find_element(By.XPATH, "//td[2]/span").text
    print(t3)
    sysT4 = danpheEMR.find_element(By.XPATH, "//tr[3]/td[2]/span").text
    print("SysT4:", sysT4)
    print("T4:", t4)
    # assert t4 == danpheEMR.find_element(By.XPATH, "//tr[3]/td[2]/span").text
    # print(t4)
    # assert tsh == danpheEMR.find_element(By.XPATH, "//tr[4]/td[2]/span").text
    # print(tsh)


def checkLabDuplicateRequisition(danpheEMR, HospitalNo, ItemName):
    print("Start>>checkLabDuplicateRequisition")
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Laboratory").click()
    time.sleep(5)
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),' Sample Collection ')]").click()
        danpheEMR.find_element(By.ID, "quickFilterInput").click()
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(Keys.RETURN)
        time.sleep(5)
        x = danpheEMR.find_element(By.XPATH, "//span[contains(text(),'No Rows To Show')]", ).text
        print("x", x)
        assert x == "No Rows To Show"
    print("End>>checkLabDuplicateRequisition")


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
