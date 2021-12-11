'''
import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleLaboratory as LL
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleLaboratory as LL
#############
#AC.applicationSelection()
EMR = AC.openBrowser()
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
LB.counteractivation(EMR)
hospitalNo = LA.patientquickentry(EMR, 0, 'Cash',department=departmentGynae, doctor=doctorGynae).HospitalNo
print("hospitalNo", hospitalNo)
#oblx.verifyopdinvoice(deposit=0, billamt=500)
LB.createLabInvoice(EMR, hospitalNo, labTestTFT, radioTestUSG)
#oblx.verifylabxrayinvoice()
#############
AC.logout()
AC.login(labUserId, labUserPwd)
LL.collectLabSample(EMR, hospitalNo, labTestTFT)
LL.addLabResult(EMR)
LL.verifyLabReport(EMR, hospitalNo)
LL.printLabReport(EMR, hospitalNo, "2.23", "15.0", "4.05")
AC.logout()
AC.closeBrowser()