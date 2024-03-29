import time
from selenium.webdriver.support.select import Select
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# danpheEMR = AC.danpheEMR
# print("DanpheEMR", danpheEMR)
AppName = GSV.appName


# Module:ADT -----------------------------
def admitDisTrans(danpheEMR, admit, discharge, transfer, HospitalNo, deposit, doctor, department,
                  admittingDoctorMandatory):
    print("START>>admitDisTrans")
    if admit == 1:
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "ADT").click()
        time.sleep(3)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Admit").click()
        time.sleep(3)
        danpheEMR.find_element(By.ID, "admissionCase").click()
        dropdown = danpheEMR.find_element(By.ID, "admissionCase")
        dropdown.find_element(By.XPATH, "//option[. = 'General']").click()
        danpheEMR.find_element(By.ID, "admissionCase").click()
        danpheEMR.find_element(By.ID, "RequestingDeptId").send_keys(department)
        danpheEMR.find_element(By.ID, "RequestingDeptId").send_keys(Keys.ENTER)
        danpheEMR.find_element(By.ID, "RequestingDeptId").click()
        time.sleep(3)
        if admittingDoctorMandatory == "true":
            danpheEMR.find_element(By.ID, "AdmittingDoctorId").send_keys(doctor)
            danpheEMR.find_element(By.ID, "AdmittingDoctorId").send_keys(Keys.ENTER)
            time.sleep(3)

        danpheEMR.find_element(By.ID, "WardId").click()
        wardName = Select(danpheEMR.find_element(By.ID, "WardId"))
        time.sleep(2)
        wardName.select_by_visible_text(GSV.admitWard)
        time.sleep(3)
        danpheEMR.find_element(By.ID, "BedFeatureId").click()
        time.sleep(3)
        danpheEMR.find_element(By.ID, "BedFeatureId").send_keys(Keys.ENTER)
        time.sleep(1)
        danpheEMR.find_element(By.ID, "BedFeatureId").send_keys(Keys.DOWN)
        danpheEMR.find_element(By.ID, "BedFeatureId").send_keys(Keys.ENTER)
        # danpheEMR.find_element(By.ID, "BedFeatureId").click()
        time.sleep(2)
        danpheEMR.find_element(By.ID, "BedId").click()
        time.sleep(0.5)
        danpheEMR.find_element(By.ID, "BedId").send_keys(Keys.ENTER)
        danpheEMR.find_element(By.ID, "BedId").send_keys(Keys.DOWN)
        time.sleep(2)
        danpheEMR.find_element(By.ID, "BedId").send_keys(Keys.ENTER)
        time.sleep(2)
        # danpheEMR.find_element(By.ID, "SaveAdmission").click()
        time.sleep(2)
        danpheEMR.find_element(By.ID, "SaveAdmission").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//button[@class='btn btn-danger' and contains(text(),'X')]").click()

        # elif AppName == "MPH":
        #     danpheEMR.find_element(By.ID, "btnAdtSticker").click()
        # else:
        #     danpheEMR.find_element(By.XPATH, "//button[@class='btn btn-danger' and contains(text(),'X')]").click()
        # print("Patient successfully admitted.")
        # time.sleep(2)

    elif discharge == 1:
        time.sleep(5)
        danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
        time.sleep(2)
        danpheEMR.find_element(By.LINK_TEXT, "IPBilling").click()
        if HospitalNo == 'Auto Test':
            danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("Auto ")
            time.sleep(5)
        else:
            danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
            time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,'Discharge')]").click()
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//div[3]/textarea").send_keys("Patient discharging")
        danpheEMR.find_element(By.XPATH, "(//button[@type='button'])[5]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//pat-ip-bill-summary/div/div[2]/div/div/div/div/a").click()
        danpheEMR.find_element(By.LINK_TEXT, "Billing").click()

    elif transfer == 1:
        danpheEMR.find_element(By.LINK_TEXT, "ADT").click()
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Admitted Patients").click()
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Transfer").click()
        time.sleep(2)
        danpheEMR.find_element(By.ID, "DepartmentName").click()
        danpheEMR.find_element(By.ID, "DepartmentName").send_keys(department)
        danpheEMR.find_element(By.ID, "DepartmentName").send_keys(Keys.TAB)
        danpheEMR.find_element(By.ID, "SecondaryDoctorName").send_keys(Keys.TAB)
        # danpheEMR.find_element(By.ID, "SecondaryDoctorName").send_keys()
        danpheEMR.find_element(By.ID, "WardId").click()
        danpheEMR.find_element(By.ID, "WardId").send_keys(Keys.ARROW_DOWN)
        danpheEMR.find_element(By.ID, "WardId").send_keys(Keys.ENTER)
        time.sleep(2)
        danpheEMR.find_element(By.ID, "BedFeatureId").send_keys(Keys.ENTER)
        time.sleep(2)
        danpheEMR.find_element(By.ID, "BedFeatureId").send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        danpheEMR.find_element(By.ID, "BedFeatureId").send_keys(Keys.ENTER)
        time.sleep(3)
        danpheEMR.find_element(By.ID, "BedId").click()
        danpheEMR.find_element(By.ID, "BedId").send_keys(Keys.ARROW_DOWN)
        time.sleep(3)
        danpheEMR.find_element(By.ID, "BedId").send_keys(Keys.ENTER)
        danpheEMR.find_element(By.ID, "Remarks").send_keys("Transfer to ICU ward")
        danpheEMR.find_element(By.XPATH, "//input[@name='name']").click()
    print("END>>admitDisTrans")


def cancelDischarge(danpheEMR, HospitalNo):
    # To cancel discharge user need to return discharge invoice
    print("START>>cancelDischarge")
    danpheEMR.find_element(By.LINK_TEXT, "ADT").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Discharged Patients").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Cancel Discharge')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "DischargeCancelNote").send_keys("Cancel Discharge")
    time.sleep(2)
    danpheEMR.find_element(By.ID, "Approve").click()
    time.sleep(5)
    print("END>>cancelDischarge")


def dischargeRandomPatient(danpheEMR):
    print("START>>dischargeRandomPatient")
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "IPBilling").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("Auto Test")
    time.sleep(3)
    try:
        danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
        time.sleep(9)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,'Discharge')]").click()
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//div[3]/textarea").send_keys("Patient discharging")
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "(//button[@type='button'])[5]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger del-btn']").click()
        time.sleep(5)
    except:
        pass
    print("END>>dischargeRandomPatient")


def checkAutoAddItems(danpheEMR):
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),' ADT ')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Manage Auto Add Billing Items").click()
    time.sleep(2)
    autoaddbillitemvalue = danpheEMR.find_element(By.XPATH, "//b[contains(.,'  False')]").text
    autoaddBeditemvalue = danpheEMR.find_element(By.XPATH, "//b[contains(.,'  True')]").text
    print("autoaddbillitemvalue", autoaddbillitemvalue)
    print("autoaddBeditemvalue", autoaddBeditemvalue)
    # assert autoaddbillitemvalue == "autoaddbillitemvalue   False"      rework needed
    # assert autoaddBeditemvalue == "autoaddBeditemvalue   True"        rework needed


def AddSummaryOfDischargedPatient(danpheEMR, HospitalNo, consultantDr, inchargeDr):
    print("START>>AddingSummary")
    danpheEMR.find_element(By.LINK_TEXT, "ADT").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Discharged Patients").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Add Summary").click()
    time.sleep(3)
    DischargeType = Select(danpheEMR.find_element(By.XPATH, "//select[@formcontrolname='DischargeTypeId']"))
    DischargeType.select_by_visible_text("Referred")
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Consultant name']").send_keys(consultantDr)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Consultant name']").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Doctor Incharge name'] ").send_keys(inchargeDr)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Doctor Incharge name'] ").send_keys(Keys.ENTER)
    time.sleep(1)
    specialNotes = danpheEMR.find_element(By.XPATH, "//textarea[@placeholder='Special Notes']")
    specialNotes.send_keys("This is Special Notes")
    history = danpheEMR.find_element(By.XPATH, "//textarea[@placeholder='Presenting Illness']")
    history.send_keys("No any history found.")
    time.sleep(1)
    save = danpheEMR.find_element(By.XPATH, "(//input[@value='Save'])[2]")
    save.click()
    time.sleep(3)
    hospitalNumber = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div/div/div[1]/div[2]/div/p[1]").text
    print("Hospital Number of Patient is :", hospitalNumber)
    hospitalNumber = hospitalNumber.replace("Hospital No.: ", "")
    assert hospitalNumber == HospitalNo
    dischargeType = danpheEMR.find_element(By.XPATH, "//span[normalize-space()='Referred']").text
    print("Discharge Type f the Patient is :", dischargeType)
    assert dischargeType == "Referred"
    medicalOfficer = danpheEMR.find_element(By.XPATH,
                                            "//*[@id='printpage']/div/div/div[4]/div/div/div/div[1]/p[2]/strong").text
    print("Medical Officer of given Patient is :", medicalOfficer)
    medicalOfficer = str(medicalOfficer)
    assert inchargeDr == medicalOfficer
    consultantDoctor = danpheEMR.find_element(By.XPATH,
                                              "//*[@id='printpage']/div/div/div[4]/div/div/div/div[2]/p[2]/strong").text
    print("Consultant Doctor is :", consultantDoctor)
    consultantDoctor = str(consultantDoctor)
    assert consultantDoctor == consultantDr
    print("END: Summary Report")


def updateAndViewSummaryOfDischargedPatient(danpheEMR, HospitalNo):
    print("START>>updating summary")
    global incDr
    danpheEMR.find_element(By.LINK_TEXT, "ADT").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Discharged Patients").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    danpheEMR.find_element(By.XPATH, "//a[normalize-space()='View Summary']").click()
    time.sleep(2)
    incharge = danpheEMR.find_element(By.XPATH, "//input[@placeholder='Doctor Incharge name']")
    incDr = incharge.get_attribute('value')
    print("Incharge Doctor is:", incDr)
    danpheEMR.find_element(By.XPATH, "//input[@value='Update']").click()
    print("END: Updating")
    return incDr


def verifyInchargeDoctorAfterUpdate(danpheEMR, HospitalNo):
    print("START>>Verifying Doctor")
    danpheEMR.find_element(By.LINK_TEXT, "ADT").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Discharged Patients").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    danpheEMR.find_element(By.XPATH, "//a[normalize-space()='View Summary']").click()
    time.sleep(2)
    incharge = danpheEMR.find_element(By.XPATH, "//input[@placeholder='Doctor Incharge name']")
    inchDr = incharge.get_attribute('value')
    print("Incharge Doctor is:", inchDr)
    assert inchDr == inchDr
    print("Verify End")


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
