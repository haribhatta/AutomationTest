import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD

EMR = AC.openBrowser()
#############
## pharmacy user login
phuserid = GSV.pharmacyUserID
phuserpwd = GSV.pharmacyUserPwD
drugSinex = GSV.drugSinexName

paymentMode = 'Credit'
AC.login(phuserid, phuserpwd)
LD.activateDispensaryCounter(danpheEMR=EMR, dispensaryName=GSV.dispensaryName1)
LD.createDispensarySaleRegisterOutdoorPatient(danpheEMR=EMR, HospitalNo=1, qty=1, drugName=GSV.drug1BrandName,paymentmode=paymentMode)
AC.logout()
AC.closeBrowser()
