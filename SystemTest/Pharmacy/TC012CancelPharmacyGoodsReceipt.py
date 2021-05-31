from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

cpgr = A()
qty = 5
drugname = "test"
tqty = 2
tqty1 = 1
rate = 270
amount = qty * rate

cpgr.openBrowser()
cpgr.login(pharmacyUserId, pharmacyUserPwd)
cpgr.activatePharmacyCounter()
cpgr.addPharmacyItem()
cpgr.verifyPharmacyItem()
cpgr.getPharmacyGoodsReceiptListAmount()
cpgr.XgetPharmacyGoodsReceiptListAmount()
cpgr.createPharmacyGoodsReceipt(qty=qty)
cpgr.verifyPharmacyGoodsReceipt(qty=qty)
cpgr.getPharmacyGoodsReceiptListAmount()
cpgr.verifygetPharmacyGoodsReceiptListAmount(amount=amount, discount=0)
cpgr.transferStore2DispensaryTC(tqty=tqty)
cpgr.transferDispensary2StoreTC(tqty=tqty1)
cpgr.cancelPharmacyGoodsReceipt()
cpgr.verifyStockDetailTC()
cpgr.logout()
cpgr.closeBrowser()

# Test script is failing with bug: EMR-2801
