'''
Objective:
To test below check points:
1. Create pharmacy goods receipt
2. Transfer GR Items from Pharmacy/Store >> Dispensary
3. Return back GR Items from Dispensary >> Pharmacy/Store (Note: with out consuming)
2. Cancel pharmacy goods receipt
3. Verify cancelled pharmacy goods receipt.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModuleSettings as LS
# front desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.adminUserPwD

qty = 5
brandName = GSV.drug1BrandName
genericName = GSV.drug1GenericName
tqty = 1
rate = GSV.drug1Rate
amount = qty * rate
print("amount", amount)
supplierName = GSV.pharmacySupplierName1
dispensaryName = GSV.dispensaryName1
########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
flagReceiveItemInDispensary = LS.EnableReceiveItemsInDispensary(EMR)
LD.activateDispensaryCounter(danpheEMR=EMR, dispensaryName=dispensaryName)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
#cpgr.addPharmacyItem(drugname)
#cpgr.verifyPharmacyItem()
LP.getPharmacyGoodsReceiptListAmount(EMR)
LP.XgetPharmacyGoodsReceiptListAmount()
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplierName, DrugName=brandName, itemQty=qty, freeQty=0, grPrice=rate, Margin=0, cc=0, discountPer=0, vatPer=0, NepaliReceipt=NepaliReceipt)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=brandName, genericName=genericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LP.getPharmacyGoodsReceiptListAmount(EMR)
LP.verifygetPharmacyGoodsReceiptListAmount(amount=amount, discount=0)
LP.cancelPharmacyGoodsReceipt(EMR, grNo=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
AC.logout()
AC.closeBrowser()

# Test script is failing with bug: EMR-2801
