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

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
paymentmode = "CREDIT"
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode=paymentmode, department=GSV.departmentGyno, doctor=GSV.doctorGyno).HospitalNo
AC.logout()

AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
InvoiceNo = LP.createPharmacyInvoiceTC(danpheEMR=EMR, HospitalNo=HospitalNo, drugname=drugname, qty=quantity, paymentmode=paymentmode)
#RPI.verifyPharmacyInvoice3(drugname, quantity, rate)
LD.returnPharmacyInvoice(danpheEMR=EMR, pInvoiceNo=InvoiceNo, qty=quantity, returnremark=returnremark)
LD.verifyReturnPharmacyInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, paymentmode=paymentmode, returnRemark=returnremark)
AC.logout()
AC.closeBrowser()
# This has open bug: EMR-2630
