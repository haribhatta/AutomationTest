from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
OpdRate = GSV.opdRate

pvs = A()

pvs.openBrowser()
pvs.login(adminUserId, adminUserPwd)
pvs.getIncentivePatientVsServiceReport()
pvs.preIncentivePatientVsServiceReport()
pvs.counteractivation()
pvs.patientquickentry(discountpc=0, paymentmode='Cash')
pvs.synchBilingIncentive()
pvs.getIncentivePatientVsServiceReport()
pvs.verifyIncentivePatientVsServiceReport(amount=OpdRate)
pvs.logout()
pvs.closeBrowser()
