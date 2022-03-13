import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleMedicalRecords as LMR
import Library.LibModuleMedicalRecordsReports as LMRR
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleADT as ADT
import time
import Library.LibModuleSettings as LS
# front desk user login
mrUserId = GSV.adminUserID
mrUserPwd = GSV.MRUserPwD
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
opdAmt = GSV.opdRate
user = GSV.foUserID
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
########
EMR = AC.openBrowser()
########
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
AC.logout()
AC.login(mrUserId, mrUserPwd)
########
LMRR.getInpatientMorbidityReport(EMR)
LMRR.storeInpatientMorbidityReport(EMR)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType)
ADT.admitDisTrans(EMR, 1, 0, 0, HospitalNo, 0, doctorGynae, departmentGynae, isDoctorMandatory)
ADT.admitDisTrans(EMR, 0, 1, 0, HospitalNo, 0, doctorGynae, departmentGynae, isDoctorMandatory)
LMR.addMRwithDischargeTypeDeath(EMR, HospitalNo=HospitalNo)
LMRR.getInpatientMorbidityReport(EMR)
LMRR.verifyInpatientMorbidityReport(EMR)

time.sleep(2)
AC.logout()
AC.closeBrowser()
