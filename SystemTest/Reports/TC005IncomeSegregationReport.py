#Scenarios to test:
# Same Day:
# 1. Cash Invoice, 2. Return Cash Invoice,
# 3. Credit Invoice, 4. Return Credit Invoice,
# 5. Credit Payment,
# 6.Provisional billing, 7.Cancel Provisional bill,
# 8.Deposit, 9.Deduct Deposit, 10.Refund Deposit
# 11.Repeat Scenarios 1-10 for different date.

from TestActionLibrary import A

usgtest = "USG (Abdomen / pelvis)"
usgprice = 1050

isr = A()
isr.openBrowser()
isr.login('billing1', 'pass123')
isr.counteractivation()
isr.getIncomeSegregation()
isr.patientquickentry(0, 'Cash')
isr.preSystemIncomeSegregation()
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=500, cashreturn=0, credit=0, creditreturn=0, provision=0)
isr.preSystemIncomeSegregation()
isr.returnBillingInvoice(returnmsg="this is bill return 1")
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=0, cashreturn=500, credit=0, creditreturn=0, provision=0)
isr.patientquickentry(0, 'CREDIT')
isr.preSystemIncomeSegregation()
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=0, cashreturn=0, credit=500, creditreturn=0, provision=0)
isr.preSystemIncomeSegregation()
isr.returnBillingInvoice(returnmsg="this is bill return 2")
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=0, cashreturn=0, credit=0, creditreturn=500, provision=0)
isr.patientquickentry(0, 'Cash')
isr.admitDisTrans(1, 0, 0, 0)
isr.getIncomeSegregation()
isr.createIPprovisionalBill(usgtest)
isr.preSystemIncomeSegregation()
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=0, cashreturn=0, credit=0, creditreturn=0, provision=usgprice)

isr.logout()
isr.closeBrowser()

