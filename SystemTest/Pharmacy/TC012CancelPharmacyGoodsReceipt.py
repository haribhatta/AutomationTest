from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

cpgr = A()
qty = 5
drugname = GSV.drug1BrandName
tqty = 2
tqty1 = 1
rate = GSV.drug1Rate
costPrice = 20
amount = qty * costPrice
print("amount", amount)
cpgr.openBrowser()
cpgr.login(pharmacyUserId, pharmacyUserPwd)
cpgr.activatePharmacyCounter()
#cpgr.addPharmacyItem(drugname)
#cpgr.verifyPharmacyItem()
cpgr.getPharmacyGoodsReceiptListAmount()
cpgr.XgetPharmacyGoodsReceiptListAmount()
cpgr.createPharmacyGoodsReceipt(qty=qty, DrugName=drugname, grPrice=costPrice)
cpgr.verifyPharmacyGoodsReceipt(qty=qty, DrugName=drugname)
cpgr.getPharmacyGoodsReceiptListAmount()
cpgr.verifygetPharmacyGoodsReceiptListAmount(amount=amount, discount=0)
cpgr.transferStore2DispensaryTC(tqty=tqty, DrugName=drugname)
cpgr.transferDispensary2StoreTC(tqty=tqty1)
cpgr.cancelPharmacyGoodsReceipt()
cpgr.verifyStockDetailTC()
cpgr.logout()
cpgr.closeBrowser()

# Test script is failing with bug: EMR-2801
