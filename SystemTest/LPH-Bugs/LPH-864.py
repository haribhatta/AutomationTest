''''
BIlling>ReturnInvoice: Dashboard amount mismatch on cash bill return.

Steps:1. Return bill invoice and verify bill dashboard data.

Issue:
1. 'Subtotal' amount is getting increase.
2. 'Total Amount', 'User Collection', 'Counter Collection' & 'Net Cash Collection' remains same.

'''

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
doctor = GSV.doctor1
department = GSV.department1

opdticket = GSV.opdRate
discountpct = 50
#discountamount = (discountpct*opdticket/100)
returnamount = opdticket
usgtest = GSV.USG
usgprice = GSV.usgRate
admisioncharge = GSV.admitRate
deposit = 1000

CBDS = A()
CBDS.openBrowser()
CBDS.login(foUserId, foUserPwd)
CBDS.counteractivation()

# 1. Cash Invoice
CBDS.getBillingDashboard()
CBDS.patientquickentry(discountpc=0, paymentmode="Cash")  # cash = opdticket
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=opdticket, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 2. Return Cash Invoice
print("2. Return Cash Invoice")
CBDS.getBillingDashboard()
CBDS.returnBillingInvoice("This is cash invoice return")
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)
