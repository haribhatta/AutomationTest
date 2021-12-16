'''
Objective:
The aim of this test script is to test below check points:
1. Create pharmacy cash invoice.
2. Return pharmacy cash invoice.
3. Create pharmacy credit invoice.
4. Return pharmacy credit invoice.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
#AC.applicationSelection()
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
# pharmacy user login
phuserid = GSV.pharmacyUserID
phuserpwd = GSV.pharmacyUserPwD
drugSinex = GSV.drugSinexName
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(EMR, discountpc=0, paymentmode='cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
AC.logout()
#############
AC.login(phuserid, phuserpwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)

######## Create pharmacy cash invoice.
paymentMode = 'cash'
pInvoiceNo = LD.createDispensarySale(EMR, HospitalNo, qty=1, drugName=drugSinex, paymentmode=paymentMode)
returnRemark = "Wrong entry"
######## Retunr pharmacy cash invoice.
LD.returnPharmacyInvoice(EMR, pInvoiceNo, qty=1, returnremark=returnRemark)
LD.verifyReturnPharmacyInvoice(EMR, pInvoiceNo, paymentMode, returnRemark)

######## Create pharmacy credit invoice.
paymentMode1 = 'credit'
pInvoiceNo = LD.createDispensarySale(EMR, HospitalNo, qty=1, drugName=drugSinex, paymentmode=paymentMode1)
returnRemark = "Wrong entry"
######## Retunr pharmacy credit invoice.
LD.returnPharmacyInvoice(EMR, pInvoiceNo, qty=1, returnremark=returnRemark)
LD.verifyReturnPharmacyInvoice(EMR, pInvoiceNo, paymentMode1, returnRemark)

AC.logout()
AC.closeBrowser()
