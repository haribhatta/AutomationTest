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
#AC.applicationSelection()
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
time.sleep(2)
LBR.getUserCollectionReport(EMR, user)
LBR.preSystemUserCollectionReport()
InvoiceNo = LA.patientquickentry(EMR, discountpc=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno).InvoiceNo
# LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, user)
LBR.verifyUserCollectionReport(cash=opdRate, cashreturn=0, credit=0, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0, maternityPayment=0)
time.sleep(2)
LB.returnBillingInvoice(EMR, InvoiceNo, returnmsg="This is Return Invoice",)
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, user)
LBR.verifyUserCollectionReport(cash=0, cashreturn=opdRate, credit=0, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0, maternityPayment=0)
InvoiceNo = LA.patientquickentry(EMR, discountpc=0, paymentmode='CREDIT', department=GSV.departmentGyno, doctor=GSV.doctorGyno).InvoiceNo
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, user)
LBR.verifyUserCollectionReport(cash=0, cashreturn=0, credit=opdRate, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0, maternityPayment=0)
LB.returnBillingInvoice(EMR, InvoiceNo, returnmsg="This is credit return.")
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(EMR, user)
LBR.verifyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=opdRate, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0, maternityPayment=0)
AC.logout()
AC.closeBrowser()
