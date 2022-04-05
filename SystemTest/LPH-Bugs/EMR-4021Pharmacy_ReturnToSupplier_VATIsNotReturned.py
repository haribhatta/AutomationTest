import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModulePharmacy as LP

# pharmacy desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.adminUserPwD
genericName = GSV.drug1GenericName
drugName = GSV.drug1BrandName
drugRate = GSV.drug1Rate
supplierName = GSV.pharmacySupplierName1
dispensaryName = GSV.dispensaryName1
qty = 50

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplierName, qty=qty, DrugName=drugName, grPrice=drugRate)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=drugName, genericName=genericName, grno=goodsReceiptNo)
LP.return_to_supplier(danpheEMR=EMR, grno=goodsReceiptNo, rqty=11)
AC.logout()
AC.closeBrowser()