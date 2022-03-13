# Preconditions in core config: Parameter name: accprimaryhospitalshortname and Parameter GroupName: Accounting.
# Parameter value should be from ACC_MST_Hospital table col name: HospitalShortName
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
import Library.LibModuleAccounting as LACC
# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
doctorGyno = GSV.doctorGyno
departmentGyno = GSV.departmentGyno
########
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGyno, doctor=doctorGyno, priceCategoryType=priceCategoryType)
LI.getIncentivePaymentReport(EMR, doctorGyno)
LI.preIncentivePaymentReport()
#ip.createLedgerIncentivePayment()
LACC.verifyAcMasterMapping()
LI.IncentivePayment(EMR, doctorGyno)
LI.getIncentivePaymentReport(EMR, doctorGyno)
LI.verifyIncentivePaymentReport()

#This test script has open bug: EMR-2725
