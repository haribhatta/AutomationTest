import time
import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import Library.LibModuleAppointment as LA
import random
########
AppName = GSV.appName
########
#Module:Incentive ******************

def VaccinationPatientRegistration(danpheEMR):
    global HospitalNo
    print("Start >> VaccinationPatientRegistration")
    time.sleep(7)
    danpheEMR.find_element_by_link_text("Vaccination").click()
    time.sleep(7)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),' New Vaccination Patient')]").click()
    time.sleep(4)
    sname = str(random.randint(1111, 9999))
    fname = "vaccine "
    mname = "mother "
    fullName = fname + mname + sname
    print("Full name of patient:", fullName)
    danpheEMR.find_element(By.ID, "regPatMotherName").send_keys(fullName)
    age = str(random.randint(1, 9))
    danpheEMR.find_element(By.ID, "babyAge").send_keys(age)
    time.sleep(4)
    '''    
    danpheEMR.find_element(By.CSS_SELECTOR, "#gender > option:nth-child(2)").click()
    dropdown = danpheEMR.find_element(By.ID, "gender")
    dropdown.find_element(By.XPATH, "//option[. = 'Female']").click()
    '''
    danpheEMR.find_element(By.CSS_SELECTOR, "#gender > option:nth-child(2)").click()
    #danpheEMR.find_element(By.ID, "address").click()
    #danpheEMR.find_element(By.ID, "address").send_keys("rupandehi")
    #danpheEMR.find_element(By.ID, "address").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "register").click()
    time.sleep(6)
    HospitalNo = danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Hospital No. :')]").text
    print("HospitalNo:", HospitalNo)
    HospitalNo = HospitalNo.partition("Hospital No. : ")[2]
    vaccineRegNo = danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Vacc. Reg. No :')]").text
    print("vaccineRegNo:", vaccineRegNo)
    danpheEMR.find_element(By.ID, "btnPrintSticker").send_keys(Keys.ESCAPE)
    time.sleep(3)
    print("End >> VaccinationPatientRegistration")
def verifyVaccinationPatientRegistration(danpheEMR):
    global HospitalNo
    print("Start >> verifyVaccinationPatientRegistration")
    danpheEMR.find_element_by_link_text("Vaccination").click()
    time.sleep(5)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    searchResult = danpheEMR.find_element(By.XPATH, "(//div[@col-id='PatientCode'])[2]").text
    print("searchResult:", searchResult)
    assert searchResult == HospitalNo
    print("End >> verifyVaccinationPatientRegistration")

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

