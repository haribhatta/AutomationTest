'''
Objective:
To test below check points:
1. Create pharmacy goods receipt
2. Cancel pharmacy goods receipt
3. Verify cancelled pharmacy goods receipt.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

qty = 5
drugname = GSV.drug1BrandName
tqty = 2
tqty1 = 1
rate = GSV.drug1Rate
costPrice = 20
amount = qty * costPrice
print("amount", amount)
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(danpheEMR=EMR, dispensaryName=GSV.dispensaryName)
#cpgr.addPharmacyItem(drugname)
#cpgr.verifyPharmacyItem()
LP.getPharmacyGoodsReceiptListAmount(EMR)
LP.XgetPharmacyGoodsReceiptListAmount()
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, qty=qty, DrugName=drugname, grPrice=costPrice)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, DrugName=drugname, grno=goodsReceiptNo)
LP.getPharmacyGoodsReceiptListAmount(EMR)
LP.verifygetPharmacyGoodsReceiptListAmount(amount=amount, discount=0)
LP.transferStore2DispensaryTC(danpheEMR=EMR, tqty=tqty, DrugName=drugname)
LP.transferDispensary2StoreTC(danpheEMR=EMR,tqty=tqty1)
LP.cancelPharmacyGoodsReceipt(EMR)
LP.verifyStockDetailTC(EMR)
AC.logout()
AC.closeBrowser()

# Test script is failing with bug: EMR-2801
