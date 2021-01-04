from TestActionLibrary import A

dbr = A()

deposit = 1000

dbr.openBrowser()
dbr.login('billing1', 'pass123')
dbr.counteractivation()
dbr.patientRegistration()
dbr.opDeposit(deposit)
dbr.verifyDepositBalanceReport(deposit)
dbr.logout()
dbr.closeBrowser()