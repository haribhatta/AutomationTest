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

paymode = "Cash"
itemprice = GSV.opdRate

# incentive % = 60%

EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LB.counteractivation(EMR)
LI.synchBilingIncentive()
LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode=paymode, department=GSV.departmentGyno, doctor=GSV.doctorGyno)
LI.getIncentiveTransactionReport(EMR)
LI.preIncentiveTransactionReport()
LI.synchBilingIncentive()
LI.getIncentiveTransactionReport(EMR)
LI.verifyIncentiveTransactionReport(cash=itemprice, credit=0)
AC.logout()
AC.closeBrowser()
