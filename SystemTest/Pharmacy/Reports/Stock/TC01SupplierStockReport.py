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
amount = qty*rate
totalamount = amount
remark = "This is test return."
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
supplier = GSV.supplier
########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=2, DrugName=drugname, grPrice=5)
LMPR.getSupplierStockReport(EMR, supplier=GSV.supplier)
LMPR.preSupplierStockReport()
LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=2, DrugName=drugname, grPrice=5)
LP.verifyPharmacyGoodsReceipt(EMR, DrugName=GSV.drug1BrandName)
LP.cancelPharmacyGoodsReceipt(EMR)
LMPR.getSupplierStockReport(EMR, supplier=GSV.supplier)
LMPR.verifysupplierStockReport()
AC.logout()
AC.closeBrowser()
# Test script is failling with bug:EMR-4788
