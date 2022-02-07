'''
Objective:
To test Pharmacy> Item Wise Purchase report with below check points:

'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD
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
# Item Wise Purchase Start
LMPR.getItemWisePurchaseReport(EMR)
LMPR.preItemWisePurchaseReport()
LP.createPharmacyGoodsReceipt(EMR, supplier=supplier, qty=2, DrugName=drugname, grPrice=5)
LP.verifyPharmacyGoodsReceipt(EMR, DrugName=GSV.drug1BrandName)
LMPR.getItemWisePurchaseReport(EMR)
LMPR.verifyItemWisePurchaseReport(EMR)
AC.logout()
AC.closeBrowser()


