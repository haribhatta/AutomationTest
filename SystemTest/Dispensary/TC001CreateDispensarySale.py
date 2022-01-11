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
paymentMode = 'Cash'
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
AC.logout()
#############
AC.login(phuserid, phuserpwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
pInvoiceNo = LD.createDispensarySale(EMR, HospitalNo, qty=1, drugName=drugSinex, paymentmode=paymentMode)
LD.returnPharmacyInvoice(EMR, pInvoiceNo, qty=1, returnremark="Wrong entry")
AC.logout()
AC.closeBrowser()
