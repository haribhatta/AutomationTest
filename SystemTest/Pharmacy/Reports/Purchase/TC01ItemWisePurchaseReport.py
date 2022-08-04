'''
Objective:
To test Pharmacy> Item Wise Purchase report with below check points:

'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LMPR
import Library.LibModuleSettings as LS

# pharmacy desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName
# front desk user login
billingId = GSV.foUserID
billingPwd = GSV.foUserPwD
drugname = GSV.drug1BrandName
qty = 2
rate = GSV.drug1Rate
amount = qty*rate
amount = int(amount)
totalamount = amount
supplier = GSV.pharmacySupplierName1
print("Total amount i.e rate * grprice ", totalamount)
VatAmount = totalamount * 0.13
print("Vat Amount of the Given Item is ", VatAmount)

########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplier, DrugName=drugname, itemQty=qty, freeQty=0, grPrice=rate, Margin=0, cc=0, discountPer=0, vatPer=0, NepaliReceipt=NepaliReceipt)
# Item Wise Purchase Start
LMPR.getItemWisePurchaseReport(EMR)
LMPR.preItemWisePurchaseReport()
goodsReceiptNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplier, DrugName=drugname, itemQty=qty, freeQty=5, grPrice=rate, Margin=100, cc=7.5, discountPer=10, vatPer=13, NepaliReceipt=NepaliReceipt)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=GSV.drug1BrandName, genericName=GSV.drug1GenericName, grno=goodsReceiptNo, NepaliReceipt=NepaliReceipt)
LMPR.getItemWisePurchaseReport(EMR)
LMPR.verifyItemWisePurchaseReport(qty=2, purchaseValue=totalamount, VatAmount=VatAmount)
AC.logout()
AC.closeBrowser()


