import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleDispensary as LD
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
AC.applicationSelection()
AC.openBrowser()
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
paymentMode = 'Cash'
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
HospitalNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
AC.logout()
#############
AC.login(phuserid, phuserpwd)
LD.activatePharmacyCounter()
pInvoiceNo = LD.createDispensarySale(HospitalNo, qty=1, drugName=drugSinex, paymentmode=paymentMode)
LD.returnPharmacyInvoice(pInvoiceNo, qty=1, returnremark="Wrong entry")
AC.logout()
AC.closeBrowser()
