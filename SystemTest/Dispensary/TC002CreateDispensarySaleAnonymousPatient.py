import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleDispensary as LD

AC.applicationSelection()
AC.openBrowser()
#############
# pharmacy user login
phuserid = GSV.pharmacyUserID
phuserpwd = GSV.pharmacyUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
drugSinex = GSV.drugSinexName

paymentMode = 'Cash'
#############
AC.login(phuserid, phuserpwd)
LD.activatePharmacyCounter()
LD.createDispensarySaleRandomPatient(qty=1, drugname=drugSinex, paymentmode=paymentMode)
AC.logout()
AC.closeBrowser()
