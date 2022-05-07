'''
Objective:
To test Pharmacy> Deposit Balance report with below check points:
1. Create Deposit slip
2. Verify deposit slip
3. Return Deposit balance
4. Verify deposit return.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacyReports as LPR

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve').HospitalNo
AC.logout()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName)
LP.addPharmacyDeposit(danpheEMR=EMR, HospitalNo=HospitalNo, deposit=1000)
LPR.getPharmacyDepositBalanceReport(danpheEMR=EMR, HospitalNo=HospitalNo)
LP.addPharmacyDeposit(danpheEMR=EMR, HospitalNo=HospitalNo, deposit=1000)
LPR.verifyPharmacyDepositBalanceReport(danpheEMR=EMR, HospitalNo=HospitalNo, deposit=1000, depositreturn=0)
LPR.getPharmacyDepositBalanceReport(danpheEMR=EMR, HospitalNo=HospitalNo)
LP.returnPharmacyDeposit(danpheEMR=EMR, HospitalNo=HospitalNo, depositreturn=500)
LPR.verifyPharmacyDepositBalanceReport(danpheEMR=EMR, HospitalNo=HospitalNo, deposit=0, depositreturn=500)
AC.logout()
AC.closeBrowser()