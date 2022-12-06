import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
#import Library.LibModuleSettings as LS
import Library.LibModuleMedicalRecords as LMR
#############


# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD

departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName

EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)

LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
print("Status:Passed - > Appointment created")
LMR.OutpatientList(danpheEMR=EMR, HospitalNo=HospitalNo, DoctorName=doctorGynae)
AC.logout()
AC.closeBrowser()






