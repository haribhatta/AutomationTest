#Objective: To cover the OPD bill amount deduction from deposit balance where deposit balance > Total Amount.

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

CBC = GSV.CBC

DepositAmount = 5000

bsdd = A()

bsdd.openBrowser()
bsdd.login(foUserId, foUserPwd)
bsdd.counteractivation()
bsdd.patientRegistration()
bsdd.opDeposit(DepositAmount)
bsdd.opDepositDbiling(DepositAmount, CBC)
bsdd.logout()
bsdd.closeBrowser()
