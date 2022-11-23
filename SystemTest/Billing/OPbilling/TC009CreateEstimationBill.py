import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleADT as LADT
import Library.LibModuleSettings as LS

#AC.applicationSelection()
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
deposite = GSV.deposit
labTestTFT = GSV.TFT
USGName = GSV.USG
USGRate = GSV.usgRate
print("radioTestUSG", USGName)
print("radioTestUSG", USGRate)
priceCategoryType = 'Normal'
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LADT.admitDisTrans(danpheEMR=EMR, HospitalNo=HospitalNo, admit=1, transfer=0, discharge=0, deposit=0, doctor=doctorGynae, department=departmentGynae, admittingDoctorMandatory=isDoctorMandatory)
LB.createIPprovisionalBill(danpheEMR=EMR, HospitalNo=HospitalNo, test=GSV.USG)  #provisional=usgprice
LB.verifyEstimationBill(danpheEMR=EMR, HospitalNo=HospitalNo)
AC.logout()
AC.closeBrowser()
