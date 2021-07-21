# Happy Path

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

PSMI = A()

drug = GSV.Testdrug
drugGenericName = GSV.drug1GenericName
drugPrice = GSV.drug1Rate

qty = 10

PSMI.openBrowser()
PSMI.login(pharmacyUserId, pharmacyUserPwd)
PSMI.activatePharmacyCounter()
PSMI.addPharmacyItem(drugGenericName)
PSMI.createPharmacyGoodsReceipt(qty=qty, drug, grPrice=drugPrice)
PSMI.getStoreDetail(drugname=drug)
PSMI.manageStoreStock(drugname=drug, type="In", qty=qty)
PSMI.verifyStoreDetail(drugname=drug)
PSMI.getStoreDetail(drugname=drug)
PSMI.manageStoreStock(drugname=drug, type="Out", qty=qty)
PSMI.verifyStoreDetail(drugname=drug)

PSMI.logout()
PSMI.closeBrowser()
