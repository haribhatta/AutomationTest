''''
Scripted by: Hari P. Bhatta
The objective of this test case is to test below issue:
Headline: Registration>NewVisit: Double click issue on new patient visit creation.
Issue: There is double click issue while creating new visit for new patient.
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
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='-ve')
LB.verifyDuplicateBill(EMR, HospitalNo)
#AC.logout()
#AC.closeBrowser()