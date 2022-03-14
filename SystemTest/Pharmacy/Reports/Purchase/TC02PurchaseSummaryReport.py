'''
Objective:
To test Pharmacy> User Collection report with below check points:
1. Cash Sale
2. Cash Sale Return
3. Credit Sale
4. Credit Settlement
5. Credit Sale Return
6. Deposit
7. Deposit Return
8. Estimation bill (i.e. Provisional).
9. Cancel estimation bill.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleBilling as LB
import Library.LibModulePharmacyReports as LMPR


# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName
# front desk user login
billingId = GSV.foUserID
billingPwd = GSV.foUserPwD
drugname = GSV.drug1BrandName
genericName = GSV.drug1GenericName
qty = 1
rate = GSV.drug1Rate
amount = qty*rate
totalamount = amount
remark = "This is test return."
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
supplier = GSV.pharmacySupplierName1
########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LMPR.getPurchaseSummaryReport(EMR)
LMPR.prePurchaseSummaryReport()
goodsReceiptNo = LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=2, DrugName=drugname, grPrice=5)
print(goodsReceiptNo)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=drugname, genericName=genericName, grno=goodsReceiptNo)
LP.cancelPharmacyGoodsReceipt(EMR)
LMPR.getPurchaseSummaryReport(EMR)
LMPR.verifypurchasesummarybeforeReturn()
goodsReceiptNo = LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=2, DrugName=drugname, grPrice=5)
print(goodsReceiptNo)
LP.return_to_supplier(danpheEMR=EMR, grno=goodsReceiptNo, rqty=1)
LMPR.getPurchaseSummaryReport(EMR)
# retamt == grPrice ie goodreceipt amount while doing Good receipt
LMPR.verifypurchaseSummaryAfterReturn(retamt=5)
AC.logout()
AC.closeBrowser()


