import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD

EMR = AC.openBrowser()
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
LD.activateDispensaryCounter(danpheEMR=EMR, dispensaryName=GSV.dispensaryName)
LD.createDispensarySaleRandomPatient(danpheEMR=EMR, qty=1, drugname=drugSinex, paymentmode=paymentMode)
AC.logout()
AC.closeBrowser()
