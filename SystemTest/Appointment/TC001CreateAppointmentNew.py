from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

can = A()

can.openBrowser()
can.login(foUserId, foUserPwd)
can.counteractivation()
can.patientquickentry(discountpc=0, paymentmode='Cash')
can.verifyopdinvoice(deposit=0, billamt=500)
can.logout()
can.closeBrowser()
print("Status:Passed - > TC001 CreateAppointmentNew")
