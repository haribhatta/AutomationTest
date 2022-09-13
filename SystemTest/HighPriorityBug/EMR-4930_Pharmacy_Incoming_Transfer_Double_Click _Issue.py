import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP

#import Library.LibModuleBilling as LB
# pharmacy desk user login as transfer is not access to user so change to admin user
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
###
drug = GSV.drug1BrandName
transferqty = 1
dispensaryName = GSV.dispensaryName1
remarks = "Transfer Quantity is 1"
###
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, dispensaryName=dispensaryName)
LD.transferMainDispensary2MainStore(danpheEMR=EMR, drugname=drug, qty=transferqty)
LP.transferReceive(danpheEMR=EMR, drugname=drug, qty=transferqty, remarks=remarks)
AC.logout()
AC.closeBrowser()
