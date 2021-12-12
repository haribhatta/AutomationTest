'''
Objective:
To test Pharmacy> Opening and Ending Stock Summary Report with below check points:
1. Get Opening&Ending Stock Summary
2. Dispatch Pharmacy Stock
3. Verify Opening&Ending Stock Summary
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacyReports as LPR
import Library.LibModulePatientPortal as LPP

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

quantity = 5
drug = GSV.drug1BrandName

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
LPR.getPharmacyOpeningEndingStockSummaryReport(danpheEMR=EMR, drugname=drug)
LPP.getRandomPatient()
LD.createPharmacyInvoiceRandomPatient(drugname=drug, qty=quantity, paymentmode='Cash')
LPR.preSystemPharmacyOpeningEndingStockSummaryReport()
LPR.verifyPharmacyOpeningEndingStockSummaryReport(EMR, quantity)
AC.logout()
AC.closeBrowser()
# Test script has open bug: EMR-2768