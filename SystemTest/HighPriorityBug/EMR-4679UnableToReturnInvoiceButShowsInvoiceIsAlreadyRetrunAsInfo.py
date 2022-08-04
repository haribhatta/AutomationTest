'''
Objective:
To test below check points:
1. Create pharmacy invoice.
2. Return pharmacy invoice.
3. Verify pharmacy invoice return.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModulePharmacy as LP
import Library.LibModuleBilling as LB
import Library.LibModuleSettings as LS

# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

drugname = GSV.drug1BrandName
quantity = 2
rate = GSV.drug1Rate
returnremark = "This is auto return"
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
paymentmode = "CREDIT"
gRNo =LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=GSV.pharmacySupplierName1, DrugName=drugname, itemQty=quantity, freeQty=0, grPrice=rate, Margin=0, cc=0, discountPer=0, vatPer=0, NepaliReceipt=NepaliReceipt)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, brandName=GSV.drug1BrandName, genericName=GSV.drug1BrandName, grno=gRNo, NepaliReceipt=NepaliReceipt)
LP.return_to_supplier(danpheEMR=EMR, grno=gRNo, rqty=2)
AC.logout()
AC.closeBrowser()
