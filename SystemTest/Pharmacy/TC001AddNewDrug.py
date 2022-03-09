'''
Objective:
To test below check points:
1. Add new drug item in pharmacy.
2. Verify added new drug item.
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
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
###
drugGeneric = GSV.drug1GenericName
dispensaryName = GSV.dispensaryName1
########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(danpheEMR=EMR, dispensaryName=dispensaryName)
LP.addPharmacyItem(danpheEMR=EMR, genericName=drugGeneric)
LP.verifyPharmacyItem(danpheEMR=EMR)
AC.logout()
AC.closeBrowser()
