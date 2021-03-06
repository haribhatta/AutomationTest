from TestActionLibrary import A

# front desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

smdr = A()
drug = 'testdrugreport'
setupqty = 5
testqty = 7

smdr.openBrowser()
smdr.login(pharmacyUserId, pharmacyUserPwd)
smdr.activatePharmacyCounter()
smdr.getStoreDetail(drugname=drug)
smdr.manageStoreStock(drugname=drug, type='In', qty=setupqty)
smdr.getPharmacyStockManageDetailReport(drugname=drug)
smdr.preSystemPharmacyStockManageDetailReport()
smdr.manageStoreStock(drugname=drug, type='In', qty=testqty)
smdr.getPharmacyStockManageDetailReport(drugname=drug)
smdr.verifyPharmacyStockManageDetailReport(In=testqty, Out=0)
#Blocked by EMR-2588