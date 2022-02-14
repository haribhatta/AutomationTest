import time
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import random
########
AppName = GSV.appName
########
#Module:Incentive ******************

def ExistingPatientNewVisit(danpheEMR, HospitalNo, Department):
    global NSHI
    print("Start >> Existing Patient Registration")
    danpheEMR.find_element(By.LINK_TEXT, "GovInsurance").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "allPatWithOutIns").click()
    danpheEMR.find_element(By.ID, "allPatWithOutIns").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "allPatWithOutIns").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "allPatWithOutIns").send_keys(Keys.TAB)
    NSHI = str(random.randint(11111, 99999))
    danpheEMR.find_element(By.ID, "Ins_NshiNumber").send_keys(NSHI)
    danpheEMR.find_element(By.ID, "Ins_InsuranceBalance").send_keys(50000)
    dropdown = Select(danpheEMR.find_element(By.ID, "firstServicePoint"))
    dropdown.select_by_visible_text("Yes")
    dropdown = Select(danpheEMR.find_element(By.ID, "IsFamilyHead"))
    dropdown.select_by_visible_text("Yes")
    danpheEMR.find_element(By.ID, "update").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(NSHI)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "New Visit").click()
    danpheEMR.find_element(By.ID, "txtDepartment").send_keys(Department)
    danpheEMR.find_element(By.ID, "txtDepartment").send_keys(Keys.TAB)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btnPrintInvoice").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btnPrintInsSticker").send_keys(Keys.ESCAPE)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Insurance Billing").click()


def insurancePatientRegistration(danpheEMR):
      global NSHI
      time.sleep(5)
      print("Start >> Insurance Patient Registration")
      danpheEMR.find_element(By.LINK_TEXT, "GovInsurance").click()
      time.sleep(3)
      danpheEMR.find_element(By.LINK_TEXT, "Patient List").click()
      time.sleep(3)
      danpheEMR.find_element(By.ID, "btnNewInsurancePat").click()
      fname = str(random.randint(1111, 9999))
      time.sleep(3)
      danpheEMR.find_element(By.ID, "aptPatFirstName").send_keys("insu", fname)
      time.sleep(3)
      #danpheEMR.find_element(By.ID, "middleName").send_keys("Patient")
      danpheEMR.find_element(By.ID, "lastName").send_keys("registration")
      time.sleep(3)
      dropdown = danpheEMR.find_element(By.ID, "selGender")
      dropdown.find_element(By.XPATH, "//option[. = 'Male']").click()
      danpheEMR.find_element(By.ID, "selGender").click()
      danpheEMR.find_element(By.ID, "age").send_keys(5)
      NSHI = str(random.randint(1111111111, 9999999999))
      danpheEMR.find_element(By.ID, "Ins_NshiNumber").send_keys(NSHI)
      danpheEMR.find_element(By.ID, "Ins_InsuranceBalance").send_keys(50000)
      fps = Select(danpheEMR.find_element(By.ID, "firstServicePoint"))
      fps.select_by_visible_text("Yes")
      time.sleep(3)
      familyhead = Select(danpheEMR.find_element(By.ID, "IsFamilyHead"))
      familyhead.select_by_visible_text("Yes")
      danpheEMR.find_element(By.ID, "register").click()

      return NSHI



def insuranceNewVisit(danpheEMR, NSHI):
      global HospitalNo
      print(">> Start: Create insurance patient new visit")
      danpheEMR.find_element(By.LINK_TEXT, "GovInsurance").click()
      time.sleep(3)
      danpheEMR.find_element(By.LINK_TEXT, "Patient List").click()
      time.sleep(3)
      danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(NSHI)
      time.sleep(2)
      danpheEMR.find_element(By.XPATH, "//a[contains(text(),'New Visit')]").click()
      time.sleep(2)
      danpheEMR.find_element(By.ID, "txtDepartment").send_keys("GYNAE & OBS")
      time.sleep(3)
      danpheEMR.find_element(By.ID, "txtDepartment").send_keys(Keys.RETURN)
      time.sleep(2)
      danpheEMR.find_element(By.ID, "btnPrintInvoice").click()
      time.sleep(3)
      HospitalNo = danpheEMR.find_element(By.XPATH, "//strong[contains(text(), 'Hospital No:')]/parent::p/child::span/child::strong").text
      print("HospitalNo:", HospitalNo)
      danpheEMR.find_element(By.ID, "btnPrintInsSticker")
      danpheEMR.find_element(By.ID, "btnPrintInsSticker").send_keys(Keys.ESCAPE)
      return HospitalNo

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

def getInsurancePatientBimaSummaryValue(danpheEMR):
    global summaryValue
    danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Insurance Patients (BIMA)')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(2)
    summaryValue = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr/td[2]/span").text
    print("Summary Value is :", summaryValue)
    summaryValue = int(summaryValue)
    print("Summary value of Insurance Bima is ", summaryValue)

def preInsurancePatientBimaSummaryValue():
    global presummaryValue
    presummaryValue = summaryValue
    print("PreSummary Value is :", presummaryValue)

def verifyinsurancePatientBimaSummaryValue(rate):
    print("Start >> Verifying Insurance sale summary")
    assert presummaryValue == summaryValue - rate
    print("END>> Insurance Sales Summary Verified")

def insuranceDispensarySell(danpheEMR, NSHINO , genericname, drugname):
    global PreInvoiceNo
    print("Start >> insurance Dispensary Sell")
    time.sleep(3)
    danpheEMR.find_element(By.ID, "patient-search").send_keys(NSHINO)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "patient-search").send_keys(Keys.DOWN)
    danpheEMR.find_element(By.ID, "patient-search").send_keys(Keys.ENTER)
    time.sleep(2)
    # danpheEMR.find_element(By.ID, "currentRequestedByDoctor").send_keys("DR RISHAV SUBEDI")
    danpheEMR.find_element(By.ID, "currentRequestedByDoctor").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "generic0").send_keys(genericname)
    danpheEMR.find_element(By.ID, "generic0").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "item-box0").send_keys(drugname)
    danpheEMR.find_element(By.ID, "item-box0").send_keys(Keys.ENTER)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "qty0").send_keys(1)
    danpheEMR.find_element(By.ID, "qty0").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.XPATH, "//button[@title='ALT + P']").click()
    time.sleep(2)
    PreInvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    print("PreInvoiceNo", PreInvoiceNo)
    PreInvoiceNo = PreInvoiceNo.partition("PH")[2]
    print("PreInvoiceNo", PreInvoiceNo)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "btnPrintPhrmInvoice")
    danpheEMR.find_element(By.ID, "btnPrintPhrmInvoice").send_keys(Keys.ESCAPE)
    return PreInvoiceNo
    print("END >> insurance Dispensary Sell")


def NewInsurancePatientBilling(danpheEMR, NSHI, lab):
    global PreInvoiceNo
    print("Start >>> NewInsurancePatientBilling <<<")
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "GovInsurance").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Patient List").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(NSHI)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Insurance Billing')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "items-box0").send_keys(lab)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "items-box0").send_keys(Keys.ENTER)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quantity_0").send_keys(1)
    danpheEMR.find_element(By.ID, "quantity_0").send_keys(Keys.ENTER)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "btn_printInvoice").click()
    time.sleep(2)
    PreInvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    print("PreInvoiceNo", PreInvoiceNo)
    PreInvoiceNo = PreInvoiceNo.partition("INS")[2]
    print("PreInvoiceNo", PreInvoiceNo)
    time.sleep(2)
    element = danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger del-btn']")
    time.sleep(2)
    danpheEMR.execute_script("arguments[0].click();", element)
    time.sleep(5)
    return PreInvoiceNo
    print("Create OPD Invoice: 1 Lab Items: END<<")


def PatientWiseClaimReport(danpheEMR, HospitalNo, PreInvoiceNo):
    print("Start >>> PatientWiseClaimReport <<<")
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "GovInsurance").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Patient List").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "/html/body/my-app/div/div/div[3]/div[2]/div/div/app-insurance/div[1]/ul/li[4]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Ins Patient Wise Claims')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "btn_showClaims").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,"//div/div[2]/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr/td[3]/button").click()
    time.sleep(2)
    print("PreInvoice:", PreInvoiceNo)
    Invoice = danpheEMR.find_element(By.XPATH, "//td[contains(text(),' "+PreInvoiceNo+"')]").text
    print("Invoice : ", Invoice)
    assert PreInvoiceNo == Invoice
    danpheEMR.find_element(By.XPATH, "//button[@class='btn btn-danger' and contains(text(),'X')]").click()
    time.sleep(3)





def wait_for_window(danpheEMR, timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars("window_handles")
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

