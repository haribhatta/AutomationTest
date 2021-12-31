# Objective: To Check Billing Dashboard Summary.
# Scenarios to cover:
# 1. Cash Invoice,
# 2. Return Cash Invoice,
# 3. Cash Discount Invoice,
# 4. Return Cash Discount Invoice,
# 5. Credit Invoice,
# 6. Return Credit Invoice,
# 7. Credit Payment,
# 8. Provisional Bill,
# 9. Cancel Provisional Bill,
# 10. Deposit,
# 11. Deposit Deduct,
# 12. Deposit Refund.
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT

EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno

opdticket = GSV.opdRate
discountpctSeniorCtz = GSV.Membership
#discountamount = (discountpct*opdticket/100)
returnamount = opdticket
usgtest = GSV.USG
usgprice = GSV.usgRate
admisioncharge = GSV.admitRate
deposit = 1000
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
########
# 1. Cash Invoice
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).InvoiceNo  # cash = opdticket
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=opdticket, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 2. Return Cash Invoice
print("2. Return Cash Invoice")
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo, returnmsg="This is cash invoice return")
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 3. Cash Discount Invoice
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
InvoiceNo1 = LA.patientquickentry(danpheEMR=EMR, discountpc=discountpctSeniorCtz, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).InvoiceNo
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=opdticket, discountpc=discountpctSeniorCtz, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 4. Return Cash Discount Invoice
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo1, returnmsg="This is cash discount invoice return")
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=discountpctSeniorCtz, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 5. Credit Invoice
print("##### Credit Invoice #####")
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
InvoiceNo3 = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='CREDIT', department=departmentGynae, doctor=doctorGynae).InvoiceNo
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=opdticket, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 6. Return Credit Invoice
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo3, returnmsg="This is credit invoice return")
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=opdticket,
                            settlement=0, provisional=0, provisionalcancel=0)

# 7. Credit Payment
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo #credit=opdticket
LBR.getBillingDashboard(EMR)
LB.creditPayment(danpheEMR=EMR, HospitalNo=HospitalNo)     #settlement=credit
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=opdticket, creditReturn=0,
                            settlement="CREDIT", provisional=0, provisionalcancel=0)

# 8.1 Provisional Bill
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
HospitalNo = LP.patientRegistration(EMR)
LB.createProvisionalBill(danpheEMR=EMR, HospitalNo=HospitalNo, usgtest=usgtest)  #provisional=usgprice
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0,
                            provisional=usgprice, provisionalcancel=0)

# 8.2 Provisional IP Bill
HospitalNo1 = LP.patientRegistration(EMR)
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
LADT.admitDisTrans(danpheEMR=EMR, HospitalNo=HospitalNo1, admit=1, trasfer=0, discharge=0, deposit=deposit, doctor=doctorGynae, department=departmentGynae)
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=admisioncharge, provisionalcancel=0)
LB.createIPprovisionalBill(danpheEMR=EMR, HospitalNo=HospitalNo1, test=usgtest)
LBR.preSystemDataBillingDashboard()
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=usgprice, provisionalcancel=0)


# 9. Cancel Provisional Bill
LBR.getBillingDashboard(EMR)
LB.cancelIPprovisionalBill(EMR, HospitalNo, usgtest)
LBR.preSystemDataBillingDashboard()
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0,
                            provisional=0, provisionalcancel=usgprice)

print(" EMR-2571: is existing bug to cancel provisional bill")
AC.logout()
AC.closeBrowser()
#End of the test case




