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
discountType = GSV.discountScheme
#discountTypeName = GSV.discountSchemeName
#discountTypePct = GSV.discountSchemePct
#AC.applicationSelection()
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
time.sleep(2)
LBR.getReturnBillReport(EMR)
LBR.preReturnBillReprot()
InvoiceNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType="Normal").InvoiceNo
#Cash Bill Return
LB.returnBillingInvoice(EMR, InvoiceNo, "TestReturn")
LBR.getReturnBillReport(EMR)
LBR.verifyReturnBillReport(returnamt=opdRate, returnDiscount=0)
#Cash discount Bill Return
'''
InvoiceNo = LA.patientquickentry(EMR, discountType=discountType, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType="Normal").InvoiceNo
LBR.preReturnBillReprot()
LB.returnBillingInvoice(EMR, InvoiceNo, "TestReturn")
LBR.getReturnBillReport(EMR)
LBR.verifyReturnBillReport(returnamt=opdRate, returnDiscount=discountPct)
'''
#Credit Bill Return
InvoiceNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Credit', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType="Normal").InvoiceNo
LBR.preReturnBillReprot()
LB.returnBillingInvoice(EMR, InvoiceNo, "TestReturn")
LBR.getReturnBillReport(EMR)
LBR.verifyReturnBillReport(returnamt=opdRate, returnDiscount=0)
AC.logout()
AC.closeBrowser()
