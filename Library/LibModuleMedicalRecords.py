import random
from selenium.common.exceptions import NoSuchElementException
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
AppName = GSV.appName
HospitalNo = None
# Module:Appointment --------------------
def addBirthCertificate(danpheEMR, HospitalNo):
   print(">>START: addBirthCertificate")
   if  AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
      time.sleep(2)
      danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
      time.sleep(5)
      danpheEMR.find_element(By.LINK_TEXT, "Birth List").click()
      time.sleep(3)
      danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'Add New Birth Certificate')]").click()
      time.sleep(4)
      danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
      time.sleep(3)
      danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
      time.sleep(3)
      number = str(random.randint(1, 9999))
      danpheEMR.find_element(By.ID, "certNum").send_keys(number)
      print(number)
      time.sleep(3)
      birthCondition = Select(danpheEMR.find_element(By.ID, "ddlBirthCondition"))
      birthCondition.select_by_visible_text("Live Birth")
      gender = Select(danpheEMR.find_element(By.ID, "sex"))
      gender.select_by_visible_text("Male")
      time.sleep(3)
      danpheEMR.find_element(By.ID, "babyWt").send_keys(2)
      time.sleep(5)
      # birthType = Select(danpheEMR.find_element(By.ID, "ddlBirthType")).click()
      # birthType.select_by_visible_text(" Spontaneous Vaginal Delivery")
      # time.sleep(3)
      danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Add Certificate')]").click()
      time.sleep(5)
      danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Submit')]").click()
      # return number for the verifying the certificate number

      return number
   print("<<END: addBirthCertificate")

def verifyaddbirthCertificate(danpheEMR , certNo):
   print("Verifying Certificate Start")
   time.sleep(2)
   danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
   time.sleep(3)
   danpheEMR.find_element(By.LINK_TEXT, "Birth List").click()
   time.sleep(3)
   danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(certNo)
   time.sleep(2)
   try:
      danpheEMR.find_element(By.XPATH,  "(//a[contains(text(),'Certificate')])[2]").click()
      danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Cancel')]").click()
      print("End of Verifying Certificate")

   except NoSuchElementException:
       print("Not verified")
       raise NoSuchElementException("FileNotFoundError")


def addMRwithDischargeTypeDeath(danpheEMR, HospitalNo):
   print(">>START: addMRwithDischargeTypeDeath")
   ######## add MR with discharge Type = Death goes here
   if  AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
      time.sleep(2)
      danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
      time.sleep(5)
      danpheEMR.find_element(By.LINK_TEXT, "MR Inpatient List").click()
      time.sleep(3)
      danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Load Patients')]").click()
      danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'Add MR')]").click()
      time.sleep(3)
      dischargeType = Select(danpheEMR.find_element(By.XPATH, "//div[4]/div[2]/select"))
      dischargeType.select_by_visible_text("Death")
      time.sleep(3)
      dischargeCondition = Select(danpheEMR.find_element(By.CSS_SELECTOR, ".row:nth-child(5) .cstm-field-sel"))
      dischargeCondition.select_by_visible_text('Post Operative Death')
      time.sleep(3)
      deathPeriod = Select(danpheEMR.find_element(By.CSS_SELECTOR, ".row:nth-child(6) .cstm-field-sel"))
      time.sleep(1)
      deathPeriod.select_by_visible_text("<48")
      danpheEMR.find_element(By.ID, "icd10code").send_keys("A00 | Cholera")
      time.sleep(3)
      danpheEMR.find_element(By.ID, "icd10code").send_keys(Keys.RETURN)
      time.sleep(3)
      # number = str(random.randint(1, 9999))
      # danpheEMR.find_element(By.ID, "certNum").send_keys(number)
      # print(number)
      # danpheEMR.find_element(By.ID, "Submit").click()
      element = danpheEMR.find_element(By.ID, "Submit")
      action = ActionChains(danpheEMR)
      action.double_click(element).perform()
      time.sleep(10)
      # danpheEMR.find_element(By.ID, "certNum").send_keys()
      addrecords = danpheEMR.find_element(By.CSS_SELECTOR, ".all-buttons > .green")
      record = ActionChains(danpheEMR)
      record.double_click(addrecords).perform()
      time.sleep(3)
   print(">>End: addMRwithDischargeTypeDeath")


def addMultipleBirthDetailAndMultipleCertificate(danpheEMR, HospitalNo):
   print("Adding multiple birth details")
   danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
   time.sleep(5)
   danpheEMR.find_element(By.LINK_TEXT, "Birth List").click()
   time.sleep(3)
   danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Add New Birth Certificate')]").click()
   time.sleep(4)
   danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
   time.sleep(3)
   danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
   time.sleep(3)
   number = str(random.randint(1, 9999))
   danpheEMR.find_element(By.ID, "certNum").send_keys(number)
   print("Certificate number is ", number)
   number = int(number)
   time.sleep(3)
   birthCondition = Select(danpheEMR.find_element(By.ID, "ddlBirthCondition"))
   birthCondition.select_by_visible_text("Live Birth")
   gender = Select(danpheEMR.find_element(By.ID, "sex"))
   gender.select_by_visible_text("Male")
   time.sleep(3)
   danpheEMR.find_element(By.ID, "babyWt").send_keys(2)
   time.sleep(2)
   birthNumber = Select(danpheEMR.find_element(By.ID, "ddlBirthNumberType"))
   birthNumber.select_by_visible_text("Multiple")
   danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Add Certificate')]").click()
   numbers = number + 1
   print("certificate number of another child is:", numbers)
   danpheEMR.find_element(By.ID, "certNum").send_keys(numbers)
   birthCondition = Select(danpheEMR.find_element(By.ID, "ddlBirthCondition"))
   birthCondition.select_by_visible_text("Live Birth")
   gender = Select(danpheEMR.find_element(By.ID, "sex"))
   gender.select_by_visible_text("Male")
   time.sleep(3)
   danpheEMR.find_element(By.ID, "babyWt").send_keys(4)
   time.sleep(2)
   birthNumber = Select(danpheEMR.find_element(By.ID, "ddlBirthNumberType"))
   birthNumber.select_by_visible_text("Twins")
   danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Add Certificate')]").click()
   danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
   print("END: adding Multiple Birth Details")


def addBirthDetailsFromMRInpatientList(danpheEMR, HospitalNo, babyWeight):
   print("Adding birth details from MR Inpatient List")
   danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
   time.sleep(2)
   danpheEMR.find_element(By.XPATH, "//button[contains(text(), ' Load Patients ')]").click()
   time.sleep(2)
   danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
   time.sleep(3)
   danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Add MR')]").click()
   time.sleep(5)
   dischargeType = Select(danpheEMR.find_element(By.CSS_SELECTOR, ".cstm-field-sel"))
   dischargeType.select_by_visible_text("Recovered")
   time.sleep(5)
   dischargeCondition = Select(danpheEMR.find_element(By.XPATH, "//div[4]/div[2]/select"))
   time.sleep(1)
   dischargeCondition.select_by_visible_text("Delivery")
   time.sleep(3)
   number = str(random.randint(1, 9999))
   danpheEMR.find_element(By.ID, "certNum").send_keys(number)
   print("Certificate number is ", number)
   number = int(number)
   time.sleep(3)
   birthCondition = Select(danpheEMR.find_element(By.ID, "ddlBirthCondition"))
   birthCondition.select_by_visible_text("Live Birth")
   gender = Select(danpheEMR.find_element(By.ID, "sex"))
   gender.select_by_visible_text("Male")
   time.sleep(3)
   danpheEMR.find_element(By.ID, "babyWt").send_keys(babyWeight)
   time.sleep(2)
   birthNumber = Select(danpheEMR.find_element(By.ID, "ddlBirthNumberType"))
   birthNumber.select_by_visible_text("Multiple")
   danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Add Certificate')]").click()
   time.sleep(1)
   danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Add Record')]").click()
   return babyWeight


# this is to assert the edited weight for bug EMR-4580


def OutpatientList(danpheEMR, HospitalNo, DoctorName):
   time.sleep(5)
   danpheEMR.find_element(By.XPATH, "//span[normalize-space()='MedicalRecords']").click()
   time.sleep(5)
   danpheEMR.find_element(By.XPATH, "//a[contains(text(),'MR Outpatient List')]").click()
   # time.sleep(2)
   # danpheEMR.find_element(By.XPATH, "//input[@placeholder='Doctor Name']").send_keys(DoctorName)
   # danpheEMR.find_element(By.XPATH, "//input[@placeholder='Doctor Name']").send_keys(Keys.ENTER)
   time.sleep(2)
   danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
   time.sleep(3)
   doctorname = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[5]").text
   print("doctor name is :", doctorname)
   doctorname = str(doctorname)
   print(doctorname)
   # assert doctorname == DoctorName


def addFinalDiagnosisOutPatient(danpheEMR, isReferredOutpatient, diagnosis):
   print("Start Adding Final Diagnosis of OutPatient")
   danpheEMR.find_element(By.LINK_TEXT, "Add Final Diagnosis").click()
   if isReferredOutpatient == 'yes':
      danpheEMR.find_element(By.ID, "referredOutoutpatient").click()
      time.sleep(5)
      danpheEMR.find_element(By.XPATH, "//label[@for='ReferredBy']/following-sibling::input").click()
      danpheEMR.find_element(By.XPATH, "//label[@for='ReferredBy']/following-sibling::input").send_keys("Dr.Buddha Karki")
   danpheEMR.find_element(By.XPATH, "//input[@placeholder='ICD-11']").click()
   danpheEMR.find_element(By.XPATH, "//input[@placeholder='ICD-11']").send_keys(diagnosis)
   danpheEMR.find_element(By.XPATH, "//input[@placeholder='ICD-11']").send_keys(Keys.ENTER)
   danpheEMR.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]").click()
   print("END: Adding Final Diagnosis of OutPatient")


def editFinalDiagnosisOutPatient(danpheEMR, diagnosis):
   print("Editing the Final Diagnosis of OutPatient:")
   danpheEMR.find_element(By.XPATH, "(//a[normalize-space()='Edit Final Diagnosis'])[1]").click()
   danpheEMR.find_element(By.XPATH, "//input[@placeholder='ICD-11']").click()
   danpheEMR.find_element(By.XPATH, "//input[@placeholder='ICD-11']").send_keys(diagnosis)
   danpheEMR.find_element(By.XPATH, "//input[@placeholder='ICD-11']").send_keys(Keys.ENTER)
   danpheEMR.find_element(By.XPATH, "(//button[normalize-space()='Update'])[1]").click()
   print("END: Editing final Diagnosis of OutPatient")



def editBirthDetailsfromMRInpatientList(danpheEMR, editedWeight):
   time.sleep(3)
   print("Editing birth details from MR Inpatient List")
   danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View MR')]").click()
   time.sleep(2)
   danpheEMR.find_element(By.XPATH, " //button[contains(text(), 'Edit Record ')]").click()
   time.sleep(2)
   danpheEMR.find_element(By.XPATH, "//button[@title = 'edit']").click()
   danpheEMR.find_element(By.ID, "babyWt").clear()
   danpheEMR.find_element(By.ID, "babyWt").send_keys(editedWeight)
   time.sleep(2)
   danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Update Birth Certificate')]").click()
   danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Update Record')]").click()
   time.sleep(2)
   preweight = danpheEMR.find_element(By.XPATH,
                                      "//*[@id='patMrRecordDetail']/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/p").text
   print("Weight of the baby is", preweight)
   preweight = float(preweight)
   assert editedWeight == preweight
   danpheEMR.find_element(By.XPATH, "//button[@class = 'btn btn-danger']").click()


def wait_for_window(danpheEMR, timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars("window_handles")
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

