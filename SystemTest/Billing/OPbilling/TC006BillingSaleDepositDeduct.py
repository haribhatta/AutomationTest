#Objective: To cover the OPD bill amount deduction from deposit balance where deposit balance > Total Amount.

from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

DepositAmount = 5000
testname = "CBC(Hb,TC,DC,PLT)"

bsdd = A()

bsdd.openBrowser()
bsdd.login(foUserId, foUserPwd)
bsdd.counteractivation()
bsdd.patientRegistration()
bsdd.opDeposit(DepositAmount)
bsdd.opDepositDbiling(DepositAmount, testname)
bsdd.logout()
bsdd.closeBrowser()
