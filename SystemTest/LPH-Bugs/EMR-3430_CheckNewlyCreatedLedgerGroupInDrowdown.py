''''
Scripted by: Hari P. Bhatta
The objective of this test case is to test below issue:
Headline:
Account> Transaction> Voucher Entry> Ledger group is not showing up in the dropdown once it is created from the (?) button.

Description:
While creating ledger group from transaction page. It is not showing up in the dropdown once it is created. It is due to the issue shown in the attachments down below.

'''
########
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleSettings as LS
import Library.LibModuleAccounting as LAc

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
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
#Scenario: Cash Payment
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LAc.createLedgerGroup(EMR)
AC.logout()
AC.closeBrowser()