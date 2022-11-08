import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
import Library.LibModuleSettings as LS
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
userName = GSV.foUserName
#
opdRate = GSV.opdRate
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(GSV.adminUserID, GSV.adminUserPwD)
LS.ChangePaymentLabelSettingstoMaternityPayment(EMR)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LBR.getItemSummaryReport(danpheEMR=EMR)
LBR.storeItemSummaryReport()
invoiceNO = LB.createUSGinvoice(danpheEMR=EMR, HospitalNo=HospitalNo, USGtest=GSV.USG)
LBR.getItemSummaryReport(danpheEMR=EMR)
LBR.verifyItemSummaryReport(Return="No", qty=1.0, grossAmount=GSV.usgRate, discount=0, netAmount=GSV.usgRate)
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=invoiceNO, returnmsg="this is return bill")
LBR.getItemSummaryReport(danpheEMR=EMR)
LBR.verifyItemSummaryReport(Return="Yes", qty=1.0, grossAmount=GSV.usgRate, discount=0, netAmount=GSV.usgRate)
AC.logout()
AC.closeBrowser()
