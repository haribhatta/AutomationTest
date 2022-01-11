import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR

EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
rateOPD = GSV.opdRate
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LBR.getSalesDayBook(EMR)
###
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).InvoiceNo
LBR.preSystemSalesDayBook()
LBR.getSalesDayBook(EMR)
LBR.verifySalesDayBook(cash=rateOPD, cashreturn=0, credit=0, creditreturn=0)
###
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo, returnmsg="this is bill return 1")
LBR.preSystemSalesDayBook()
LBR.getSalesDayBook(EMR)
LBR.verifySalesDayBook(cash=0, cashreturn=rateOPD, credit=0, creditreturn=0)
###
InvoiceNo1 = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='CREDIT', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).InvoiceNo
LBR.preSystemSalesDayBook()
LBR.getSalesDayBook(EMR)
LBR.verifySalesDayBook(cash=0, cashreturn=0, credit=rateOPD, creditreturn=0)
###
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo1, returnmsg="this is bill retur 2n")
LBR.preSystemSalesDayBook()
LBR.getSalesDayBook(EMR)
LBR.verifySalesDayBook(cash=0, cashreturn=0, credit=0, creditreturn=rateOPD)
###
AC.logout()
AC.closeBrowser()
