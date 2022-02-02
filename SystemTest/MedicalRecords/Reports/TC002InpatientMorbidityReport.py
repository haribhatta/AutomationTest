import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleMedicalRecords as LMR
import Library.LibModuleMedicalRecordsReports as LMRR
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleADT as ADT
import time

# front desk user login
mrUserId = GSV.adminUserID
mrUserPwd = GSV.MRUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"

EMR = AC.openBrowser()
AC.login(mrUserId, mrUserPwd)
LMRR.getInpatientMorbidityReport(EMR)
LMRR.storeInpatientMorbidityReport(EMR)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
ADT.admitDisTrans(EMR, 1, 0, 0, HospitalNo, 0, doctorGynae, departmentGynae)
ADT.admitDisTrans(EMR, 0, 1, 0, HospitalNo, 0, doctorGynae, departmentGynae)
LMR.addMRwithDischargeTypeDeath(EMR, HospitalNo=HospitalNo)
LMRR.getInpatientMorbidityReport(EMR)
LMRR.verifyInpatientMorbidityReport(EMR)

time.sleep(2)
AC.logout()
AC.closeBrowser()
