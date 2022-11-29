# Scripted by: Alina Shrestha
# The objective of this test case is to test below issue:
# Headline:
# Incentive | Report | Referral Summary Report > Referral Name is missing in referral summary report.
#
# Description:
# After adding incentive amount for referral doctor, that referral doctor name is not shown in Referral Summary Report.
#
# '''
# ########
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleIncentive as LI

#############
# admin user login
admUserId = GSV.adminUserID
admUserPwd = GSV.adminUserPwD
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
########
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
ReferralName = GSV.doctor2
#discountScheme = GSV.discountSchemeName
#############
EMR = AC.openBrowser()
AC.login(admUserId, admUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
#Scenario: Cash Payment
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
print(HospitalNo)
LI.synchBilingIncentive(EMR)
LI.transactionInvoice(EMR, HospitalNo=HospitalNo, ReferralName=ReferralName, Performer=doctorGynae)
LI.ReferralSummaryReport(EMR, doctorName=ReferralName)