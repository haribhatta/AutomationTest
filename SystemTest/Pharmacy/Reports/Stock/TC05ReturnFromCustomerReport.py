'''
Scripted by: Hari
Objective:
To test Pharmacy> Return From Customer Report with below check points:
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
# pharmacy user login
phuserid = GSV.pharmacyUserID
phuserpwd = GSV.pharmacyUserPwD
drug1Name = GSV.drug1BrandName
drug1Rate = GSV.drug1Rate
totalAmount = drug1Rate * 1
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
EMR = AC.openBrowser()
AC.login(userid=billingId, pwd=billingPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
AC.logout()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
###Pharmacy Cash Sale
pInvoiceNo = LD.createDispensarySale(EMR, HospitalNo, qty=1, drugName=drug1Name, paymentmode='Cash')
LPR.getPharmacyReturnFromCustomerReport(danpheEMR=EMR, invoiceNo=pInvoiceNo)
LPR.prePharmacyReturnFromCustomerReport()
### Pharmacy Cash Return
LD.returnDispensaryInvoice(EMR, pInvoiceNo, qty=1, returnremark="Wrong entry")
LPR.getPharmacyReturnFromCustomerReport(danpheEMR=EMR, invoiceNo=pInvoiceNo)
LPR.verifyPharmacyReturnFromCustomerReport(danpheEMR=EMR, invoiceNo=pInvoiceNo, cashReturn=totalAmount, creditReturn=0)
### Pharmacy Credit Sale
pInvoiceNo1 = LD.createDispensarySale(EMR, HospitalNo, qty=1, drugName=drug1Name, paymentmode='Credit')
LPR.prePharmacyReturnFromCustomerReport()
### Pharmacy Credit Sale Return
LD.returnDispensaryInvoice(EMR, pInvoiceNo1, qty=1, returnremark="Wrong entry")
LPR.getPharmacyReturnFromCustomerReport(danpheEMR=EMR, invoiceNo=pInvoiceNo1)
LPR.verifyPharmacyReturnFromCustomerReport(danpheEMR=EMR, invoiceNo=pInvoiceNo1, cashReturn=0, creditReturn=totalAmount)
AC.logout()
AC.closeBrowser()
