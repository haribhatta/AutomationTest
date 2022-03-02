'''
Objective:
To test below checkpoints:
1. Transaction Report Happy Path.
a. Consultation Charge.
b. OPB billing Charge.
c. IPD billing Charge (Major Operation Item + RoundUp charge).

'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleIncentive as LI
import Library.LibModuleAppointment as LA
# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
###
departmentGynae=GSV.departmentGyno
doctorGynae = GSV.doctorGyno
###
'''
(Magh-18:2078) Check Point or if needed need to create script
### EMR-4729:
'''
###
itemprice = GSV.opdRate
discountScheme = GSV.discountSchemeName
### getting Incentive % from Setting
#incentive % = 60%
###
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LB.counteractivation(EMR)
###Pre-Condition:
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType="Normal").HospitalNo
LI.synchBilingIncentive(EMR)
###Read Transaction Report
LI.getIncentiveTransactionReport(danpheEMR=EMR, doctorName=doctorGynae)
LI.preIncentiveTransactionReport()
###Consultation Charge
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType="Normal").HospitalNo
LI.synchBilingIncentive(EMR)
LI.getIncentiveTransactionReport(danpheEMR=EMR, doctorName=doctorGynae)
LI.verifyIncentiveTransactionReport(cash=itemprice, credit=0)
###################This test script is incomplete due to Bug-ID:EMR-4917
###b. OPB billing Charge.


###c. IPD billing Charge (Major Operation Item + RoundUp charge).
AC.logout()
AC.closeBrowser()

### EMR-4797: bug is blocking this script execution.: Closed

