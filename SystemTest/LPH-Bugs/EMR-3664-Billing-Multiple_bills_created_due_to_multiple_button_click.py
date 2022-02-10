import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA

AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
labTestTFT = GSV.TFT
radioTestUSG = GSV.USG
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
hospitalNo = LA.patientquickentry(0, 'Cash',department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
print("hospitalNo", hospitalNo)
InvoiceNo=LB.multiplebillingclick(hospitalNo,labTestTFT, radioTestUSG)
LB.verifymultipleclickbilling(InvoiceNo)
AC.logout()
AC.closeBrowser()

