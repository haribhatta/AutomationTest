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

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

# front desk user login
billingId = GSV.foUserID
billingPwd = GSV.foUserPwD

drugname = GSV.drug1BrandName
qty = 1
paymode = 'Cash'
rate = GSV.drug1Rate
amount = qty*rate
totalamount = amount
remark = "This is test return."

EMR = AC.openBrowser()
# To get random patient information
AC.login(userid=billingId, pwd=billingPwd)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno).HospitalNo
AC.logout()
# Start of User collection report
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
######## Create anonymous pharmacy sale
LP.createPharmacyInvoiceAnonymous(danpheEMR=EMR, drugname=drugname, qty=qty, paymentmode=paymode)
LPR.getPharmacyUserCollectionReport(danpheEMR=EMR, user=pharmacyUserId)
LP.getStockDetail(danpheEMR=EMR, drugname=drugname)
######## Create pharmacy cash sale
pInvoiceNo = LP.createPharmacyInvoiceTC(EMR, HospitalNo, drugname, qty, paymode)
LPR.preSystemPharmacyUserCollectionReport()
LPR.getPharmacyUserCollectionReport(danpheEMR=EMR, user=pharmacyUserId)
LPR.verifySystemPharmacyUserCollectionReport(cash=totalamount, cashreturn=0, credit=0, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
######## Return pharmacy case sale
LD.returnPharmacyInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo, qty=qty, returnremark="Test")
LPR.preSystemPharmacyUserCollectionReport()
LPR.getPharmacyUserCollectionReport(danpheEMR=EMR, user=pharmacyUserId)
LPR.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=totalamount, credit=0, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
######## Create pharmacy credit sale
pInvoiceNo1 = LP.createPharmacyInvoiceTC(danpheEMR=EMR, HospitalNo=HospitalNo, drugname=drugname, qty=qty, paymentmode='Credit')
LPR.preSystemPharmacyUserCollectionReport()
LPR.getPharmacyUserCollectionReport(EMR, pharmacyUserId)
LPR.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=amount, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
######## Return pharmacy credit sale
LD.returnPharmacyInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo1, qty=qty, returnremark="Test")
LPR.preSystemPharmacyUserCollectionReport()
LPR.getPharmacyUserCollectionReport(EMR, pharmacyUserId)
LPR.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=amount, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
AC.logout()
AC.closeBrowser()

# Test script is failling with bug: EMR-2764.
