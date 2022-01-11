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
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
AC.login(foUserId, foUserPwd)
############
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(EMR, 0, 'Cash',department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("hospitalNo", HospitalNo)
#oblx.verifyopdinvoice(deposit=0, billamt=500)
LB.createLabInvoice(EMR, HospitalNo, labTestTFT)
#oblx.verifylabxrayinvoice()
#############
AC.logout()
AC.login(labUserId, labUserPwd)
LL.collectLabSample(EMR, HospitalNo, labTestTFT)
LL.addLabResult(EMR)
LL.verifyLabReport(EMR, HospitalNo)
LL.printLabReport(EMR, HospitalNo, "2.23", "15.0", "4.05")
AC.logout()
AC.closeBrowser()