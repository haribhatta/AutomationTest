'''
Scripted by: Alina
Objective:
To test Pharmacy> Item-wise Sales report with below check points:
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
import Library.LibModulePharmacyReports as LMPR
import Library.LibModuleBilling as LB

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName
# front desk user login
billingId = GSV.foUserID
billingPwd = GSV.foUserPwD

drugName = GSV.drug1BrandName
drugRate = GSV.drug1Rate
qty = 1
totalAmount = qty*drugRate
remark = "This is test return."
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
# To get random patient information
AC.login(userid=billingId, pwd=billingPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
AC.logout()
#Start Item Wise Sales Report
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
LMPR.getSystemPharmacyItemWiseSalesReport(danpheEMR=EMR, drugName=drugName)
LMPR.preSystemPharmacyItemWiseSalesReport()
######## Create pharmacy cash sale
pInvoiceNo = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, drugName=drugName, qty=qty, paymentmode='Cash')
LMPR.getSystemPharmacyItemWiseSalesReport(danpheEMR=EMR, drugName=drugName)
LMPR.VerifySystemPharmacyItemWiseSalesReport(danpheEMR=EMR, drugName=drugName, cash=totalAmount, credit=0, qty=qty)
######## Create pharmacy credit sale
LMPR.preSystemPharmacyItemWiseSalesReport()
pInvoiceNo1 = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=qty,drugName=drugName, paymentmode='Credit')
LMPR.getSystemPharmacyItemWiseSalesReport(danpheEMR=EMR, drugName=drugName)
LMPR.VerifySystemPharmacyItemWiseSalesReport(danpheEMR=EMR, drugName=drugName, cash=0, credit=totalAmount, qty=qty)
AC.logout()
AC.closeBrowser()

