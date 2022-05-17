'''
Scripted by: Hari P. Bhatta
Headline:
Pharmacy>GoodsReceipt: Similar GR information message should not be displayed for different batch no item entry.
Description:
Steps:
1. Create GR for Item-A and note down it's GR entry information.
2. Create GR same as per step 1 but with different batch entry and same rate as previous.

Issue: Similar GR information must have logic of duplicate batch number + current logic.
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
costPrice = 20
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
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplierName, qty=qty, DrugName=brandName, grPrice=costPrice, NepaliReceipt=NepaliReceipt)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=brandName, genericName=genericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LP.getPharmacyGoodsReceiptListAmount(EMR)
LP.verifygetPharmacyGoodsReceiptListAmount(amount=amount, discount=0)
AC.logout()
AC.closeBrowser()

# Test script is failing with bug: EMR-2801
