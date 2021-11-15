from selenium import webdriver
import time
import random
import AutomationTest.Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)
AppName = AC.appName

#Module:Patient_Registration -----------------
   def patientRegistration(self):
      global contactno
      global HospitalNo
      global FullName
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("Patient").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("Register Patient").click()
      time.sleep(2)

      #fname = "auto "
      #z = "preg"
      #sname1 = z+sname
      #print("Sir name", sname1)
      #FullName = fname + sname1
      #print("Full name of patient:", FullName)

      age = random.randint(1, 99)
      self.danpheEMR.find_element_by_xpath("//input[@type='number']").send_keys(age)
      contactno = random.randint(9811111111, 9899999999)
      self.danpheEMR.find_element_by_xpath("//input[@type='tel']").send_keys(contactno)
      print(contactno)

      # if appPort == "81":
      #    self.danpheEMR.find_element_by_id("regPatFirstName").send_keys("auto")
      #    sname = str(random.randint(1111, 9999))
      #    self.danpheEMR.find_element_by_xpath("(//input[@value=''])[3]").send_keys("preg", sname)
      #    self.danpheEMR.find_element_by_css_selector(".col-md-6:nth-child(2) > .form-group:nth-child(1) .mt-checkbox:nth-child(1) > span").click()
      if appPort == "82":
         self.danpheEMR.find_element_by_link_text("Register Patient").click()
         self.danpheEMR.find_element_by_id("regPatFirstName").send_keys("auto")
         sname = str(random.randint(1111, 9999))
         self.danpheEMR.find_element_by_xpath("(//input[@value=''])[3]").send_keys("preg", sname)
         gender = Select(self.danpheEMR.find_element_by_xpath("//select[@formcontrolname='Gender']"))
         gender.select_by_visible_text("Female")

      self.danpheEMR.find_element_by_xpath("//input[@value='Register Patient']").click()
      time.sleep(7)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(contactno)
      time.sleep(5)
      assert str(contactno) == self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']"
                                                                    "/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
      global HospitalNo
      HospitalNo = self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']"
                                                        "/div/div/div/div[3]/div[2]/div/div/div/div").text
      print(HospitalNo)
   def getRandomPatient(self):
      self.danpheEMR.find_element_by_link_text("Patient").click()
      time.sleep(5)
      global HospitalNo
      HospitalNo = self.danpheEMR.find_element_by_xpath("(//div[@col-id='PatientCode'])[2]").text


def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

