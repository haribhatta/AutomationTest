# scripting blocked due to bug: EMR-2587
'''
Objective:
To test Pharmacy> Narcotic Stock Report with below check points:
Precondition: Drug-Narcotic
1. Cash Sale
2. Cash Sale Return
3. Credit Sale
4. Credit Settlement
5. Credit Sale Return
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleSettings as LS
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacyReports as LPR


# pharmacy desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName
# front desk user login
billingId = GSV.foUserID
billingPwd = GSV.foUserPwD

drugName = GSV.drug1NarcoticName
drugRate = GSV.drug1NarcoticRate
qty = 1
totalAmount = qty*drugRate
remark = "This is test return."
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
supplier = GSV.pharmacySupplierName1
########
EMR = AC.openBrowser()
# Start of Narcotic Stock Report
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
grNO = LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=2, DrugName=drugName, grPrice=5, NepaliReceipt=NepaliReceipt)
LPR.verifynarcoticstockreport(danpheEMR=EMR, qty=2, DrugName=drugName, grNo=grNO)
AC.logout()
AC.closeBrowser()

