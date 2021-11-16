import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleLaboratory as LL
#############
AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
#############
# lab user login
labUserId = GSV.labUserID
labUserPwd = GSV.labUserPwD
labTestTFT = GSV.TFT
radioTestUSG = GSV.USG
#############
AC.login(foUserId, foUserPwd)
############
LB.counteractivation()
hospitalNo = LA.patientquickentry(0, 'Cash',department=departmentGynae, doctor=doctorGynae)
print("hospitalNo", hospitalNo)
#oblx.verifyopdinvoice(deposit=0, billamt=500)
LB.createlabxrayinvoice(hospitalNo, labTestTFT, radioTestUSG)
#oblx.verifylabxrayinvoice()
#############
AC.logout()
AC.login(labUserId, labUserPwd)
LL.collectLabSample(hospitalNo, labTestTFT)
LL.addLabResult()
LL.verifyLabReport(hospitalNo)
LL.printLabReport(hospitalNo, "2.23", "15.0", "4.05")
AC.logout()
AC.closeBrowser()