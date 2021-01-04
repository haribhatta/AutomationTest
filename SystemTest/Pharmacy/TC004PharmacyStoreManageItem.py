# Happy Path

from TestActionLibrary import A


PSMI = A()

drug = "testdrugreport"
qty = 10

PSMI.openBrowser()
PSMI.login("pharmacy1", "pass123")
PSMI.activatePharmacyCounter()
PSMI.addPharmacyItem()
PSMI.createPharmacyGoodsReceipt(qty=qty)
PSMI.getStoreDetail(drugname=drug)
PSMI.manageStoreStock(drugname=drug, type="In", qty=qty)
PSMI.verifyStoreDetail(drugname=drug)
PSMI.getStoreDetail(drugname=drug)
PSMI.manageStoreStock(drugname=drug, type="Out", qty=qty)
PSMI.verifyStoreDetail(drugname=drug)

PSMI.logout()
PSMI.closeBrowser()
