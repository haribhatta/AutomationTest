
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModuleSettings as LS
#import Library.LibModuleBilling as LB

# pharmacy desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
genericName = GSV.drug1GenericName
drugName = GSV.drug1BrandName
drugRate = GSV.drug1Rate
supplierName = GSV.pharmacySupplierName1
dispensaryName = GSV.dispensaryName1
qty = 50

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, dispensaryName)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplierName, DrugName=drugName, itemQty=qty, freeQty=0, grPrice=drugRate, Margin=0, cc=0, discountPer=0, vatPer=0, NepaliReceipt=NepaliReceipt)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=drugName, genericName=genericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LP.cancelPharmacyGoodsReceipt(danpheEMR=EMR, grNo=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LP.createPharmacyGrwithSameInvoiceNumberAfterGrCancel(danpheEMR=EMR, invoiceNumber=goodsReceiptNo, supplier=supplierName, qty=qty, DrugName=drugName, grPrice=drugRate, NepaliReceipt=NepaliReceipt)
AC.logout()
AC.closeBrowser()
