import time
import Library.GlobalShareVariables as gSV
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

AppName = gSV.appName


def addTriage(danpheEMR, hospitalNumber, Height, Weight, Temperature, Pulse, BPSystolic, BPDiastolic, RespirotaryRate, SPO2, BodyPart):
    print("START: Adding Outpatient Triage")
    danpheEMR.find_element(By.LINK_TEXT, "Nursing").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(hospitalNumber)
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'Add Triage')]").click()
    time.sleep(2)
    height = danpheEMR.find_element(By.XPATH, "//*[@id='vitalsSection']/div/div/div[2]/vitals-add/div/div[2]/div[2]/div[1]/input")
    height.send_keys(Height)
    weight = danpheEMR.find_element(By.XPATH, "//*[@id='vitalsSection']/div/div/div[2]/vitals-add/div/div[2]/div[3]/div[1]/input")
    weight.send_keys(Weight)
    temperature = danpheEMR.find_element(By.XPATH, "//*[@id='vitalsSection']/div/div/div[2]/vitals-add/div/div[2]/div[5]/div[1]/input")
    temperature.send_keys(Temperature)
    pulse = danpheEMR.find_element(By.XPATH, "//*[@id='vitalsSection']/div/div/div[2]/vitals-add/div/div[2]/div[6]/div[1]/input")
    pulse.send_keys(Pulse)
    bpSystolic = danpheEMR.find_element(By.NAME, "BPSystolic")
    bpSystolic.send_keys(BPSystolic)
    bpDiastolic = danpheEMR.find_element(By.NAME, "BPDiastolic")
    bpDiastolic.send_keys(BPDiastolic)
    respirotaryRate = danpheEMR.find_element(By.XPATH, "//*[@id='vitalsSection']/div/div/div[2]/vitals-add/div/div[2]/div[8]/div[1]/input")
    respirotaryRate.send_keys(RespirotaryRate)
    spo2 = danpheEMR.find_element(By.XPATH, "//input[@placeholder = 'SpO2']")
    spo2.send_keys(SPO2)
    # bodyPain = danpheEMR.find_element(By.ID, "bodyPart")
    # bodyPain.send_keys(BodyPart)
    save = danpheEMR.find_element(By.NAME, "name")
    save.click()
    time.sleep(1)
    chiefComplaint = danpheEMR.find_element(By.CSS_SELECTOR, ".flex-container:nth-child(1)")
    chiefComplaint.send_keys("This is chief complaints")
    danpheEMR.find_element(By.XPATH, "//button[contains(text(), ' Add Triage')] ").click()


def outPatientOverview(danpheEMR, hospitalNumber, IsTriageDone):
    print("START: Opening OutPatient Overview ")
    danpheEMR.find_element(By.LINK_TEXT, "Nursing").click()
    time.sleep(5)
    if IsTriageDone == "yes":
        danpheEMR.find_element(By.XPATH, "//a[@href = '#taken']").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "(//input[@id = 'quickFilterInput'])[2]").send_keys(hospitalNumber)
    else:
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(hospitalNumber)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[@title = 'overview']").click()
    print("END: Outpatient Overview Opened")


def inPatientOverview(danpheEMR, wardName, hospitalNumber):
    print("START: Opening inpatient Overview")
    danpheEMR.find_element(By.LINK_TEXT, "Nursing").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),  'In Patient')] ").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + wardName + "')]").click()
    time.sleep(2)
    Expected_text = "Doctor Name"
    Actual_text = danpheEMR.find_element(By.XPATH, "//span[normalize-space()='Doctor Name']").text
    print(Actual_text)
    assert Expected_text == Actual_text
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(hospitalNumber)
    danpheEMR.find_element(By.XPATH, "//i[@title = 'overview']").click()
    print("END:Inpatient Overview Opened")


def addNotes(danpheEMR, Template):
    print("START: Adding Notes")
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'Notes')]").click()
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'Add Notes')]").click()
    danpheEMR.find_element(By.XPATH, "//input[@placeholder = 'Select Template']").send_keys(Template)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder = 'Select Template']").send_keys(Keys.ENTER)
    time.sleep(3)
    if Template == "Progress Note":
        time.sleep(1)
        subjectiveNote = danpheEMR.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .col-md-8 > .form-control")
        subjectiveNote.send_keys("This is  Subjective Notes")
        objectiveNote = danpheEMR.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .col-md-8 > .form-control")
        objectiveNote.send_keys("This is Objective Notes")
        instruction = danpheEMR.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > .col-md-8 > .form-control")
        instruction.send_keys("This is Instructions")
    elif Template == "History & Physical" or "Consult Note":
        time.sleep(2)
        historyIllness = danpheEMR.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .col-md-8 > .ng-pristine")
        historyIllness.send_keys("This is History of Presenting illness")
        time.sleep(2)
        reviewSystem = danpheEMR.find_element(By.CSS_SELECTOR, ".form-group > .col-md-8 > .ng-pristine")
        reviewSystem.send_keys("This is the Review of System")
    elif Template == "Emergency Note":
        time.sleep(2)
        stretcher = danpheEMR.find_element(By.CSS_SELECTOR, ".mt-checkbox:nth-child(2) > span")
        stretcher.click()
        broughtBy = danpheEMR.find_element(By.XPATH, "//div[3]/div/div/div/div/input")
        broughtBy.send_keys("Unknown")
        phoneNumber = danpheEMR.find_element(By.CSS_SELECTOR, ".col-md-6:nth-child(3) .form-control")
        phoneNumber.send_keys(9851012034)
        courseDescription = danpheEMR.find_element(By.XPATH, "//textarea[@placeholder = 'Enter Er course description']")
        courseDescription.send_keys("This is the ER course Description")
        time.sleep(1)
        heent = danpheEMR.find_element(By.CSS_SELECTOR, ".cstm-form-group:nth-child(2) .ng-untouched")
        heent.send_keys("This is the Heent")
        chest = danpheEMR.find_element(By.CSS_SELECTOR, ".cstm-form-group:nth-child(3) .ng-untouched")
        chest.send_keys("Need to do Xray ")
    else:
        print("Please Select the Valid Templete")
    danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Save')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//*[contains(text(), 'Home')]").click()
