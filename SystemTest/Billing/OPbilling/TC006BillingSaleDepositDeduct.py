'''
Objective:
To cover the OPD bill amount deduction from deposit balance where deposit balance > Total Amount.
'''
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
priceCategoryType = "Normal"
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LB.opDeposit(EMR, HospitalNo=HospitalNo, amount=GSV.deposit)
LB.opDepositDbiling(EMR, HospitalNo=HospitalNo, deposit=GSV.deposit, testname=GSV.TFT)
AC.logout()
AC.closeBrowser()
