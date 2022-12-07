''''
The objective of this test case is to test below scenarios:
1. Create an appointment for new patient with Price Category 'SSF' and verify tender amount.
'''
########
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
from datetime import datetime
# from colorama import Fore, Back, Style

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
priceCategoryType = "SSF"
discountValue = GSV.discountSchemeName


EMR = AC.openBrowser()
AC.login(admUserId, admUserPwd)
LB.counteractivation(EMR)
    # 1. Create an appointment for new patient with Price Category 'SSF'.

HospitalNo2, InvoiceNo2, discountPercentage2 = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
print("Status:Passed || TestAction:NewAppointment|| SSF Patient")
AC.logout()
AC.closeBrowser()




