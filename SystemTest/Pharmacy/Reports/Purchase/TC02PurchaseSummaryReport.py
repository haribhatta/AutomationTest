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
import Library.LibModuleSettings as LS
import Library.LibModulePharmacyReports as LMPR


# pharmacy desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName
# front desk user login
billingId = GSV.foUserID
billingPwd = GSV.foUserPwD
drugname = GSV.drug1BrandName
genericName = GSV.drug1GenericName
qty = 2
rate = GSV.drug1Rate
amount = qty*rate
totalamount = amount
returnRate = 1
remark = "This is test return."
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
supplier = GSV.pharmacySupplierName1
returnAmount = qty * returnRate
########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LMPR.getPurchaseSummaryReport(EMR)
LMPR.prePurchaseSummaryReport()
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplier, DrugName=drugname, itemQty=qty, freeQty=0, grPrice=rate, Margin=0, cc=0, discountPer=0, vatPer=0, NepaliReceipt=NepaliReceipt)
print(goodsReceiptNo)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=drugname, genericName=genericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LP.cancelPharmacyGoodsReceipt(EMR, grNo=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LMPR.getPurchaseSummaryReport(EMR)
LMPR.verifypurchasesummarybeforeReturn()
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplier, DrugName=drugname, itemQty=qty, freeQty=0, grPrice=rate, Margin=0, cc=0, discountPer=0, vatPer=0, NepaliReceipt=NepaliReceipt)
print(goodsReceiptNo)
LP.return_to_supplier(danpheEMR=EMR, grno=goodsReceiptNo, returnqty=qty, returnRate=returnRate, returnDiscount=0, returnVat=0, returnCcCharge=0)
LMPR.getPurchaseSummaryReport(EMR)
# retamt == grPrice ie goodreceipt amount while doing Good receipt
LMPR.verifypurchaseSummaryAfterReturn(retamt=returnAmount)
AC.logout()
AC.closeBrowser()


