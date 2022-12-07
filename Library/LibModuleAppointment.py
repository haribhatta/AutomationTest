from selenium import webdriver
import time
import random
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

AppName = GSV.appName


# HospitalNo = None
# Module:Appointment --------------------
def patientquickentry(danpheEMR, discountScheme, paymentmode, department, doctor, priceCategoryType, case):
    print("START>>patientquickentry")
    global InvoiceNo
    global contactno
    global HospitalNo
    global FullName
    global discountPercentage
    global TenderAmt
    global selected_option
    print("AppName", AppName)
    time.sleep(5)
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Registration").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Appointment").click()
    time.sleep(7)
    danpheEMR.find_element(By.ID, "btnNewPatient").click()
    time.sleep(4)
    if AppName == "LPH" and priceCategoryType == "EHS":
        danpheEMR.find_element(By.CSS_SELECTOR, "div > .ng-untouched:nth-child(2)").click()
        # dropdown = danpheEMR.find_element(By.CSS_SELECTOR, ".ng-dirty")
        dropdown = danpheEMR.find_element(By.XPATH, "//price-category-select/div/select")
        dropdown.find_element(By.XPATH, "//option[. = 'EHS (PayClinic)']").click()
        time.sleep(3)

    elif (AppName != "LPH" or AppName != "APF") and priceCategoryType == "SSF":
        danpheEMR.find_element(By.XPATH, "//select[@class='ng-untouched ng-pristine ng-valid']").click()
        dropdown = danpheEMR.find_element(By.XPATH, "//price-category-select/div/select")
        dropdown.find_element(By.XPATH, "//option[. = 'SSF']").click()
        time.sleep(3)
        CreditOrganization = Select(
            danpheEMR.find_element(By.XPATH, "//select[@class='form-control mb-8 ng-untouched ng-pristine ng-valid']"))
        selected_option = CreditOrganization.first_selected_option
        print(selected_option.text)
        selected_option = str(selected_option.text)
        print(selected_option)
        danpheEMR.find_element(By.XPATH, "//input[@placeholder='Remarks']").send_keys("This is remark")
    danpheEMR.find_element(By.ID, "txtDepartment").send_keys(department)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "txtDepartment").send_keys(Keys.TAB)
    time.sleep(5)
    danpheEMR.find_element(By.ID, "doctorName").send_keys(doctor)
    time.sleep(5)
    danpheEMR.find_element(By.ID, "doctorName").send_keys(Keys.ENTER)
    time.sleep(5)
    danpheEMR.find_element(By.ID, "aptPatFirstName").send_keys("auto")
    danpheEMR.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("test")
    sname = str(random.randint(1111, 9999))
    danpheEMR.find_element(By.CSS_SELECTOR, ".col-md-3:nth-child(4) > .form-control").send_keys("pqe", sname)
    fname = "auto "
    mname = "test "
    z = "pqe"
    sname1 = z + sname
    print("Sir name", sname1)
    FullName = fname + mname + sname1
    print("Full name of patient:", FullName)
    age = random.randint(15, 47)
    danpheEMR.find_element(By.CSS_SELECTOR, ".row > .form-control").send_keys(age)
    danpheEMR.find_element(By.CSS_SELECTOR, ".input-group > .ng-valid").click()  #
    dropdown = danpheEMR.find_element(By.CSS_SELECTOR, ".ng-dirty")  #
    dropdown.find_element(By.XPATH, "//option[. = 'Years']").click()  #
    danpheEMR.find_element(By.CSS_SELECTOR, ".ng-dirty").click()  #
    gender = Select(danpheEMR.find_element(By.XPATH, "//select[@formcontrolname='Gender']"))
    gender.select_by_visible_text("Female")
    phoneNo = random.randint(9111111111, 9999999999)
    danpheEMR.find_element(By.ID, "txtPhone").send_keys(phoneNo)
    time.sleep(3)
    TenderAmt = danpheEMR.find_element(By.ID, "tender").get_attribute("value")
    TenderAmt = float(TenderAmt)
    print("Tender Amount", TenderAmt)
    time.sleep(3)
    # Community =danpheEMR.find_element(By.XPATH, "//select[@id='Membership']").click()
    # Community.select_by_visible_text("Social Service Unit")
    if discountScheme == 0:
        discountPercentage = 0
    if discountScheme != 0:
        print("discountScheme:", discountScheme)
        dropdown1 = Select(danpheEMR.find_element(By.ID, "Scheme"))
        time.sleep(5)
        print("dropdown1:", dropdown1)
        dropdown1.select_by_visible_text(discountScheme)
        time.sleep(3)
        discountPercentage = danpheEMR.find_element(By.XPATH, "//input[@placeholder='Discount %']").get_attribute(
            "value")
        print("discountPercentage:", discountPercentage)
        discountPercentage = int(discountPercentage)
        print("discountPercentage:", discountPercentage)
        assert discountPercentage == GSV.DiscountPercent
    if paymentmode == 'Credit':
        paymentoptions = Select(danpheEMR.find_element(By.XPATH, "//select[@id='pay_mode']"))
        paymentoptions.select_by_visible_text("Credit")
        creditorg = Select(danpheEMR.find_element(By.XPATH, "//tr[2]/td[2]/select"))
        time.sleep(2)
        creditorg.select_by_visible_text(GSV.creditOrganization)
        danpheEMR.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("Credit in request of chairman")
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//input[@placeholder='Remarks']").send_keys("This is remark")
    time.sleep(9)
    # danpheEMR.find_element(By.CSS_SELECTOR, ".btn-success").click()
    if case == '-ve':
        danpheEMR.find_element(By.ID, "btnPrintInvoice").click()
        print("first click for duplicate check")
        danpheEMR.find_element(By.ID, "btnPrintInvoice").click()
        print("second click for duplicate check")
        danpheEMR.find_element(By.ID, "btnPrintInvoice").click()
        print("third click for duplicate check")
    else:
        danpheEMR.find_element(By.ID, "btnPrintInvoice").click()
    time.sleep(9)
    if priceCategoryType == "SSF":
        InvoiceTenderAmt = danpheEMR.find_element(By.XPATH,
                                                  "//*[@id='divBilInvoicePrintPage']/div/div[3]/span").text
        print(InvoiceTenderAmt)
        InvoiceTenderAmt = InvoiceTenderAmt.partition(": ")[2]
        InvoiceTenderAmt = InvoiceTenderAmt.partition(".")[0]
        InvoiceTenderAmt = InvoiceTenderAmt.replace(',', '')
        InvoiceTenderAmt = float(InvoiceTenderAmt)
        print("Invoice Tender Amt", InvoiceTenderAmt)
        InvoiceCreditOrganization = danpheEMR.find_element(By.XPATH,
                                                           "//*[@id='divBilInvoicePrintPage']/div/div[8]/div").text
        InvoiceCreditOrganization = InvoiceCreditOrganization.partition(": ")[2]
        InvoiceCreditOrganization = InvoiceCreditOrganization.partition(".")[0]
        InvoiceCreditOrganization = InvoiceCreditOrganization.replace(',', '')
        print("InvoiceCreditOrganization", InvoiceCreditOrganization)
        assert TenderAmt == InvoiceTenderAmt
        assert selected_option == str(InvoiceCreditOrganization)
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    print("InvoiceNoTemp", InvoiceNo)
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("InvoiceNo", InvoiceNo)
    time.sleep(3)
    HospitalNo = danpheEMR.find_element(By.XPATH,
                                        "//strong[contains(text(), 'Hospital No:')]/parent::p/child::span/child::strong").text
    print("HospitalNo:", HospitalNo)
    danpheEMR.find_element(By.ID, "btnPrintOpdSticker").send_keys(Keys.ESCAPE)
    time.sleep(10)
    print("END>>patientquickentry")
    return HospitalNo, InvoiceNo, discountPercentage
    # return type('', (object,), {"InvoiceNo": InvoiceNo, "HospitalNo": HospitalNo})()


def followUpAppointment(danpheEMR):
    print("START>>followUpAppointment")
    time.sleep(5)
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Registration").click()
        time.sleep(5)
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Appointment").click()
        time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "List Visits").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
    time.sleep(7)
    danpheEMR.find_element(By.XPATH, "(//a[@danphe-grid-action='followup' and contains(text(),'followup')])[5]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),' Add Followup Visit ')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btnPrintOpdSticker").send_keys(Keys.ESCAPE)  # LPH-932
    print("END>>followUpAppointment")


def oldPatientRegistration(danpheEMR, HospitalNo, DoctorName, Department):
    print("START>>oldPatientRegistration")
    time.sleep(2)
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Registration").click()
        time.sleep(2)
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Appointment").click()
        time.sleep(2)
    x = int(HospitalNo) - 36
    print("old patient:", x)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(x)
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Check In").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "txtDepartment").send_keys(Department)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "txtDepartment").send_keys(Keys.TAB)
    if AppName != "LPH":
        danpheEMR.find_element(By.ID, "doctorName").send_keys(DoctorName)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btnPrintInvoice").click()
    time.sleep(5)
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    # verify = popup.danpheEMR.find_element(By.XPATH, "//b[contains(text(),' Please bring this invoice on your next visit. ')]").text
    print("InvoiceNo", InvoiceNo)
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    time.sleep(3)
    print("END>>oldPatientRegistration")


def VerifySSFpatient(danpheEMR):
    global TenderAmt
    global CreditOrganization
    print("START>>> Verify SSF patient")
    InvoiceTenderAmt = danpheEMR.find_element(By.XPATH,"//*[@id='divBilInvoicePrintPage']/div/div[3]/span").get_attribute(
        "value")
    InvoiceTenderAmt = float(InvoiceTenderAmt)
    print("InvoiceTenderAmt", InvoiceTenderAmt)
    InvoiceCreditOrganization = danpheEMR.find_element(By.XPATH,
                                                       "/html/body/my-app/div/div/div[3]/div[2]/div/div/my-app/visit-main/div/div/div[2]/div/div[1]/div[3]/visit-billing-info/div/div/div/div/div/div[5]/payment-mode-info/table/tbody/tr[2]").text
    print("InvoiceCreditOrganization", InvoiceCreditOrganization)

    assert TenderAmt == InvoiceTenderAmt
    assert CreditOrganization == InvoiceCreditOrganization


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
