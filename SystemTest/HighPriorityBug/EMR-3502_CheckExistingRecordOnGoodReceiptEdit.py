'''
Scripted by: Hari P. Bhatta
Headline:
Pharmacy -> Order: Existing record is not populated when item edit.
Description:
Steps to Reproduce:
1. Navigate to Pharmacy -> Order
2. Add Purchase order and Print
3. Proceed to Add the Good Receipt from Order List
4. In the Good Receipt Page Pending Order quantity is as per the Purchase Order
5. Edit the item and see the record in the pending qty as '0'.

Issue: Pending quantity is not displaying correct value.

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
costPrice = GSV.drug1CostPrice
amount = qty * costPrice
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
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplierName, DrugName=brandName, itemQty=qty, freeQty=0, grPrice=costPrice, Margin=0, cc=0, discountPer=0, vatPer=0, NepaliReceipt=NepaliReceipt)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=brandName, genericName=genericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LP.getPharmacyGoodsReceiptListAmount(EMR)
LP.verifygetPharmacyGoodsReceiptListAmount(amount=amount, discount=0)
LP.editPharmacyGoodsReceipt(danpheEMR=EMR, grNo=goodsReceiptNo, NepaliReceipt=0)

AC.logout()
AC.closeBrowser()

# Test script is failing with bug: EMR-2801
