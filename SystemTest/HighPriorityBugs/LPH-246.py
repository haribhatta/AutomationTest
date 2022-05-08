# ADT -> failed to admit the patient.

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModulePatientPortal as LPP
import Library.LibModuleBilling as LB
import Library.LibModuleADT as LADT
import Library.LibModuleSettings as LS
########
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
########
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
########
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
AC.logout()
AC.login(GSV.foUserID, GSV.foUserPwD)
########
HospitalNo = LPP.patientRegistration(EMR)
LB.counteractivation(EMR)
LADT.admitDisTrans(danpheEMR=EMR, admit=1, trasfer=0, discharge=0, HospitalNo=HospitalNo, deposit=0, doctor=GSV.doctorGyno, department=GSV.departmentGyno, admittingDoctorMandatory=isDoctorMandatory)
AC.logout()
AC.closeBrowser()
print("patient has been add successfully")