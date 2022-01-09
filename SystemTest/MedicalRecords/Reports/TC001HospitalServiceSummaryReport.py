import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT
import Library.LibModuleMedicalRecordsReports as LMRR
import time

# front desk user login
mrUserId = GSV.MRUserID
mrUserPwd = GSV.MRUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID

EMR = AC.openBrowser()
AC.login(mrUserId, mrUserPwd)
LMRR.getHospitalServiceSummaryReport(EMR)

time.sleep(2)
AC.logout()
AC.closeBrowser()
