import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
import Library.LibModuleADT as LAD
import Library.LibModuleSettings as LS

#AC.applicationSelection()
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
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
LB.createProvisionalBill(EMR, HospitalNo, GSV.USG)  #provisional=usgprice
LAD.admitDisTrans(EMR, admit=1, discharge=0, transfer=0, HospitalNo=HospitalNo, deposit=0, doctor=doctorGynae, department=departmentGynae, admittingDoctorMandatory=isDoctorMandatory)
LB.createIPprovisionalBill(EMR,HospitalNo,GSV.USG)
LB.verifyEstimationBill(EMR, HospitalNo)
LAD.admitDisTrans(EMR, admit=0, discharge=1, transfer=0, HospitalNo=HospitalNo, deposit=0, doctor=doctorGynae, department=departmentGynae, admittingDoctorMandatory=isDoctorMandatory)
