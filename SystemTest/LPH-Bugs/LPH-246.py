# ADT -> failed to admit the patient.

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LS
import Library.LibModulePatientPortal as LPP
import Library.LibModuleBilling as LB
import Library.LibModuleADT as LADT

adminId = GSV.adminUserID
adminPwd = GSV.adminUserPwD

deposit = 0

EMR = AC.openBrowser()
AC.login(adminId, adminPwd)
HospitalNo = LPP.patientRegistration()
LB.counteractivation(EMR)
LADT.admitDisTrans(danpheEMR=EMR, admit=1, trasfer=0, discharge=0, HospitalNo=HospitalNo, deposit=0, doctor=GSV.doctorGyno, department=GSV.departmentGyno)
AC.logout()
AC.closeBrowser()
print("patient has been add successfully")