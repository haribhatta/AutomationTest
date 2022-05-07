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
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, 0, 'Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
print("hospitalNo", HospitalNo)
LB.createLabInvoice(EMR, HospitalNo, labTestTFT)
LL.collectLabSample(EMR, HospitalNo, labTestTFT)
patientName = LL.seeWorkListFIFO(EMR)
HospitalNo1, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, 0, 'Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LB.createLabInvoice(EMR, HospitalNo1, labTestTFT)
LL.collectLabSample(EMR, HospitalNo1, labTestTFT)
LL.verifyFIFOInWorklist(EMR, patientName=patientName)
AC.logout()
AC.closeBrowser()

