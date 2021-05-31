#Objective: To cover the OPD bill amount deduction from deposit balance where deposit balance < Total Amount.

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

deposit = 50
billamt = GSV.opdRate
testname = GSV.TFT

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


