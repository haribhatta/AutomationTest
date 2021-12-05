'''
Objective:
To cover the OPD bill amount deduction from deposit balance where deposit balance < Total Amount.
'''
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
HospitalNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
LB.opDeposit(HospitalNo=HospitalNo, amount=GSV.deposit)
LB.opDepositDbiling(HospitalNo=HospitalNo, deposit=GSV.deposit, testname=GSV.USG)
#LB.verifyopdinvoice(deposit=GSV.deposit, billamt=GSV.usgRate)
AC.logout()
AC.closeBrowser()


