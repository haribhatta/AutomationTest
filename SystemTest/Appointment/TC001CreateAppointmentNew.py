''''
The objective of this test case is to test below scenarios:
1. Create an appointment for new patient.
2. Create an appointment for old patient.
'''
########
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
from datetime import datetime
from colorama import Fore, Back, Style

#############
# admin user login
admUserId = GSV.adminUserID
admUserPwd = GSV.adminUserPwD
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
########
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
discountValue = GSV.discountSchemeName

#############
try:

    EMR = AC.openBrowser()
    AC.login(admUserId, admUserPwd)
    LB.counteractivation(EMR)
    # 1. Create an appointment for new patient.
    #Scenario: Cash Payment
    HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
    print("Status:Passed || TestAction:NewAppointment||Cash||NoDiscount")
    #Scenario: Cash Payment with discount
    HospitalNo1, InvoiceNo1, discountPercentage1 = LA.patientquickentry(EMR, discountScheme=discountValue, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
    print("Status:Passed || TestAction:NewAppointment||Cash||Discount")
    #Scenario: Credit Payment
    HospitalNo2, InvoiceNo2, discountPercentage2 = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Credit', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
    print("Status:Passed || TestAction:NewAppointment||Credit||NoDiscount")
    #Scenario: Credit Payment with discount
    HospitalNo3, InvoiceNo3, discountPercentage3 = LA.patientquickentry(EMR, discountScheme=discountValue, paymentmode='Credit', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
    print("Status:Passed || TestAction:NewAppointment||Credit||Discount")
    AC.logout()
    AC.closeBrowser()
    print("Status:Passed - > TC001 oldPatientAppointment")
except:
    now = datetime.now()
    print("now:", now)
    today = now.strftime("%m%d%y%H%M%S")
    print("today:", today)
    fileName = today + "image.png"
    print("fileName:", fileName)
    EMR.save_screenshot(fileName)
    print(Fore.RED + "Test Case Execution Status: Failed, Please check screenshot.")

#in discountScheme : need to send below data: may be in form of Array?
#1. showCommunityFlag



