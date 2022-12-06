import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LMPR
import Library.LibModuleSettings as LS

# pharmacy desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName
drugname = GSV.drug1BrandName
qty = 100
rate = GSV.drug1Rate
supplier = GSV.pharmacySupplierName1
returnQuantity = 2
returnRate = 2
########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplier, DrugName=drugname, itemQty=qty, freeQty=0, grPrice=rate, Margin=0, cc=0, discountPer=0, vatPer=0, NepaliReceipt=NepaliReceipt)
print(goodsReceiptNo)
LP.verifyPharmacyGoodsReceipt(EMR, brandName=drugname, genericName=GSV.drug1GenericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
creditnote = LP.return_to_supplier(danpheEMR=EMR, grno=goodsReceiptNo, returnqty=returnQuantity, returnRate=returnRate, returnDiscount=0, returnVat=0, returnCcCharge=0)
print(creditnote)
LMPR.getReturnToSupplierReport(EMR, creditno=creditnote)
AC.logout()
AC.closeBrowser()
