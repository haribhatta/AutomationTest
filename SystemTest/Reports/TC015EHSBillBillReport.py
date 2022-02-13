import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC

import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
# front desk user login
itUserId = GSV.itUserID
itUserPwd = GSV.itUserPwD
user = GSV.foUserID
departmentGynae = GSV.departmentGyno
doctorGynaeEHS = GSV.doctorGynoEHS
opdRate = GSV.opdRate
###
priceCategoryType = "EHS"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(itUserId, itUserPwd)
LB.counteractivation(EMR)
time.sleep(2)
LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynaeEHS, priceCategoryType=priceCategoryType) # fulfilling pre-condition
#Scenario-A1: EHS Cash billing
LBR.getEHSBillReport(EMR)
LBR.preEHSBillReport()
InvoiceNo1 = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynaeEHS, priceCategoryType=priceCategoryType).InvoiceNo
print("InvoiceNo1", InvoiceNo1)
LBR.getEHSBillReport(EMR)
LBR.verifyEHSBillReport()
#Scenario-A2: EHS Return Cash billing
LBR.preEHSBillReport()
LB.returnBillingInvoice(EMR, InvoiceNo1, returnmsg="This is Return Invoice",)
LBR.getEHSBillReport(EMR)
LBR.verifyEHSBillReport()
#Scenario-A3: EHS Credit billing
LBR.getEHSBillReport(EMR)
LBR.preEHSBillReport()
InvoiceNo2 = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Credit', department=departmentGynae, doctor=doctorGynaeEHS, priceCategoryType=priceCategoryType).InvoiceNo
print("InvoiceNo2", InvoiceNo2)
LBR.getEHSBillReport(EMR)
LBR.verifyEHSBillReport()
#Scenario-A4: EHS Return Credit billing
LBR.preEHSBillReport()
LB.returnBillingInvoice(EMR, InvoiceNo2, returnmsg="This is Return Invoice",)
LBR.getEHSBillReport(EMR)
LBR.verifyEHSBillReport()
######## Repeat above 1-4 scenarios with Discount
#Scenario-B1: EHS Discount Cash billing
LBR.getEHSBillReport(EMR)
LBR.preEHSBillReport()
InvoiceNo3 = LA.patientquickentry(EMR, discountScheme=discountScheme, paymentmode='Cash', department=departmentGynae, doctor=doctorGynaeEHS, priceCategoryType=priceCategoryType).InvoiceNo
print("InvoiceNo3", InvoiceNo3)
LBR.getEHSBillReport(EMR)
LBR.verifyEHSBillReport()
#Scenario-B2: EHS Return Discount Cash billing
LBR.preEHSBillReport()
LB.returnBillingInvoice(EMR, InvoiceNo3, returnmsg="This is Return Invoice",)
LBR.getEHSBillReport(EMR)
LBR.verifyEHSBillReport()
#Scenario-B3: EHS Discount Credit billing
LBR.getEHSBillReport(EMR)
LBR.preEHSBillReport()
InvoiceNo4 = LA.patientquickentry(EMR, discountScheme=discountScheme, paymentmode='Credit', department=departmentGynae, doctor=doctorGynaeEHS, priceCategoryType=priceCategoryType).InvoiceNo
print("InvoiceNo4", InvoiceNo4)
LBR.getEHSBillReport(EMR)
LBR.verifyEHSBillReport()
#Scenario-B4: EHS Return Discount Credit billing
LBR.preEHSBillReport()
LB.returnBillingInvoice(EMR, InvoiceNo4, returnmsg="This is Return Invoice",)
LBR.getEHSBillReport(EMR)
LBR.verifyEHSBillReport()
AC.logout()
AC.closeBrowser()
