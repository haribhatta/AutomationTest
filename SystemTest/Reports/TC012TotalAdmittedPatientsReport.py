import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleADT as LADT
import Library.LibModuleBillingReports as LBR

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
Doctor1 = GSV.doctorGyno
Department1 = GSV.departmentGyno
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=Department1, doctor=Doctor1, priceCategoryType=priceCategoryType).HospitalNo
LADT.admitDisTrans(danpheEMR=EMR, admit=1, trasfer=0, discharge=0,deposit=0,HospitalNo=HospitalNo, doctor=Doctor1, department=Department1)
LBR.verifyTotalAdmittedPatients(EMR, HospitalNo)
AC.logout()
AC.closeBrowser()
