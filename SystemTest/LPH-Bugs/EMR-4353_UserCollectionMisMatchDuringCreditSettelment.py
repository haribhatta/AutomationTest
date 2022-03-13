'''
Objective:
To test User Collection Report after providing Discount while doing settelment :
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
paymode = "CREDIT"
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymode, department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
LBR.getUserCollectionReport(EMR, user=GSV.foUserID)
LBR.preSystemUserCollectionReport()
LB.createCreditLabInvoice(EMR, HospitalNo=HospitalNo, labtest=GSV.USG)
LB.creditSettlements(EMR, HospitalNo=HospitalNo, ProvisionalSlip="No", cashdiscount=50)
LBR.getUserCollectionReport(EMR, user=GSV.foUserID)
LBR.verifyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=0, tradeDiscount=0, cashDiscount=50, deposit=0, depositreturn=0, creditsettlement=1000, provisional=0, provisionalcancel=0)
AC.logout()
AC.closeBrowser()
