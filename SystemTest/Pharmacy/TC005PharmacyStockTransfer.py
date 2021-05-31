from TestActionLibrary import A
from GlobalShareVariables import GSV

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

PST = A()

drug = GSV.Testdrug
qty = 10
transferqty = 1

PST.openBrowser()
PST.login(pharmacyUserId, pharmacyUserPwd)
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
