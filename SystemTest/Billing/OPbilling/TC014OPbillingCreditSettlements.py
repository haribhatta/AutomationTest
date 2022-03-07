'''
Objective:
To test below checkpoints:
1. Create out patient credit invoice.
2. Verify credit invoice (i.e. Credit Note).
3. Do credit settlement.
4. Verify credit settlement slip.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB

# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
itemrate = GSV.opdRate
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo1, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode="Credit", department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
LB.createCreditLabInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=GSV.USG)
LB.creditSettlements(danpheEMR=EMR, HospitalNo=HospitalNo, ProvisionalSlip="No", cashdiscount=0)
LB.verifyCreditSettlement(danpheEMR=EMR, HospitalNo=HospitalNo, itemRate=itemrate)