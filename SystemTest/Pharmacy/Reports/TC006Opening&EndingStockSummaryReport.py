from TestActionLibrary import A

quantity = 5
drug = 'SINEX TAB'

oess = A()
oess.openBrowser()
oess.login('pharmacy1', 'pass123')
oess.activatePharmacyCounter()
oess.getPharmacyOpeningEndingStockSummaryReport(drugname=drug)
oess.getRandomPatient()
oess.createPharmacyInvoiceRandomPatient(drugname=drug, qty=quantity, paymentmode='Cash')
oess.preSystemPharmacyOpeningEndingStockSummaryReport()
oess.verifyPharmacyOpeningEndingStockSummaryReport(quantity)
oess.logout()
oess.closeBrowser()
# Test script has open bug: EMR-2768