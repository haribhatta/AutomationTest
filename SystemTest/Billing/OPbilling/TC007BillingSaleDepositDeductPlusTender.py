#Objective: To cover the OPD bill amount deduction from deposit balance where deposit balance < Total Amount.

from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

deposit = 50
billamt = 500
testname = "CBC(Hb,TC,DC,PLT)"

bsddpt = A()
bsddpt.openBrowser()
bsddpt.login(foUserId, foUserPwd)
bsddpt.counteractivation()
bsddpt.patientRegistration()
bsddpt.opDeposit(deposit)
bsddpt.opDepositDbiling(deposit, testname)
bsddpt.verifyopdinvoice(deposit, billamt)
bsddpt.logout()
bsddpt.closeBrowser()


