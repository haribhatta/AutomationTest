import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

user = GSV.foUserID
#
opdRate = GSV.opdRate
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
AC.verifyLogIn(EMR)
LB.counteractivation(EMR)
time.sleep(2)
#####Scenario: Cash Invoice with no Discount
LBR.getUserCollectionReport(EMR, user)
LBR.preSystemUserCollectionReport()
InvoiceNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).InvoiceNo
LBR.getUserCollectionReport(EMR, user)
LBR.verifyUserCollectionReport(cash=opdRate, cashreturn=0, credit=0, creditreturn=0, cashDiscount=0, tradeDiscount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
time.sleep(2)
#####Scenario: Return Cash Invoice with no Discount
LB.returnBillingInvoice(EMR, InvoiceNo, returnmsg="This is Return Invoice",)
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, user)
LBR.verifyUserCollectionReport(cash=0, cashreturn=opdRate, credit=0, creditreturn=0, cashDiscount=0, tradeDiscount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
#####Scenario: Credit Invoice with no Discount
InvoiceNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Credit', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).InvoiceNo
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, user)
LBR.verifyUserCollectionReport(cash=0, cashreturn=0, credit=opdRate, creditreturn=0, cashDiscount=0, tradeDiscount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
#####Scenario: Return Credit Invoice with no Discount
LB.returnBillingInvoice(EMR, InvoiceNo, returnmsg="This is credit return.")
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, user)
LBR.verifyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=opdRate, cashDiscount=0, tradeDiscount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
AC.logout()
AC.closeBrowser()
