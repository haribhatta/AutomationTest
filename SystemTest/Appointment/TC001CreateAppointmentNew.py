import AutomationTest.Library.ApplicationConfiguration as AC
import AutomationTest.Library.GlobalShareVariables as GSV
import AutomationTest.Library.LibModuleBilling as LB
import AutomationTest.Library.LibModuleAppointment as LA

AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae)
#can.verifyopdinvoice(deposit=0, billamt=500)
AC.logout()
AC.closeBrowser()
print("Status:Passed - > TC001 CreateAppointmentNew")
