import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT
import Library.LibModuleMedicalRecords as LMR
import Library.LibModuleMedicalRecordsReports as LMRR
import time

# front desk user login
mrUserId = GSV.MRUserID
mrUserPwd = GSV.MRUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID

EMR = AC.openBrowser()
AC.login(mrUserId, mrUserPwd)
LMRR.getInpatientMorbidityReport(EMR)
LMRR.storeInpatientMorbidityReport(EMR)

LMR.addMRwithDischargeTypeDeath(EMR, HospitalNo=HospitalNo)
LMRR.getInpatientMorbidityReport(EMR)
LMRR.verifyInpatientMorbidityReport(EMR)

AC.logout()
AC.closeBrowser()
