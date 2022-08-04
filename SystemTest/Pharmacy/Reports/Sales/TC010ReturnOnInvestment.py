'''
Objective:
To test Pharmacy> ROI

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
qty = float(100)
rate = float(50.25)
amount = qty*rate
amount = float(amount)
freeQuantity = float(50)
margin = 0.00
ccCharge = 7.5
discount = 15.00
vat = 13.00
supplier = GSV.pharmacySupplierName1

########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
grNo = LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplier, DrugName=drugname, itemQty=qty, freeQty=freeQuantity, grPrice=rate, Margin=margin, cc=ccCharge, discountPer=discount, vatPer=vat, NepaliReceipt=NepaliReceipt)
LMPR.getReturnOnInvestmentReport(danpheEMR=EMR, gRNo=grNo)
LMPR.verifyROIReport(supplier=supplier, itemRate=rate, DrugName=drugname, itemQty=qty, freeItemQty=freeQuantity, grPrice=rate, Margin=margin, cc=ccCharge, discountPer=discount, vatPer=vat)
AC.logout()
AC.closeBrowser()


