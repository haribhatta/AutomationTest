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

drugname = GSV.Testdrug
drugGeneric = GSV.drug1GenericName

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(danpheEMR=EMR, dispensaryName=GSV.dispensaryName)
LP.addPharmacyItem(danpheEMR=EMR, genericName=drugGeneric)
LP.verifyPharmacyItem(danpheEMR=EMR)
AC.logout()
AC.closeBrowser()

print("This tc is incomplete")
