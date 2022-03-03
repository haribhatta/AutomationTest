'''
Objective:
To test below check points:
1. Create pharmacy invoice.
2. Return pharmacy invoice.
3. Verify pharmacy invoice return.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleAppointment as LA
#import Library.LibModuleBilling as LB
import Library.LibModuleBilling as LB

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

drugname = GSV.drug1BrandName
quantity = 2
rate = GSV.drug1Rate
returnremark = "This is auto return"
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
paymentmode = "CREDIT"
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymentmode, department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).HospitalNo
AC.logout()

AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName)
InvoiceNo = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=quantity, drugName=drugname, paymentmode=paymentmode)
#RPI.verifyPharmacyInvoice3(drugname, quantity, rate)
LD.returnPharmacyInvoice(danpheEMR=EMR, pInvoiceNo=InvoiceNo, qty=quantity, returnremark=returnremark)
LD.verifyReturnPharmacyInvoice(danpheEMR=EMR, paymentmode=paymentmode, returnRemark=returnremark, InvoiceNo=InvoiceNo)
AC.logout()
AC.closeBrowser()
# This has open bug: EMR-2630
