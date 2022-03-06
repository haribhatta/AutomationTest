# scripting blocked due to bug: EMR-2587
'''
Objective:
To test Pharmacy> Narcotic Drug Daily Sales Report with below check points:
Precondition: Drug-Narcotic
1. Cash Sale
2. Cash Sale Return
3. Credit Sale
4. Credit Settlement
5. Credit Sale Return
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

drugName = GSV.drug1NarcoticName
drugRate = GSV.drug1NarcoticRate
qty = 1
totalAmount = qty*drugRate
totalAmount = int(totalAmount)
print("Total Amount of narcotic sale is", totalAmount)
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
# Start of User collection report
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
######## Create pharmacy cash sale
pInvoiceNo = LD.createNarcoticDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, drugName=drugName, qty=qty, paymentmode='Cash')
LPR.verifySystemPharmacyNarcoticDailySalesReport(danpheEMR=EMR, invoiceNo=pInvoiceNo, totalAmount=totalAmount)
######## Return pharmacy cash sale
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo, qty=qty, returnremark="Test")
LPR.verifySystemPharmacyNarcoticDailySalesReport(danpheEMR=EMR, invoiceNo=pInvoiceNo, totalAmount=totalAmount) ### Open bug in Jira: EMR-4776

######## Create pharmacy credit sale
pInvoiceNo1 = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=qty, drugName=drugName, paymentmode='Credit')
LPR.verifySystemPharmacyNarcoticDailySalesReport(danpheEMR=EMR, invoiceNo=pInvoiceNo1, totalAmount=totalAmount)

######## Return pharmacy credit sale
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo1, qty=qty, returnremark="Test")
LPR.verifySystemPharmacyNarcoticDailySalesReport(danpheEMR=EMR, invoiceNo=pInvoiceNo1, totalAmount=totalAmount)

AC.logout()
AC.closeBrowser()

# Test script is failling with bug: EMR-2764.
