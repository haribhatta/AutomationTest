from TestActionLibrary import A

smdr = A()
drug = 'testdrugreport'
setupqty = 5
testqty = 7

smdr.openBrowser()
smdr.login('pharmacy1', 'pass123')
smdr.activatePharmacyCounter()
smdr.getStoreDetail(drugname=drug)
smdr.manageStoreStock(drugname=drug, type='In', qty=setupqty)
smdr.getPharmacyStockManageDetailReport(drugname=drug)
smdr.preSystemPharmacyStockManageDetailReport()
smdr.manageStoreStock(drugname=drug, type='In', qty=testqty)
smdr.getPharmacyStockManageDetailReport(drugname=drug)
smdr.verifyPharmacyStockManageDetailReport(In=testqty, Out=0)
#Blocked by EMR-2588