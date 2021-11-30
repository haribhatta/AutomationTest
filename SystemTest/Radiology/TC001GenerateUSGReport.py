import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleRadiology as LR

AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
radioTestUSG = GSV.USG
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
HospitalNo = LA.patientquickentry(0, 'Cash',department=departmentGynae, doctor=doctorGynae).HospitalNo
print("hospitalNo", HospitalNo)
LP.patientRegistration()
LB.createUSGinvoice(HospitalNo=HospitalNo, USGtest=radioTestUSG)
AC.logout()
######## Radiology user login
radioUserId = GSV.radioUserID
radioUserPwd = GSV.radioUserPwD
AC.login(radioUserId, radioUserPwd)
######## Radiology Report generation
LR.doRadioScan(HospitalNo=HospitalNo)
AC.logout()
AC.closeBrowser()
