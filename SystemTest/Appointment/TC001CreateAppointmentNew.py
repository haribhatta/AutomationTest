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
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeChildUN
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
#Scenario: Cash Payment
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("Status:Passed || TestAction:NewAppointment||Cash||NoDiscount")
#Scenario: Cash Payment with discount
HospitalNo1 = LA.patientquickentry(EMR, discountScheme=discountScheme, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("Status:Passed || TestAction:NewAppointment||Cash||Discount")
#Scenario: Credit Payment
HospitalNo2 = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Credit', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("Status:Passed || TestAction:NewAppointment||Credit||NoDiscount")
#Scenario: Credit Payment with discount
HospitalNo3 = LA.patientquickentry(EMR, discountScheme=discountScheme, paymentmode='Credit', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("Status:Passed || TestAction:NewAppointment||Credit||Discount")
# 2. Create an appointment for old patient.
LA.oldPatientRegistration(EMR, HospitalNo, doctorGynae, departmentGynae)
AC.logout()
AC.closeBrowser()
print("Status:Passed - > TC001 oldPatientAppointment")


