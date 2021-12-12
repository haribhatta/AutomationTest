import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LPP
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

deposit = 1000

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LPP.patientRegistration()
LB.opDeposit(danpheEMR=EMR, HospitalNo=HospitalNo, amount=deposit)
LBR.verifyDepositBalanceReport(danpheEMR=EMR, HospitalNo=HospitalNo, deposit=deposit)
AC.logout()
AC.closeBrowser()