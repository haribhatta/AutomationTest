from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

quantity = 5
drug = GSV.Sinex

oess = A()
oess.openBrowser()
oess.login(pharmacyUserId, pharmacyUserPwd)
oess.activatePharmacyCounter()
oess.getPharmacyOpeningEndingStockSummaryReport(drugname=drug)
oess.getRandomPatient()
oess.createPharmacyInvoiceRandomPatient(drugname=drug, qty=quantity, paymentmode='Cash')
oess.preSystemPharmacyOpeningEndingStockSummaryReport()
oess.verifyPharmacyOpeningEndingStockSummaryReport(quantity)
oess.logout()
oess.closeBrowser()
# Test script has open bug: EMR-2768