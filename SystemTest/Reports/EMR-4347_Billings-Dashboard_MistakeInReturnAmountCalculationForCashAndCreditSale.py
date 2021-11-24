'''
Issue : Return amount is not subtracted from Subtotal.

Steps to reproduce:
1. Navigate to the billing>make cash sales and credit sales.
2. Now make sale return and check the billing dashboard.

Expected result:
The total amount in the billing dashboard(cash sales and credit sales should be the subtract of subtotal amount and return amount).

Actual result:
The total amount is equal to the sub total amount(cash sales and credit sales).
This cause the calculation error in the net cash collection.
'''

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT
AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno

opdticket = GSV.opdRate
discountpct = 50
#discountamount = (discountpct*opdticket/100)
returnamount = opdticket
usgtest = GSV.USG
usgprice = GSV.usgRate
admisioncharge = GSV.admitRate
deposit = 1000
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
########
# 1. Cash Invoice
LBR.getBillingDashboard()
LBR.preSystemDataBillingDashboard()
InvoiceNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).InvoiceNo  # cash = opdticket
LBR.getBillingDashboard()
LBR.verifyBillingDashboard(cash=opdticket, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)
# 2. Return Cash Invoice
print("2. Return Cash Invoice")
LBR.getBillingDashboard()
LBR.preSystemDataBillingDashboard()
LB.returnBillingInvoice(InvoiceNo, returnmsg='This is bug testing')
LBR.getBillingDashboard()
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)
# 5. Credit Invoice
print("##### Credit Invoice #####")
LBR.getBillingDashboard()
InvoiceNo1 = LA.patientquickentry(discountpc=0, paymentmode='CREDIT', department=departmentGynae, doctor=doctorGynae).InvoiceNo
LBR.preSystemDataBillingDashboard()
LBR.getBillingDashboard()
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=opdticket, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)
# 6. Return Credit Invoice
LBR.getBillingDashboard()
print("Returning Credit Invoice")
LB.returnBillingInvoice(InvoiceNo1, returnmsg="Bug testing")
LBR.preSystemDataBillingDashboard()
LBR.getBillingDashboard()
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=opdticket,
                            settlement=0, provisional=0, provisionalcancel=0)
AC.logout()
AC.closeBrowser()
#End of the test case




