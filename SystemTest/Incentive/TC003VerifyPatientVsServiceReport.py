'''
Objective:
To test below checkpoints:
1.

'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleIncentive as LI
import Library.LibModuleAppointment as LA

# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
OpdRate = GSV.opdRate
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
departmentGyno = GSV.departmentGyno
doctorGyno = GSV.doctorGyno
########
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LI.getIncentivePatientVsServiceReport(EMR, doctorName=doctorGyno)
LI.preIncentivePatientVsServiceReport()
LB.counteractivation(EMR)
LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGyno, doctor=doctorGyno, priceCategoryType=priceCategoryType)
LI.synchBilingIncentive(danpheEMR=EMR)
LI.getIncentivePatientVsServiceReport(danpheEMR=EMR, doctorName=doctorGyno)
LI.verifyIncentivePatientVsServiceReport(self=0, amount=OpdRate)
AC.logout()
AC.closeBrowser()
