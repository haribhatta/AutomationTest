from TestActionLibrary import A

# pharmacy desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

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
