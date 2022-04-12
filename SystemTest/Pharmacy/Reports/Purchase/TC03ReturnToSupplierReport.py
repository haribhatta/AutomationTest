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
qty = 1
rate = GSV.drug1Rate
supplier = GSV.pharmacySupplierName1
########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
goodsReceiptNo = LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=2, DrugName=drugname, grPrice=5, NepaliReceipt=NepaliReceipt)
print(goodsReceiptNo)
LP.verifyPharmacyGoodsReceipt(EMR, brandName=drugname, genericName=GSV.drug1GenericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
creditnote = LP.return_to_supplier(danpheEMR=EMR, grno=goodsReceiptNo, rqty=1)
print(creditnote)
LMPR.getReturnToSupplierReport(EMR, creditno=creditnote)
AC.logout()
AC.closeBrowser()
