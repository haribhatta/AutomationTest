from selenium import webdriver
import time
import random
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

#danpheEMR = AC.danpheEMR
#print("DanpheEMR", danpheEMR)
AppName = GSV.appName
#HospitalNo = None
# Module:Appointment --------------------
def patientquickentry(danpheEMR, discountpc, paymentmode, department, doctor):
   global InvoiceNo
   global contactno
   global HospitalNo
   global FullName
   print("AppName", AppName)
   print(">>Create New Appointment: START")
   if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
      time.sleep(2)
      if AppName == "LPH":
         danpheEMR.find_element_by_link_text("Registration").click()
      else:
         danpheEMR.find_element_by_link_text("Appointment").click()
      time.sleep(4)
      danpheEMR.find_element_by_id("btnNewPatient").click()
      time.sleep(4)
      if AppName == "LPH":
         danpheEMR.find_element_by_id("txtDepartment").send_keys(department)
         time.sleep(2)
         danpheEMR.find_element_by_id("txtDepartment").send_keys(Keys.TAB)
         time.sleep(3)
      else:
         danpheEMR.find_element_by_id("txtDepartment").send_keys(department)
         time.sleep(3)
         danpheEMR.find_element_by_id("txtDepartment").send_keys(Keys.TAB)
         time.sleep(3)
         danpheEMR.find_element_by_id("doctorName").send_keys(doctor)
         time.sleep(3)
      danpheEMR.find_element_by_id("aptPatFirstName").send_keys("auto")
      danpheEMR.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
      sname = str(random.randint(1111, 9999))
      danpheEMR.find_element_by_css_selector(".col-md-3:nth-child(4) > .form-control").send_keys("pqe", sname)
      fname = "auto "
      mname = "test "
      z = "pqe"
      sname1 = z + sname
      print("Sir name", sname1)
      FullName = fname + mname + sname1
      print("Full name of patient:", FullName)
      age = random.randint(5, 99)
      danpheEMR.find_element_by_css_selector(".row > .form-control").send_keys(age)
      danpheEMR.find_element_by_css_selector(".input-group > .ng-valid").click()  #
      dropdown = danpheEMR.find_element_by_css_selector(".ng-dirty")  #
      dropdown.find_element_by_xpath("//option[. = 'Years']").click()  #
      danpheEMR.find_element_by_css_selector(".ng-dirty").click()  #
      gender = Select(danpheEMR.find_element_by_xpath("//select[@formcontrolname='Gender']"))
      gender.select_by_visible_text("Male")
      phoneNo = random.randint(9111111111, 9999999999)
      danpheEMR.find_element_by_id("txtPhone").send_keys(phoneNo)
      if discountpc > 0:
         danpheEMR.find_element_by_css_selector(".comm-list").click()
         dropdown = danpheEMR.find_element_by_css_selector(".comm-list")
         time.sleep(3)
         dropdown.find_element_by_xpath("//option[. = 'SOCIAL SERVICE UNIT']").click()
         time.sleep(7)
         danpheEMR.find_element_by_css_selector(".comm-list").click()
         time.sleep(5)
         danpheEMR.find_element_by_css_selector(".membership-list").click()
         time.sleep(4)
         dropdown = danpheEMR.find_element_by_css_selector(".membership-list")
         time.sleep(5)
         dropdown.find_element_by_xpath("//option[. = ' Child Under Nutrition (50%)']").click()
         time.sleep(3)
         danpheEMR.find_element_by_css_selector(".membership-list").click()
      if paymentmode == 'CREDIT':
         paymentoptions = Select(danpheEMR.find_element_by_xpath("//select[@id='pay_mode']"))
         paymentoptions.select_by_visible_text(paymentmode)
         danpheEMR.find_element_by_xpath("//div[2]/div[2]/input").send_keys("Credit in request of chairman")
      danpheEMR.find_element_by_css_selector(".btn-success").click()
      time.sleep(9)
      InvoiceNo = danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]").text
      print("InvoiceNoTemp", InvoiceNo)
      InvoiceNo = InvoiceNo.partition("BL")[2]
      print("InvoiceNo", InvoiceNo)
      HospitalNo = danpheEMR.find_element_by_xpath(
         "//strong[contains(text(), 'Hospital No:')]/parent::p/child::span/child::strong").text
      print("HospitalNo:", HospitalNo)
      print(" Verify OPD Invoice Details: END<<", "HospitalNo", HospitalNo, "InvoiceNo", InvoiceNo)
      time.sleep(2)
      danpheEMR.find_element_by_id("btnPrintOpdSticker").send_keys(Keys.ESCAPE)
      time.sleep(3)
      return type('', (object,), {"InvoiceNo": InvoiceNo,"HospitalNo": HospitalNo})()
      # return [InvoiceNo, HospitalNo]
   print(" Verify OPD Invoice Details: END<<", "HospitalNo", HospitalNo, "InvoiceNo", InvoiceNo)
   print("Create New Appointment: END<<")
def followUpAppointment(danpheEMR):
      print("lets create appointment followup")
      if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
         time.sleep(5)
         if AppName == "LPH":
            danpheEMR.find_element_by_link_text("Registration").click()
            time.sleep(5)
         else:
            danpheEMR.find_element_by_link_text("Appointment").click()
            time.sleep(5)
         danpheEMR.find_element_by_link_text("List Visits").click()
         time.sleep(5)
         x = range(1, 3, 1)
         for n in x:
             try:
                print(n)
                danpheEMR.find_element_by_xpath("(//a[contains(text(),'followup')])[1]").click()
                print("test1")
                time.sleep(3)
             except:
                #danpheEMR.find_element_by_xpath("//button[contains(text(),'Next')]").click()
                print("test2")
                pass
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//button[contains(text(),' Add Followup Visit ')]").click()
         time.sleep(5)
         danpheEMR.find_element_by_id("btnPrintOpdSticker").send_keys(Keys.ESCAPE)  # LPH-932
         #danpheEMR.find_element_by_xpath("//i[@class='btn btn-danger']").click()
def oldPatientRegistration(danpheEMR, HospitalNo,DoctorName,Department):
   print(">>Create Old Appointment: START")
   if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
      time.sleep(2)
      if AppName == "LPH":
         danpheEMR.find_element_by_link_text("Registration").click()
         time.sleep(2)
      else:
         danpheEMR.find_element_by_link_text("Appointment").click()
         time.sleep(2)
      x = int(HospitalNo)-35
      print("old patient:", x)
      time.sleep(2)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(x)
      time.sleep(2)
      danpheEMR.find_element_by_link_text("Check In").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("txtDepartment").send_keys(Department)
      time.sleep(3)
      danpheEMR.find_element_by_id("txtDepartment").send_keys(Keys.TAB)
      time.sleep(3)
      danpheEMR.find_element_by_id("doctorName").send_keys(DoctorName)
      danpheEMR.find_element_by_id("btnPrintInvoice").click()
      time.sleep(5)
      InvoiceNo = danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]").text
      #verify = popup.danpheEMR.find_element_by_xpath("//b[contains(text(),' Please bring this invoice on your next visit. ')]").text
      print("InvoiceNo", InvoiceNo)
      danpheEMR.find_element_by_id("btnPrintRecipt").send_keys(Keys.ESCAPE)
      time.sleep(3)
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

