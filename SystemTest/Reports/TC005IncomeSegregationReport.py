#Scenarios to test:
# Same Day:
# 1. Cash Invoice, 2. Return Cash Invoice,
# 3. Credit Invoice, 4. Return Credit Invoice,
# 5. Credit Payment,
# 6.Provisional billing, 7.Cancel Provisional bill,
# 8.Deposit, 9.Deduct Deposit, 10.Refund Deposit
# 11.Repeat Scenarios 1-10 for different date.

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
import Library.LibModuleADT as LADT

# front desk user login
itUserId = GSV.itUserID
itUserPwd = GSV.itUserPwD

rateOPD = GSV.opdRate
usgtest = GSV.USG
usgprice = GSV.usgRate
doctor = GSV.doctorGyno
department = GSV.departmentGyno
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(itUserId, itUserPwd)
LB.counteractivation(EMR)
#####Scenario: Cash Invoice with no Discount
LBR.getIncomeSegregation(EMR)
LBR.preSystemIncomeSegregation()
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).InvoiceNo
LBR.getIncomeSegregation(EMR)
LBR.verifyIncomeSegregation(cash=rateOPD, cashReturn=0, credit=0, creditReturn=0, discount=0, provision=0)
#####Scenario: Return Cash Invoice with no Discount
print(">>>>>>Start>Cash Return")
LBR.preSystemIncomeSegregation()
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo, returnmsg="this is bill return 1")
LBR.getIncomeSegregation(EMR)
LBR.verifyIncomeSegregation(cash=0, cashReturn=rateOPD, credit=0, creditReturn=0, discount=0, provision=0)
#####Scenario: Credit Invoice with no Discount
InvoiceNo1 = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Credit', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).InvoiceNo
LBR.preSystemIncomeSegregation()
LBR.getIncomeSegregation(EMR)
LBR.verifyIncomeSegregation(cash=0, cashReturn=0, credit=rateOPD, creditReturn=0, discount=0, provision=0)
LBR.preSystemIncomeSegregation()
#####Scenario: Return Credit Invoice with no Discount
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo1, returnmsg="this is bill return 2")
LBR.getIncomeSegregation(EMR)
LBR.verifyIncomeSegregation(cash=0, cashReturn=0, credit=0, creditReturn=rateOPD, discount=0, provision=0)
#####Scenario: Cash Invoice with Discount
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=discountScheme, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).HospitalNo
LADT.admitDisTrans(danpheEMR=EMR, admit=1, trasfer=0, discharge=0,deposit=0, HospitalNo=HospitalNo, doctor=doctor, department=department)
LBR.getIncomeSegregation(EMR)
LB.createIPprovisionalBill(danpheEMR=EMR,HospitalNo=HospitalNo, test=usgtest)
LBR.preSystemIncomeSegregation()
LBR.getIncomeSegregation(EMR)
LBR.verifyIncomeSegregation(cash=0, cashReturn=0, credit=0, creditReturn=0, discount=0, provision=usgprice)

AC.logout()
AC.closeBrowser()

