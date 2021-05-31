from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

dbr = A()

deposit = 1000

dbr.openBrowser()
dbr.login(foUserId, foUserPwd)
dbr.counteractivation()
dbr.patientRegistration()
dbr.opDeposit(deposit)
dbr.verifyDepositBalanceReport(deposit)
dbr.logout()
dbr.closeBrowser()