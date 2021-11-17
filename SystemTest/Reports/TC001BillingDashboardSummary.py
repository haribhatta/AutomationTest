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

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT
AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno

opdticket = GSV.opdRate
discountpct = 50
#discountamount = (discountpct*opdticket/100)
returnamount = opdticket
usgtest = GSV.USG
usgprice = GSV.usgRate
admisioncharge = GSV.admitRate
deposit = 1000
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
########
# 1. Cash Invoice
LB.getBillingDashboard()
HospitalNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae)  # cash = opdticket
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=opdticket, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 2. Return Cash Invoice
print("2. Return Cash Invoice")
LB.getBillingDashboard()
LB.returnBillingInvoice("This is cash invoice return")
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 3. Cash Discount Invoice
LB.getBillingDashboard()
HospitalNo1 = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae)
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=opdticket, discountpc=discountpct, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 4. Return Cash Discount Invoice
LB.getBillingDashboard()
LB.returnBillingInvoice("This is cash discount invoice return")
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=0, discountpc=discountpct, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 5. Credit Invoice
print("##### Credit Invoice #####")
LB.getBillingDashboard()
HospitalNo3 = LA.patientquickentry(discountpc=0, paymentmode='CREDIT', department=departmentGynae, doctor=doctorGynae)
#LB.verifyopdinvoice()
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=opdticket, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 6. Return Credit Invoice
LB.getBillingDashboard()
print("Returning Credit Invoice")
LB.returnBillingInvoice("This is credit invoice return")
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=opdticket,
                            settlement=0, provisional=0, provisionalcancel=0)

# 7. Credit Payment
LB.getBillingDashboard()
HospitalNo4 = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae) #credit=opdticket
#LB.verifyopdinvoice()
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.creditPayment(HospitalNo4)     #settlement=credit
LB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=opdticket, creditReturn=0,
                            settlement="CREDIT", provisional=0, provisionalcancel=0)

# 8.1 Provisional Bill
LB.getBillingDashboard()
LP.patientRegistration()
LB.createProvisionalBill(usgtest)  #provisional=usgprice
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0,
                            provisional=usgprice, provisionalcancel=0)

# 8.2 Provisional IP Bill
LP.patientRegistration()
LB.getBillingDashboard()
LADT.admitDisTrans(1, 0, 0, deposit, doctor=doctorGynae, department=departmentGynae)
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=admisioncharge, provisionalcancel=0)
LB.createIPprovisionalBill(usgtest)
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=usgprice, provisionalcancel=0)


# 9. Cancel Provisional Bill
LB.getBillingDashboard()
LB.cancelIPprovisionalBill(usgtest)
LB.preSystemDataBillingDashboard()
LB.getBillingDashboard()
LB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0,
                            provisional=0, provisionalcancel=usgprice)

print(" EMR-2571: is existing bug to cancel provisional bill")
AC.logout()
AC.closeBrowser()
#End of the test case




