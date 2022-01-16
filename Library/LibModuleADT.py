from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys

#danpheEMR = AC.danpheEMR
#print("DanpheEMR", danpheEMR)
AppName = GSV.appName

#Module:ADT -----------------------------
def admitDisTrans(danpheEMR, admit, discharge, trasfer,HospitalNo, deposit, doctor, department):
      if admit == 1:
         if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
            time.sleep(3)
            danpheEMR.find_element_by_link_text("ADT").click()
            time.sleep(3)
            danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
            time.sleep(3)
            danpheEMR.find_element_by_link_text("Admit").click()
            time.sleep(3)
            danpheEMR.find_element_by_id("admissionCase").click()
            dropdown = danpheEMR.find_element_by_id("admissionCase")
            dropdown.find_element_by_xpath("//option[. = 'General']").click()
            danpheEMR.find_element_by_id("admissionCase").click()
            danpheEMR.find_element_by_id("RequestingDeptId").send_keys(department)
            danpheEMR.find_element_by_id("RequestingDeptId").send_keys(Keys.ENTER)
            danpheEMR.find_element_by_id("RequestingDeptId").click()
            time.sleep(3)
            if AppName == "SNCH" or AppName == "MPH":
                danpheEMR.find_element_by_id("AdmittingDoctorId").send_keys(GSV.doctorGyno)
                danpheEMR.find_element_by_id("AdmittingDoctorId").send_keys(Keys.ENTER)
                time.sleep(3)
            wardID = Select(danpheEMR.find_element_by_id("WardId"))
            time.sleep(3)
            wardID.select_by_visible_text(GSV.generalWard)
            time.sleep(3)
            danpheEMR.find_element_by_id("BedFeatureId").click()
            time.sleep(3)
            danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ENTER)
            time.sleep(1)
            danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.DOWN)
            danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ENTER)
            danpheEMR.find_element_by_id("BedFeatureId").click()
            time.sleep(2)
            danpheEMR.find_element_by_id("BedId").click()
            time.sleep(0.5)
            danpheEMR.find_element_by_id("BedId").send_keys(Keys.ENTER)
            danpheEMR.find_element_by_id("BedId").send_keys(Keys.DOWN)
            time.sleep(2)
            danpheEMR.find_element_by_id("BedId").send_keys(Keys.ENTER)
            danpheEMR.find_element_by_id("BedId").click()
            time.sleep(2)
            danpheEMR.find_element_by_id("SaveAdmission").click()
            time.sleep(2)
            if AppName == "LPH":
                #danpheEMR.find_element_by_id("btnAdtSticker").click()
                time.sleep(4)
                danpheEMR.find_element_by_xpath("//button[@class='btn btn-danger']").click()
                #danpheEMR.find_element_by_id("btnPrintRecipt").send_key(Keys.ESCAPE)
            else:
                danpheEMR.find_element_by_id("btnAdtSticker").click()
                #danpheEMR.find_element_by_id("btnAdtSticker").send_keys(Keys.ESCAPE)
            print("Patient successfully admitted.")
            time.sleep(2)
      elif discharge == 1:
         time.sleep(5)
         danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("IPBilling").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(5)
         danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
         danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//pat-ip-bill-summary/div/div[2]/div/div/div/div/a").click()
         # danpheEMR.find_element_by_id("btnPrintDischargeInvoice")
         # danpheEMR.find_element_by_id("btnPrintDischargeInvoice").send_keys(Keys.ESCAPE)

      elif trasfer == 1:
         danpheEMR.find_element_by_link_text("ADT").click()
         time.sleep(3)
         danpheEMR.find_element_by_link_text("Admitted Patients").click()
         time.sleep(3)
         danpheEMR.find_element_by_link_text("Transfer").click()
         time.sleep(2)
         danpheEMR.find_element_by_id("DepartmentName").click()
         danpheEMR.find_element_by_id("DepartmentName").send_keys(department)
         danpheEMR.find_element_by_id("DepartmentName").send_keys(Keys.TAB)
         # danpheEMR.find_element_by_id("SecondaryDoctorName").send_keys()

         Ward = Select(danpheEMR.find_element_by_id('WardId'))
         Ward.select_by_visible_text('ICU')
         # # select by value and index
         # select.select_by_value('1')
         time.sleep(2)
         danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ENTER)
         danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ARROW_DOWN)
         danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ENTER)


         # Bedfeature = Select(danpheEMR.find_element_by_id("BedFeatureId"))
         # Bedfeature.select_by_visible_text("BED CHARGE ICU")
         danpheEMR.find_element_by_id("BedId").click()
         danpheEMR.find_element_by_id("BedId").send_keys(Keys.ARROW_DOWN)
         danpheEMR.find_element_by_id("BedId").send_keys(Keys.ENTER)
         # danpheEMR.find_element_by_xpath("//select").send_keys(Keys.RETURN)
         # danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         # danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         # danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         # danpheEMR.find_element_by_xpath("//select").send_keys(Keys.RETURN)
         # danpheEMR.find_element_by_xpath("//tr[5]/td[2]/select").send_keys(Keys.RETURN)
         # danpheEMR.find_element_by_xpath("//tr[5]/td[2]/select").send_keys(Keys.ARROW_DOWN)
         # danpheEMR.find_element_by_xpath("//tr[5]/td[2]/select").send_keys(Keys.RETURN)
         # danpheEMR.find_element_by_xpath("//tr[7]/td[2]/select").send_keys(Keys.RETURN)
         # danpheEMR.find_element_by_xpath("//tr[7]/td[2]/select").send_keys(Keys.ARROW_DOWN)
         # danpheEMR.find_element_by_xpath("//tr[7]/td[2]/select").send_keys(Keys.RETURN)
         danpheEMR.find_element_by_id("Remarks").send_keys("Transfer to ICU ward")
         danpheEMR.find_element_by_xpath("//input[@name='name']").click()
def cancelDischarge(danpheEMR, HospitalNo):
      # To cancel discharge user need to return discharge invoice
      print("Start: cancel discharge")
      danpheEMR.find_element_by_link_text("ADT").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Discharged Patients").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Cancel Discharge')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("DischargeCancelNote").send_keys("Cancel Discharge")
      time.sleep(2)
      danpheEMR.find_element_by_id("Approve").click()
      time.sleep(5)
      print("End: cancel discharge")
def dischargeRandomPatient(danpheEMR):
      time.sleep(2)
      if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
         danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("IPBilling").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(9)
         danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
         time.sleep(3)
         danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
         time.sleep(3)
         #danpheEMR.find_element_by_id("btnPrintDischargeInvoice").send_keys(Keys.ESCAPE)
         danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']").click()
         time.sleep(14)
      time.sleep(5)
def checkAutoAddItems(danpheEMR):
      danpheEMR.find_element_by_link_text("Settings").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//a[contains(text(),' ADT ')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Manage Auto Add Billing Items").click()
      time.sleep(2)
      #danpheEMR.find_element_by_xpath("//h4[text()='Auto Add Bill Item: ']").click()
      autoaddbillitemvalue = danpheEMR.find_element_by_xpath("//b[contains(.,'  False')]").text
      autoaddBeditemvalue = danpheEMR.find_element_by_xpath("//b[contains(.,'  True')]").text
      print("autoaddbillitemvalue", autoaddbillitemvalue)
      print("autoaddBeditemvalue", autoaddBeditemvalue)
      #assert autoaddbillitemvalue == "autoaddbillitemvalue   False"      rework needed
      #assert autoaddBeditemvalue == "autoaddBeditemvalue   True"        rework needed
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

