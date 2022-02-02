import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleRadiology as LR

EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
radioTestUSG = GSV.USG
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(EMR, 0, 'Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("hospitalNo", HospitalNo)
#LP.patientRegistration()
LB.createUSGinvoice(EMR, HospitalNo=HospitalNo, USGtest=radioTestUSG)
AC.logout()
######## Radiology user login
radioUserId = GSV.adminUserID
radioUserPwd = GSV.radioUserPwD
AC.login(radioUserId, radioUserPwd)
######## Radiology Report generation
LR.doRadioScan(EMR, HospitalNo=HospitalNo)
AC.logout()
AC.closeBrowser()
