import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
import Library.LibModuleADT as LADT
import Library.LibModuleSettings as LS

# front desk user login
itUserId = GSV.itUserID
itUserPwd = GSV.itUserPwD
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
# user = GSV.itUserID
USG = GSV.USG
TotalAmt = GSV.usgRate
#
opdRate = GSV.opdRate
# AC.applicationSelection()
EMR = AC.openBrowser()
######## Precondition Check: isAdmittingDoctorMandatory?
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
AC.logout()
########
AC.login(itUserId, itUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, deposit=0, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
LB.createIPprovisionalBill(danpheEMR=EMR, HospitalNo=HospitalNo, test=USG)
LB.cancelIPprovisionalBill(danpheEMR=EMR, HospitalNo=HospitalNo, canceltest=USG)
LBR.verifyCancelBillReport(danpheEMR=EMR, HospitalNo=HospitalNo, expectedTotalCancelAmt=TotalAmt)
AC.logout()
AC.closeBrowser()
