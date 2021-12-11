import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR

#AC.applicationSelection()
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
labTestTFT = GSV.TFT
USGName = GSV.USG
USGRate = GSV.usgRate
print("radioTestUSG", USGName)
print("radioTestUSG", USGRate)
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(EMR, discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
LB.createProvisionalBill(EMR, HospitalNo, GSV.USG)  #provisional=usgprice
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0,
                            provisional= USGRate, provisionalcancel=0)
AC.logout()
AC.closeBrowser()
