# Preconditions in core config: Parameter name: accprimaryhospitalshortname and Parameter GroupName: Accounting.
# Parameter value should be from ACC_MST_Hospital table col name: HospitalShortName

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD

ip = A()

ip.openBrowser()
ip.login(adminUserId, adminUserPwd)
ip.counteractivation()
ip.patientquickentry(discountpc=0, paymentmode='Cash')
ip.getIncentivePaymentReport()
ip.preIncentivePaymentReport()
#ip.createLedgerIncentivePayment()
ip.verifyAcMasterMapping()
ip.IncentivePayment()
ip.getIncentivePaymentReport()
ip.verifyIncentivePaymentReport()

#This test script has open bug: EMR-2725
