from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

dbr = A()

dbr.openBrowser()
dbr.login(foUserId, foUserPwd)
dbr.counteractivation()
dbr.patientquickentry(0, 'Cash')
dbr.logout()
dbr.login(pharmacyUserId, pharmacyUserPwd)
dbr.activatePharmacyCounter()
dbr.addPharmacyDeposit(deposit=1000)
dbr.getPharmacyDepositBalanceReport()
dbr.addPharmacyDeposit(deposit=1000)
dbr.verifyPharmacyDepositBalanceReport(deposit=1000, depositreturn=0)
dbr.getPharmacyDepositBalanceReport()
dbr.returnPharmacyDeposit(depositreturn=500)
dbr.verifyPharmacyDepositBalanceReport(deposit=0, depositreturn=500)
dbr.logout()
dbr.closeBrowser()