'''
Scripted by: Hari P. Bhatta
Objective:
To test Pharmacy> Bill-wise Sales report with below check points:
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
HospitalNo, InvoiceNo, discountPercentage  = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
AC.logout()
# Start of User collection report
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
LPR.getSystemPharmacyBillWiseSalesReport(danpheEMR=EMR)
LPR.preSystemPharmacyBillWiseSalesReport()
######## Create pharmacy cash sale
pInvoiceNo = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, drugName=drugName, qty=qty, paymentmode='Cash')
LPR.getSystemPharmacyBillWiseSalesReport(danpheEMR=EMR)
LPR.verifySystemPharmacyBillWiseSalesReport(danpheEMR=EMR, invoiceNo=pInvoiceNo, cash=totalAmount, cashReturn=0, credit=0, creditReturn=0, totalAmount=totalAmount, discountAmount=0)
######## Return pharmacy cash sale  :
'''
*Note: Return Sales are not included in this report. ==> hence commenting return part.
LPR.preSystemPharmacyBillWiseSalesReport()
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo, qty=qty, returnremark="Test")
LPR.getSystemPharmacyBillWiseSalesReport(danpheEMR=EMR)
LPR.verifySystemPharmacyBillWiseSalesReport(danpheEMR=EMR, invoiceNo=pInvoiceNo, cash=0, cashReturn=totalAmount, credit=0, creditReturn=0, totalAmount=totalAmount, discountAmount=0) ### Open bug in Jira: EMR-4776
'''
######## Create pharmacy credit sale
LPR.preSystemPharmacyBillWiseSalesReport()
pInvoiceNo1 = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=qty,drugName=drugName, paymentmode='Credit')
LPR.getSystemPharmacyBillWiseSalesReport(danpheEMR=EMR)
LPR.verifySystemPharmacyBillWiseSalesReport(danpheEMR=EMR, invoiceNo=pInvoiceNo, cash=0, cashReturn=0, credit=totalAmount, creditReturn=0, totalAmount=totalAmount, discountAmount=0)
######## Return pharmacy credit sale
'''
*Note: Return Sales are not included in this report. ==> hence commenting return part.
LPR.preSystemPharmacyBillWiseSalesReport()
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo1, qty=qty, returnremark="Test")
LPR.getSystemPharmacyBillWiseSalesReport(danpheEMR=EMR)
LPR.verifySystemPharmacyBillWiseSalesReport(danpheEMR=EMR, invoiceNo=pInvoiceNo, cash=0, cashReturn=0, credit=0, creditReturn=totalAmount, totalAmount=totalAmount, discountAmount=0)
'''
AC.logout()
AC.closeBrowser()