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

departmentGynae=GSV.departmentGyno
doctorGynae = GSV.doctorGyno
###
itemprice = GSV.opdRate
discountScheme = GSV.discountSchemeName
# incentive % = 60%

EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LB.counteractivation(EMR)
LI.synchBilingIncentive(EMR)
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType="Normal").HospitalNo
LI.getIncentiveTransactionReport(danpheEMR=EMR, doctorName=doctorGynae)
LI.preIncentiveTransactionReport()
LI.synchBilingIncentive(EMR)
LI.getIncentiveTransactionReport(danpheEMR=EMR, doctorName=doctorGynae)
LI.verifyIncentiveTransactionReport(cash=itemprice, credit=0)
AC.logout()
AC.closeBrowser()

### EMR-4797: bug is blocking this script execution.
