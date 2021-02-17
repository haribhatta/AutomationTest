from TestActionLibrary import A

# front desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

quantity = 5
drug = 'SINEX TAB'

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