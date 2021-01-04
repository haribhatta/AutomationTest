from TestActionLibrary import A

qty = 50

pst = A()

pst.openBrowser()
pst.login('pharmacy1', 'pass123')
pst.activatePharmacyCounter()
pst.addPharmacyItem()
pst.verifyPharmacyItem()
pst.createPharmacyGoodsReceipt(qty)
pst.transferMain2Dispensary(qty)
pst.verifyDispensaryStock(qty)
