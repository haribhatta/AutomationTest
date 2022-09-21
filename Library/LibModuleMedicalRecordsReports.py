from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import Library.GlobalShareVariables as GSV

AppName = GSV.appName
HospitalNo = None


# Module:Appointment --------------------
def getHospitalServiceSummaryReport(danpheEMR):
    print(">>START: getHospitalServiceSummaryReport")
    global actualTotalPatientsAdmitted
    global actualTotalLabSeriveProvided
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        time.sleep(2)
        danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),' Reports ')]").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Hospital Service Summary Report')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//button[contains(text(),' Show Report ')]").click()
        time.sleep(14)
        actualTotalPatientsAdmitted = danpheEMR.find_element(By.XPATH,
                                                             "//b[contains(text(),'Total Patients Admitted')]/parent::td/following-sibling::td").text
        actualTotalPatientsAdmitted = int(actualTotalPatientsAdmitted)
        print("actualTotalPatientsAdmitted:", actualTotalPatientsAdmitted)
        actualTotalLabSeriveProvided = danpheEMR.find_element(By.XPATH,
                                                              "//td[contains(text(),'Total Laboratory Service Provided')]/following-sibling::td[2]").text
        print("actualTotalLabSeriveProvided:", actualTotalLabSeriveProvided)
        actualTotalLabSeriveProvided = int(actualTotalLabSeriveProvided)
        print("actualTotalLabSeriveProvided:", actualTotalLabSeriveProvided)
    print("<<END: getHospitalServiceSummaryReport")


def preHospitalServiceSummaryReport(danpheEMR):
    print("Start >> assignHospitalServiceSummaryReport")
    ######## Code goes here
    global preTotalPatientsAdmitted
    global preTotalLabSeriveProvided
    preTotalPatientsAdmitted = actualTotalPatientsAdmitted
    preTotalLabSeriveProvided = actualTotalLabSeriveProvided
    print("End >> assignHospitalServiceSummaryReport")


def verifyHospitalServiceSummaryReport(danpheEMR, labBill, admit):
    print("Start >> verifyHospitalServiceSummaryReport")
    ######## Code goes here
    global expectedTotalPatientsAdmitted
    global expectedTotalLabSeriveProvided
    expectedTotalPatientsAdmitted = preTotalPatientsAdmitted + admit
    print("expectedTotalPatientsAdmitted:", expectedTotalPatientsAdmitted)
    assert expectedTotalPatientsAdmitted == actualTotalPatientsAdmitted
    expectedTotalLabServiceProvided = preTotalLabSeriveProvided + labBill
    print("expectedTotalLabServiceProvided:", expectedTotalLabServiceProvided)
    assert expectedTotalLabServiceProvided == actualTotalLabSeriveProvided
    print("End >> verifyHospitalServiceSummaryReport")


def getInpatientMorbidityReport(danpheEMR):
    print(">>START: getInpatientMorbidityReport")
    global femaleDeath
    global maleDeath
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        time.sleep(2)
        danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),' Reports ')]").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Inpatient Morbidity Report')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//button[contains(text(),' Show Report ')]").click()
        time.sleep(4)
        femaleDeath = danpheEMR.find_element(By.XPATH, "//td[contains(text(),'TOTAL')]/following-sibling::td[25]").text
        femaleDeath = int(femaleDeath)
        print("Total Female Death is :", femaleDeath)
        maleDeath = danpheEMR.find_element(By.XPATH, "//td[contains(text(),'TOTAL')]/following-sibling::td[26]").text
        maleDeath = int(maleDeath)
        print("Total Male Death is :", maleDeath)
    print("<<END: getInpatientMorbidityReport")


def storeInpatientMorbidityReport(danpheEMR):
    print("Start >> assignInpatientMorbidityReport")
    global premaleDeath
    global prefemaleDeath
    prefemaleDeath = femaleDeath
    prefemaleDeath = int(prefemaleDeath)
    print("Current Female Death Number is :", prefemaleDeath)
    premaleDeath = maleDeath
    premaleDeath = int(premaleDeath)
    print("Current Male Death is :", premaleDeath)
    print("End >> assignInpatientMorbidityReport")


def verifyInpatientMorbidityReport(danpheEMR):
    print("Start >> verifyInpatientMorbidityReport")
    assert femaleDeath == prefemaleDeath + 1  # need to change later in male and female Death after total is shown
    print("End >> verifyInpatientMorbidityReport")


def wait_for_window(danpheEMR, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
