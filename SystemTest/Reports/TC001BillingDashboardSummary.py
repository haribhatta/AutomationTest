# Objective: To Check Billing Dashboard Summary.
# Scenarios to cover:
# 1. Cash Invoice,
# 2. Return Cash Invoice,
# 3. Cash Discount Invoice,
# 4. Return Cash Discount Invoice,
# 5. Credit Invoice,
# 6. Return Credit Invoice,
# 7. Credit Payment,
# 8. Provisional Bill,
# 9. Cancel Provisional Bill,
# 10. Deposit,
# 11. Deposit Deduct,
# 12. Deposit Refund.

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

# 3. Cash Discount Invoice
CBDS.getBillingDashboard()
CBDS.patientquickentry(discountpc=discountpct, paymentmode="Cash")
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=opdticket, discountpc=discountpct, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 4. Return Cash Discount Invoice
CBDS.getBillingDashboard()
CBDS.returnBillingInvoice("This is cash discount invoice return")
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=0, discountpc=discountpct, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 5. Credit Invoice
print("##### Credit Invoice #####")
CBDS.getBillingDashboard()
CBDS.patientquickentry(discountpc=0, paymentmode="CREDIT")
#CBDS.verifyopdinvoice()
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=opdticket, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 6. Return Credit Invoice
CBDS.getBillingDashboard()
print("Returning Credit Invoice")
CBDS.returnBillingInvoice("This is credit invoice return")
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=opdticket,
                            settlement=0, provisional=0, provisionalcancel=0)

# 7. Credit Payment
CBDS.getBillingDashboard()
CBDS.patientquickentry(discountpc=0, paymentmode="CREDIT") #credit=opdticket
#CBDS.verifyopdinvoice()
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.creditPayment()        #settlement=credit
CBDS.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=opdticket, creditReturn=0,
                            settlement="CREDIT", provisional=0, provisionalcancel=0)

# 8.1 Provisional Bill
CBDS.getBillingDashboard()
CBDS.patientRegistration()
CBDS.createProvisionalBill(usgtest)  #provisional=usgprice
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0,
                            provisional=usgprice, provisionalcancel=0)

# 8.2 Provisional IP Bill
CBDS.patientRegistration()
CBDS.getBillingDashboard()
CBDS.admitDisTrans(1, 0, 0, deposit, doctor=doctor, department=department)
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=admisioncharge, provisionalcancel=0)
CBDS.createIPprovisionalBill(usgtest)
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=usgprice, provisionalcancel=0)


# 9. Cancel Provisional Bill
CBDS.getBillingDashboard()
CBDS.cancelIPprovisionalBill(usgtest)
CBDS.preSystemDataBillingDashboard()
CBDS.getBillingDashboard()
CBDS.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0,
                            provisional=0, provisionalcancel=usgprice)

print(" EMR-2571: is existing bug to cancel provisional bill")
CBDS.logout()
CBDS.closeBrowser()
#End of the test case




