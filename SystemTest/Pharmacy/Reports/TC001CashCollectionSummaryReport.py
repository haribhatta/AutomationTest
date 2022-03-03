'''
Objective:
To test Cash Collection Summary report in pharmacy with below check scenarios:
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
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacyReports as LPR
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD
import Library.LibModulePatientPortal as LPP

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

drugname = GSV.drug1BrandName
qty = 1
rate = GSV.drug1Rate
amount = qty*rate
totalamount = round(amount)
remark = "This is test return."
drug1Name = GSV.drug1BrandName

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName)
LPR.getPharmacyCashCollectionSummary(EMR, pharmacyUserId)
LP.getStockDetail(danpheEMR=EMR, drugname=drugname)
HospitalNo = LPP.getRandomPatient(EMR)
### Pharmacy Cash Sale
InvoiceNo = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=1, drugName=drug1Name, paymentmode='Cash')
LPR.preSystemPharmacyCashCollectionSummary()
LPR.getPharmacyCashCollectionSummary(EMR, pharmacyUserId)
LPR.verifyPharmacyCashCollectionSummary(cash=totalamount, cashreturn=0, credit=0, creditreturn=0, deposit=0, depositreturn=0, discount=0)
### Pharmacy Cash Sale Return
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=InvoiceNo, qty=qty, returnremark=remark)
LPR.preSystemPharmacyCashCollectionSummary()
LPR.getPharmacyCashCollectionSummary(EMR, pharmacyUserId)
LPR.verifyPharmacyCashCollectionSummary(cash=0, cashreturn=amount, credit=0, creditreturn=0, deposit=0, depositreturn=0, discount=0)
### Pharmacy Credit Sale
InvoiceNo1 = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=1, drugName=drug1Name, paymentmode='Credit')
LPR.preSystemPharmacyCashCollectionSummary()
LPR.getPharmacyCashCollectionSummary(EMR, pharmacyUserId)
LPR.verifyPharmacyCashCollectionSummary(cash=0, cashreturn=0, credit=totalamount, creditreturn=0, deposit=0, depositreturn=0, discount=0)
### Pharmacy Credit Sale Return
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=InvoiceNo1, qty=qty, returnremark=remark)
LPR.preSystemPharmacyCashCollectionSummary()
LPR.getPharmacyCashCollectionSummary(EMR, pharmacyUserId)
LPR.verifyPharmacyCashCollectionSummary(cash=0, cashreturn=0, credit=0, creditreturn=totalamount, deposit=0, depositreturn=0, discount=0)
AC.logout()
AC.closeBrowser()