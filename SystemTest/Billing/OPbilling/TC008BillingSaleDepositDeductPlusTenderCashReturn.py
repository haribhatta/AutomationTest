#Objective: To cover the OPD bill amount deduction from deposit balance where deposit balance < Total Amount and cash return from tender.
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA

#AC.applicationSelection()
EMR = AC.openBrowser()
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
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
LB.opDeposit(EMR, HospitalNo, GSV.deposit)
LB.opDepositDbilingTenderCashReturn(EMR, HospitalNo, GSV.deposit, GSV.TFT)
AC.logout()
AC.closeBrowser()


