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
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

paymode = "CREDIT"
itemrate = GSV.opdRate

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode="CREDIT", department=GSV.departmentGyno, doctor=GSV.doctorGyno).HospitalNo
LB.verifyCreditNoteDuplicateInvoice(EMR)
LB.creditSettlements(EMR, HospitalNo)
LB.verifyCreditSettlement()  #This function need to add in LibModuleBilling library file.