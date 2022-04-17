''''
The objective of this test case is to test below scenarios:
1. Create an appointment for old patient.
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
# 2. Create an appointment for old patient.
LA.oldPatientRegistration(EMR, HospitalNo, doctorGynae, departmentGynae)
AC.logout()
AC.closeBrowser()
print("Status:Passed - > TC001 oldPatientAppointment")

#in discountScheme : need to send below data: may be in form of Array?
#1. showCommunityFlag



