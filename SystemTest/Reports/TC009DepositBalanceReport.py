from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

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