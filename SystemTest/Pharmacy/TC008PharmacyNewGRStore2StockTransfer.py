from TestActionLibrary import A
from GlobalShareVariables import GSV

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

qty = 50

pst = A()

pst.openBrowser()
pst.login(pharmacyUserId, pharmacyUserPwd)
pst.activatePharmacyCounter()
pst.addPharmacyItem()
pst.verifyPharmacyItem()
pst.createPharmacyGoodsReceipt(qty)
pst.transferMain2Dispensary(qty)
pst.verifyDispensaryStock(qty)
