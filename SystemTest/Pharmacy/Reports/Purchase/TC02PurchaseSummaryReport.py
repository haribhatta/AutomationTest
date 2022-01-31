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
LMPR.getPurchaseSummaryReport(EMR)
LMPR.prePurchaseSummaryReport()
LP.createPharmacyGoodsReceipt(EMR, 2, DrugName=drugname, grPrice=5)
LP.verifyPharmacyGoodsReceipt(EMR, DrugName=GSV.drug1BrandName)
LP.cancelPharmacyGoodsReceipt(EMR)
LP.closePopupApplication(EMR)
LMPR.getPurchaseSummaryReport(EMR)
LMPR.verifypurchasesummary()
AC.logout()
AC.closeBrowser()

# Test script is Not Passed for LPH due to Cancel Good Receipt is unable to click
