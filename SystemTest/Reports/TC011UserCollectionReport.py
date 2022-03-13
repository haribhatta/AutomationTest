import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
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
AC.login(foUserId, foUserPwd)
AC.verifyLogIn(EMR)
LB.counteractivation(EMR)
time.sleep(2)
#####Scenario: Cash Invoice with no Discount
LBR.getUserCollectionReport(EMR, userName)
LBR.preSystemUserCollectionReport()
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
LBR.getUserCollectionReport(EMR, userName)
LBR.verifyUserCollectionReport(cash=opdRate, cashreturn=0, credit=0, creditreturn=0, cashDiscount=0, tradeDiscount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
time.sleep(2)
#####Scenario: Return Cash Invoice with no Discount
LB.returnBillingInvoice(EMR, InvoiceNo, returnmsg="This is Return Invoice",)
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, userName)
LBR.verifyUserCollectionReport(cash=0, cashreturn=opdRate, credit=0, creditreturn=0, cashDiscount=0, tradeDiscount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
#####Scenario: Credit Invoice with no Discount
HospitalNo1, InvoiceNo1, discountPercentage1 = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Credit', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, userName)
LBR.verifyUserCollectionReport(cash=0, cashreturn=0, credit=opdRate, creditreturn=0, cashDiscount=0, tradeDiscount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
#####Scenario: Return Credit Invoice with no Discount
LB.returnBillingInvoice(EMR, InvoiceNo1, returnmsg="This is credit return.")
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, userName)
LBR.verifyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=opdRate, cashDiscount=0, tradeDiscount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
AC.logout()
AC.closeBrowser()
