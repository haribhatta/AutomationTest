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
import Library.LibModuleSettings as LS
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
#discountScheme = GSV.discountSchemeName
#############
EMR = AC.openBrowser()
AC.login(admUserId, admUserPwd)
a, b = LS.checkCoreCFGdiscountMembership(EMR)
discountValue = a + b

AC.logout()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
#Scenario: Cash Payment
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("Status:Passed || TestAction:NewAppointment||Cash||NoDiscount")
#Scenario: Cash Payment with discount
HospitalNo1 = LA.patientquickentry(EMR, discountScheme=discountValue, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("Status:Passed || TestAction:NewAppointment||Cash||Discount")
#Scenario: Credit Payment
HospitalNo2 = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Credit', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("Status:Passed || TestAction:NewAppointment||Credit||NoDiscount")
#Scenario: Credit Payment with discount
HospitalNo3 = LA.patientquickentry(EMR, discountScheme=discountValue, paymentmode='Credit', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("Status:Passed || TestAction:NewAppointment||Credit||Discount")
# 2. Create an appointment for old patient.
LA.oldPatientRegistration(EMR, HospitalNo, doctorGynae, departmentGynae)
AC.logout()
AC.closeBrowser()
print("Status:Passed - > TC001 oldPatientAppointment")

#in discountScheme : need to send below data: may be in form of Array?
#1. showCommunityFlag



