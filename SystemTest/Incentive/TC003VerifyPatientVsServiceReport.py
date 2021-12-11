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

EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LI.getIncentivePatientVsServiceReport(EMR)
LI.preIncentivePatientVsServiceReport()
LB.counteractivation(EMR)
LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno)
LI.synchBilingIncentive()
LI.getIncentivePatientVsServiceReport(EMR)
LI.verifyIncentivePatientVsServiceReport(self=0, amount=OpdRate)
AC.logout()
AC.closeBrowser()
