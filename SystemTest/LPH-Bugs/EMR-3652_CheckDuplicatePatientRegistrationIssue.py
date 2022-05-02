''''
Scripted by: Hari P. Bhatta
The objective of this test case is to test below issue:
Headline:
Registration | Duplicate patient created & multiple button click issue.
Description:
Multiple/ duplicate patients created due to multiple button click issues.
Navigation:
Patient > Register Patient

'''
########
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleSettings as LS
import Library.LibModulePatientPortal as LP
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
# 1. Do New Patient Registration
contactNo = LP.patientRegistrationMultipleClick(EMR)
LP.verifyMultipleRegistration(EMR, ContactNo=contactNo)
AC.logout()
AC.closeBrowser()