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

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName
# front desk user login
billingId = GSV.foUserID
billingPwd = GSV.foUserPwD

drugname = GSV.drug1BrandName
print("drugname:", drugname)
qty = 1
rate = GSV.drug1Rate
amount = qty*rate
totalamount = amount
remark = "This is test return."
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
# To get random patient information
AC.login(userid=billingId, pwd=billingPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
AC.logout()
# Start of User collection report
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
AppName = GSV.appName
print("AppName", AppName)
######## Create anonymous pharmacy sale
LD.createDispensarySaleRandomPatient(danpheEMR=EMR, drugname=drugname, qty=qty, paymentmode='Cash')
LPR.getPharmacyUserCollectionReport(danpheEMR=EMR, user=pharmacyUserName)
LP.getPharmacyStockDetail(danpheEMR=EMR, drugname=drugname)
######## Create pharmacy cash sale
pInvoiceNo = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, drugName=drugname, qty=qty, paymentmode='Cash')
LPR.preSystemPharmacyUserCollectionReport()
LPR.getPharmacyUserCollectionReport(danpheEMR=EMR, user=pharmacyUserName)
LPR.verifySystemPharmacyUserCollectionReport(cash=totalamount, cashreturn=0, credit=0, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
######## Return pharmacy case sale
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo, qty=qty, returnremark="Test")
LPR.preSystemPharmacyUserCollectionReport()
LPR.getPharmacyUserCollectionReport(danpheEMR=EMR, user=pharmacyUserName)
LPR.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=totalamount, credit=0, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
######## Create pharmacy credit sale
if AppName != 'LPH': # Credit sale is not applicable in LPH ( they only use insurance credit without need of settlement)
    pInvoiceNo1 = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=qty,drugName=drugname, paymentmode='Credit')
    LPR.preSystemPharmacyUserCollectionReport()
    LPR.getPharmacyUserCollectionReport(EMR, pharmacyUserName)
    LPR.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=amount, creditreturn=0, creditsettlement=0,
                                                 discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
    ######## Return pharmacy credit sale
    LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo1, qty=qty, returnremark="Test")
    LPR.preSystemPharmacyUserCollectionReport()
    LPR.getPharmacyUserCollectionReport(EMR, pharmacyUserName)
    LPR.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=amount, creditsettlement=0,
                                                 discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
    ######## Create pharmacy credit sale
    pInvoiceNo2 = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=qty,drugName=drugname, paymentmode='Credit')
    print("pInvoiceNo2:", pInvoiceNo2)
    LPR.preSystemPharmacyUserCollectionReport()
    LPR.getPharmacyUserCollectionReport(EMR, pharmacyUserName)
    LPR.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=amount, creditreturn=0, creditsettlement=0,
                                                 discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
    ######## Pharmacy Credit Sale Settlement
    LD.settleDispensaryCreditInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, InvoiceNo=pInvoiceNo2)
    LPR.preSystemPharmacyUserCollectionReport()
    LPR.getPharmacyUserCollectionReport(EMR, pharmacyUserName)
    LPR.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=0, creditsettlement=amount,
                                                 discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)

AC.logout()
AC.closeBrowser()

# Test script is failling with bug: EMR-2764.
