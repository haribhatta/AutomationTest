''''
BIlling>ReturnInvoice: Dashboard amount mismatch on cash bill return.

Steps:1. Return bill invoice and verify bill dashboard data.

Issue:
1. 'Subtotal' amount is getting increase.
2. 'Total Amount', 'User Collection', 'Counter Collection' & 'Net Cash Collection' remains same.

'''

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LS
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
doctor = GSV.doctorGyno
department = GSV.departmentGyno

opdticket = GSV.opdRate
discountpct = 50
#discountamount = (discountpct*opdticket/100)
returnamount = opdticket
usgtest = GSV.USG
usgprice = GSV.usgRate
admisioncharge = GSV.admitRate
deposit = 1000

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)

# 1. Cash Invoice
LBR.getBillingDashboard(EMR)
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode="Cash", department=department, doctor=doctor).InvoiceNo  # cash = opdticket
LBR.preSystemDataBillingDashboard()
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=opdticket, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 2. Return Cash Invoice
print("2. Return Cash Invoice")
LBR.getBillingDashboard(EMR)
LB.returnBillingInvoice(EMR, InvoiceNo, "This is cash invoice return")
LBR.preSystemDataBillingDashboard()
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)
