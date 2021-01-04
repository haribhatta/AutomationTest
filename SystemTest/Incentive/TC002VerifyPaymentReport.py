# Preconditions in core config: Parameter name: accprimaryhospitalshortname and Parameter GroupName: Accounting.
# Parameter value should be from ACC_MST_Hospital table col name: HospitalShortName

from TestActionLibrary import A
ip = A()

ip.openBrowser()
ip.login("admin", "pass123")
ip.getIncentivePaymentReport()
ip.preIncentivePaymentReport()
#ip.createLedgerIncentivePayment()
ip.IncentivePayment()
ip.getIncentivePaymentReport()
ip.verifyIncentivePaymentReport()

#This test script has open bug: EMR-2725
