'''
Objective:
To test Pharmacy> Item Wise Purchase report with below check points:

'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LMPR


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

########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=2, DrugName=drugname, grPrice=rate)
# Item Wise Purchase Start
LMPR.getItemWisePurchaseReport(EMR)
LMPR.preItemWisePurchaseReport()
goodsReceiptNo = LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=2, DrugName=drugname, grPrice=rate)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=GSV.drug1BrandName, genericName=GSV.drug1GenericName, grno=goodsReceiptNo)
LMPR.getItemWisePurchaseReport(EMR)
LMPR.verifyItemWisePurchaseReport(qty=2, purchaseValue=totalamount)
AC.logout()
AC.closeBrowser()


