'''
Objective:
To test below check points:
1. Create Pharmacy goods receipt.
2. Verify Pharmacy goods receipt.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModuleSettings as LS

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
genericName = GSV.drug1GenericName
drugName = GSV.drug1BrandName
drugRate = GSV.drug1Rate
supplierName = GSV.pharmacySupplierName1
dispensaryName = GSV.dispensaryName1
qty = 50
freeQuantity = 0
margin = 0
ccCharge = 0
discount = 0
vat = 0
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, dispensaryName)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplierName, DrugName=drugName, itemQty=qty, freeQty=freeQuantity, grPrice=drugRate, Margin=margin, cc=ccCharge, discountPer=discount, vatPer=vat, NepaliReceipt=NepaliReceipt)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=drugName, genericName=genericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
AC.logout()
AC.closeBrowser()
#Blocked by bug EMR-2591
#Failed with bug EMR-3177