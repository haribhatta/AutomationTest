import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LMPR


# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName

drugname = GSV.drug1BrandName
qty = 1
rate = GSV.drug1Rate
totalamount = qty*rate
remark = "This is test return."
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
supplier = GSV.supplier
########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=qty, DrugName=drugname, grPrice=rate)
LMPR.getSupplierStockReport(EMR, supplier=GSV.supplier)
LMPR.preSupplierStockReport()
goodsReceiptNo = LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=qty, DrugName=drugname, grPrice=rate)
LP.verifyPharmacyGoodsReceipt(EMR, DrugName=GSV.drug1BrandName, grno=goodsReceiptNo)
LP.cancelPharmacyGoodsReceipt(EMR)
LMPR.getSupplierStockReport(EMR, supplier=GSV.supplier)
LMPR.verifysupplierStockReport(qtyGR=qty, rateGR=rate)
AC.logout()
AC.closeBrowser()
# Test script is failling with bug:EMR-4788
