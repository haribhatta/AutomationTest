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

department=GSV.departmentGyno
doctor = GSV.doctorGyno
###
paymode = "Cash"
itemprice = GSV.opdRate
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
# incentive % = 60%

EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LB.counteractivation(EMR)
LI.synchBilingIncentive(EMR)
LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymode, department=department, doctor=doctor, priceCategoryType=priceCategoryType)
LI.getIncentiveTransactionReport(danpheEMR=EMR, doctorName=doctor)
LI.preIncentiveTransactionReport()
LI.synchBilingIncentive(EMR)
LI.getIncentiveTransactionReport(danpheEMR=EMR, doctorName=doctor)
LI.verifyIncentiveTransactionReport(cash=itemprice, credit=0)
AC.logout()
AC.closeBrowser()

### EMR-4797: bug is blocking this script execution.
