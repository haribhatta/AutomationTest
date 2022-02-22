from Library import ApplicationConfiguration as AC
from Library import LibModuleBilling as LB
from Library import LibModuleADT as ADT
from Library import LibModuleAppointment as LA
from Library import GlobalShareVariables as GSV
from Library import LibModuleBillingReports as LBR
import Library.LibModuleSettings as LS

# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
Doctor1 = GSV.doctorGyno
Department1 = GSV.departmentGyno
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=Department1, doctor=Doctor1, priceCategoryType=priceCategoryType).HospitalNo
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, deposit=0, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
LBR.verifyTotalAdmittedPatients(EMR, HospitalNo)
AC.logout()
AC.closeBrowser()
