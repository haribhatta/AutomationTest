'''
Objective:
To test below check points:
1. Create pharmacy deposit.
2. Verify pharmacy deposit slip.
3. Return pharmacy deposit.
4. Verify pharmacy deposit return.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LPP

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
HospitalNo = LPP.patientRegistration(EMR)
AC.logout()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
LP.addPharmacyDeposit(danpheEMR=EMR, HospitalNo=HospitalNo, deposit=1000)
LPR.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=0, creditreturn=0, deposit=1000, depositreturn=0, provisional=0, provisionacancel=0)
LP.returnPharmacyDeposit(danpheEMR=EMR, HospitalNo=HospitalNo, depositreturn=1000)
AC.logout()
AC.closeBrowser()
