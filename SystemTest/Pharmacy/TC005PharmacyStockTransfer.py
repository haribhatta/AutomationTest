from TestActionLibrary import A


PST = A()

drug = 'testdrugreport'
qty = 10
transferqty = 1

PST.openBrowser()
PST.login("pharmacy1", "pass123")
PST.activatePharmacyCounter()
PST.getStoreDetail(drugname=drug)
PST.getStockDetail(drugname=drug)
PST.transferStore2Dispensary(drugname=drug, tqty=transferqty)
PST.verifyStockDetail(drugname=drug)
PST.verifyStoreDetail(drugname=drug)
PST.transferDispensary2Store(drugname=drug, tqty=transferqty)
PST.verifyStoreDetail(drugname=drug)
PST.verifyStockDetail(drugname=drug)

PST.logout()
PST.closeBrowser()
