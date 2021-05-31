#Objective: To cover the OPD bill amount deduction from deposit balance where deposit balance < Total Amount and cash return from tender.

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

deposit = "200"
testname = GSV.CBC

bsddpt = A()
bsddpt.openBrowser()
bsddpt.login(foUserId, foUserPwd)
bsddpt.counteractivation()
bsddpt.patientRegistration()
bsddpt.opDeposit(deposit)
bsddpt.opDepositDbilingTenderCashReturn(deposit, testname)
bsddpt.logout()
bsddpt.closeBrowser()


