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
genericName = GSV.drug1GenericName
qty = 1
rate = GSV.drug1Rate
totalamount = qty*rate
remark = "This is test return."
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
supplier = GSV.pharmacySupplierName1
########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplier, qty=qty, DrugName=drugname, grPrice=rate, NepaliReceipt=NepaliReceipt)
LMPR.getSupplierStockReport(danpheEMR=EMR, supplier=supplier)
LMPR.preSupplierStockReport()
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplier, qty=qty, DrugName=drugname, grPrice=rate, NepaliReceipt=NepaliReceipt)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=GSV.drug1BrandName, genericName=genericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LP.cancelPharmacyGoodsReceipt(danpheEMR=EMR, grNo=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LMPR.getSupplierStockReport(danpheEMR=EMR, supplier=supplier)
LMPR.verifysupplierStockReport(qtyGR=qty, rateGR=rate)
AC.logout()
AC.closeBrowser()
# Test script is failling with bug:EMR-4788
