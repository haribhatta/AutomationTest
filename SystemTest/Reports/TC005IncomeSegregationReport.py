#Scenarios to test:
# Same Day:
# 1. Cash Invoice, 2. Return Cash Invoice,
# 3. Credit Invoice, 4. Return Credit Invoice,
# 5. Credit Payment,
# 6.Provisional billing, 7.Cancel Provisional bill,
# 8.Deposit, 9.Deduct Deposit, 10.Refund Deposit
# 11.Repeat Scenarios 1-10 for different date.

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

rateOPD = GSV.opdRate
usgtest = GSV.USG
usgprice = GSV.usgRate
doctor = GSV.doctor1
department = GSV.department1

isr = A()
isr.openBrowser()
isr.login(foUserId, foUserPwd)
isr.counteractivation()
isr.getIncomeSegregation()
isr.patientquickentry(0, 'Cash')
isr.preSystemIncomeSegregation()
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=rateOPD, cashreturn=0, credit=0, creditreturn=0, provision=0)
print(">>>>>>Start>Cash Return")
isr.preSystemIncomeSegregation()
isr.returnBillingInvoice(returnmsg="this is bill return 1")
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=0, cashreturn=rateOPD, credit=0, creditreturn=0, provision=0)

isr.patientquickentry(0, 'CREDIT')
isr.preSystemIncomeSegregation()
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=0, cashreturn=0, credit=rateOPD, creditreturn=0, provision=0)

isr.preSystemIncomeSegregation()
isr.returnBillingInvoice(returnmsg="this is bill return 2")
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=0, cashreturn=0, credit=0, creditreturn=rateOPD, provision=0)

isr.patientquickentry(0, 'Cash')
isr.admitDisTrans(1, 0, 0, 0, doctor=doctor, department=department)
isr.getIncomeSegregation()
isr.createIPprovisionalBill(usgtest)
isr.preSystemIncomeSegregation()
isr.getIncomeSegregation()
isr.verifyIncomeSegregation(cash=0, cashreturn=0, credit=0, creditreturn=0, provision=usgprice)

isr.logout()
isr.closeBrowser()

