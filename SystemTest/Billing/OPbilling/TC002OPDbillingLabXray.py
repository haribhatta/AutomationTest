'''
Objective: Happy Path of OPD billing.
The AIM of this test script is to verify below scenarios:
1. Create an OPD invoice of - lab item and xray item.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
#from datetime import datetime
#from colorama import Fore, Back, Style

#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
#############
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)

# 1. Create an appointment for new patient.
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType="Normal", case='+ve')
#can.verifyopdinvoice(deposit=0, billamt=500)
print("Status:Passed - > TC001 CreateAppointmentNew")
#oblx.verifyopdinvoice(deposit=0, billamt=500)
LB.createlabxrayinvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=GSV.TFT, imagingtest=GSV.USG)
#oblx.verifylabxrayinvoice()
AC.logout()
AC.closeBrowser()
print("Status:Passed -> TC002OPDbillingLabXray.py")
# except:
#     now = datetime.now()
#     print("now:", now)
#     today = now.strftime("%m%d%y%H%M%S")
#     print("today:", today)
#     fileName = today + "image.png"
#     print("fileName:", fileName)
#     EMR.save_screenshot(fileName)
#     print(Fore.RED + "Test Case Execution Status: Failed, Please check screenshot.")


