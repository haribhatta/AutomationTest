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
import Library.LibModuleSettings as LS
#############
#AC.applicationSelection()
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
###
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
AC.login(adminUserId, adminUserPwd)
isLabReportVerify = LS.checkCoreLabReportVerify(EMR)
AC.logout()
#############
AC.login(foUserId, foUserPwd)
############
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, 0, 'Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
print("hospitalNo", HospitalNo)
#oblx.verifyopdinvoice(deposit=0, billamt=500)
LB.createLabInvoice(EMR, HospitalNo, labTestTFT)
AC.logout()
AC.login(labUserId, labUserPwd)
LL.collectLabSample(EMR, HospitalNo, labTestTFT)
LL.addLabResult(EMR)
LL.verifyLabReport(EMR, HospitalNo, isLabReportVerify)
LL.printLabReport(EMR, HospitalNo, "2.23", "15.0", "4.05")
AC.logout()
AC.closeBrowser()