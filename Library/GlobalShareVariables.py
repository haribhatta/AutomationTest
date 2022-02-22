########Defining Variables for LPH
#runEnv = 'free'
appName = input("Please enter project/application name:\n"
                "SNCH\n"
                "MMH\n"
                "LPH\n"
                "MPH\n"
                "RTM\n"
                "Core\n")

if appName == "LPH":
      appURL = "http://202.51.74.168:453/"
###Login Credentials:
      #admin user
      adminUserID = 'admin'
      adminUserPwD = 'pass123'    # '28A7hi0jvH0='
      #IT user
      itUserID = 'bhuwan'
      itUserPwD = 'pass123'
      #billing user
      foUserID = 'ashmita' #LPH user
      foUserPwD = 'pass123'
      foUserName = 'Ms. Ashmita Karki'
      #Lab user
      labUserID = 'karuna'
      labUserPwD = 'pass123'
      #ER Lab user
      ERlabUserID = 'erlab'
      ERlabUserPwD = 'pass123'
      #radiologist user
      radioUserID = 'radiology'
      radioUserPwD = 'pass123'
      #pharmacy user
      pharmacyUserID = 'debika'
      pharmacyUserPwD = 'pass123'
      pharmacyUserName = 'Debika'
      #pharmacyUserName = 'Ms. Debika'
      #nurse user
      nurseUserID = 'admin'
      nurseUserPwD = 'pass123'
      #store user
      storeUserID = 'shreeram'
      storeUserPwD = 'pass123'
      #Medical Record user
      MRUserID = 'mr'
      MRUserPwD = 'pass123'
      #vaccination user
      vaccineUserID = 'surendra'
      vaccineUserPwD = 'pass123'
###Billing Items Name:
      opdRate = 30
      deposit = 100
      CBC = "CBC"
      TFT = "TFT"
      TFTRate = 800
      LDH = "LDH"
      USG = "USG ABDOMEN/PELVIS"
      usgRate = 700
      admitRate = 30
      UrineRE = "URINE R/E"
      BTCT = "BT/CT"
      btctRate = 100
      erTest = "TC"
      LabType = "ER"
      #EHS Billing
      opdRateEHS = 400
###Pharmacy/Dispensary Items Name:
      drug1GenericName = 'PANTOPRAZOLE 40 MG TAB'
      drug1Rate = 5
      drug1BrandName = 'PETOR 40 MG'
      drug2BrandName = "MACLAR 500MG TAB"
      drug2GenericName = "CLARITHROMYCIN"
      drug2Rate = 563.5
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'SINEX TAB'
      drugSinexRate = 3
      Testdrug = "testdrugreport"
      supplier = "A.G. HEALTHCARE"
      insurancedrug = "AMFAST 5MG TAB"
      drug1NarcoticName = "MORFIUM 10 MG TAB"
      drug1NarcoticRate ="4"

###Inventory/Store Items Name:
      Inventory1 = "General Inventory"
      SubStoreName1 = "ADMINISTRATION"
      Dispensary1 = "MainDispensary"
      dispensaryName = "MainDispensary"
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      storeItem1Name = "PLANE SCISSOR 6"
      storeItem1Rate = 25
      #stationaryItem1 = "DOTPEN"
      stationaryItem1 = "USG PAPER"
###Sub Stores Name:
      SubStore1 = "ACCOUNT"
      SubStore2 = "ADMINISTRATION"
      store1 = "ADMINISTRATION"
###Doctors/Departments Name:
      doctorGyno = "Dr. doctor doctor"
      departmentGyno = "GYNAE & OBS"
      doctorGynoEHS = "Dr. Anupa Thapa"
      doctor2 = "Mr. admin admin"
###Wards
      generalWard = "Labour Ward"
      generalBedFeature = "General Bed"
###ADT:
      admitWard = "Labour Ward"
      admitBed = "General Bed"

###Discount Scheme
      discountSchemeType = "Helpless"
      discountSchemeName = "Helpless (50%)"

###Users Name:
      UserBilling = 'Mr. Bhagawati Pandey'
###############################################################################
########Defining Variables for SNCH
if appName == "SNCH":
      appURL = "http://202.51.74.168:168/"
###Login Credentials:
      # admin user
      adminUserID = 'admin'
      adminUserPwD = 'pass123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'sabitri'
      foUserPwD = 'pass123'
      foUserName = 'Ms. Sabitri Sharma Adhikari'
      #IT user
      itUserID = 'rn'
      itUserPwD = 'pass123'
      #pharmacy user
      pharmacyUserID = 'shivraj'
      pharmacyUserPwD = 'pass123'
      pharmacyUserName = 'shiv raj'
      #laboratory user
      labUserID = 'gayatri'
      labUserPwD = 'pass123'
      # Radiology user
      radioUserID = 'bharat'
      radioUserPwD = 'pass123'
      #Inventory user
      storeUserID = 'admin'
      storeUserPwD = 'pass123'
      #Medical Record user
      MRUserID = 'haris'
      MRUserPwD = 'pass123'
### Bill Items Name:
      opdRate = 500
      deposit = 200
      CBC = "CBC"
      TFT = "FREE TFT"   #TFT(FT3,FT4,TSH) CLLEA
      T3 = "FT3"
      T4 = "FT4"
      TSH = "TSH"
      TFTRate = 1200
      LDH = "LDH"
      UrineRE = "URINE R/E" # this gets changed on V1.49.3
      BTCT = "BT/CT"
      btctRate = 300
      USG = "USG ABDOMIN AND PELVIS"
      usgRate = 1000
      admitRate = 1500
###Pharmacy/Dispensary Items Name:
      dispensaryName = "MainDispensary"
      drug1BrandName = "SINEX TAB"
      drug1GenericName = "quinapril"
      drug1Rate = 3
      drug2BrandName = 'ASTHALIN 2 MG TAB'
      drug2BrandRate = 1.14
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'SINEX TAB'
      drugSinexRate = 3
      drugAasma = 'AASMA 150 XR TAB'
      Testdrug = "Testdrugreport"
      supplier = "AAKAR ENTERPRISES"
      drug1NarcoticName = "MORFIUM 1ML ING"
      drug1NarcoticRate = 100
###Inventory/Store Items Name:
      GeneralInventory = "General Inventory"
      Dispensary1 = "General Inventory"
      A4Paper = 'A4 PAPER'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      stationaryItem1 = "PENCIL"
      File = "FILE"
###Sub Stores Name:
      SubStore1 = "General"
      SubStore2 = "PostOps"
###Doctors/Departments List
      doctorGyno = "Dr. Jyoti Rana"
      departmentGyno = "Gynecology"
      departmentNephro = "Nephro"
###Suppliers Name list
      supplierShremad = "Shremad Tech."
      supplierName2 = "AAKAR ENTERPRISES"
###Wards Name:
      generalWard = "General Ward"
      GeneralWard = "ICU"
      #wardid = "General Ward"
      bedFeature = "BED CHARGE General Ward"
      ###ADT:
      admitWard = "Pediatric Ward"
      admitBed = "Pediatric Bed Charge"
###Users Name:
      user = "admin"
###Discount Scheme
      discountSchemeType = "SocialService"
      discountSchemeName = "Social Service Unit"
###############################################################################
########Defining Variables for Medi Plus
if appName == "MPH":
      appURL = "http://202.51.74.168:129/"
###Login Credentials:
      #admin user
      adminUserID = 'admin'
      adminUserPwD = 'pass123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'bandana'
      foUserPwD = 'pass123'
      foUserName = 'Ms. Bandana Harmel'
      #IT user
      itUserID = 'alina'
      itUserPwD = 'pass123'
      #Lab user
      labUserID = 'supriya'
      labUserPwD = 'pass123'
      #ER Lab user
      ERlabUserID = 'erlab'
      ERlabUserPwD = 'pass123'
      #radiologist user
      radioUserID = 'basudev'
      radioUserPwD = 'pass123'
      #pharmacy user
      pharmacyUserID = 'kishor'
      pharmacyUserPwD = 'pass123'
      #nurse user
      nurseUserID = 'admin'
      nurseUserPwD = 'pass123'
      #store user
      storeUserID = 'radha'
      storeUserPwD = 'pass123'
###Billing Items Name:
      opdRate = 660
      deposit = 1000
      CBC = "COMPLETE BLOOD COUNT-CBC"
      CBCRate = 1100
      TFT = "TFT"
      T3 = "FT3"
      T4 = "FT4"
      TSH = "TSH"
      TFTRate = 500
      LDH = "LDH"
      LDHRate = 600
      USG = "USG ABDOMEN AND PELVIS"
      usgRate = 1300
      admitRate = 30
      UrineRE = "URINE R/E "
      UrineRERare = 125
      BTCT = "BT CT"
      btctRate = 200
      erTest = "TC, DC"
      LabType = "ER"
###Pharmacy/Dispensary Items Name:
      drug1BrandName = 'NIKO DROP 15ML BOTTLE'
      drug1GenericName = 'PARACETAMOL 150MG/ML ORAL DROP 15ML BOTTLE'
      drug1Rate = 25
      drug2BrandName = "MACLAR 500MG TAB"
      drug2GenericName = "CLARITHROMYCIN"
      drug2Rate = 563.5
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      Testdrug = "testdrugreport"
      drugSinexName = 'SINEX'
      drugSinexRate = 3
###Inventory/Store Items Name:
      Inventory1 = "General Inventory"
      SubStoreName1 = "ADMINISTRATION"
      Dispensary1 = "MainDispensary"
      dispensaryName = "Main Dispensary"
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      storeItem1Name = "Tumb Pin"
      storeItem1Rate = 10
      #stationaryItem1 = "DOTPEN"
      stationaryItem1 = "envelop print"
###Sub Stores Name:
      SubStore1 = "General"
      SubStore2 = "PostOps"
      store1 = "Administration Sub Store"
###Doctors/Departments Name:
      doctorGyno = "Dr. Anjali Subedi"
      departmentGyno = "OBG Gynae"
###Wards Name:
      generalWard = "General Non-Covid Ward"
      bedFeature = "General Non-Covid Ward"
###ADT:
      admitWard = "General Non-Covid Ward"
      admitBed = "Pediatric Bed Charge"
###Users Name:
      UserBilling = 'Mr. Bhagawati Pandey'
###Discount Scheme
      discountSchemeType = "StaffFamily"
      discountSchemeName = "Staff Family (30%)"
      ###Doctors/Departments List
      doctorNephro = "Dr. Eva Gauchan"
      departmentNephro = "Pediatrics "
      doctor2 = "Dr. Junu Shrestha"


###############################################################################
########Defining Variables for Rhythm
###############################################################################
if appName == "RTM":
      appURL = "http://202.51.74.168:85/"
###Login Credentials:
      # admin user
      adminUserID = 'admin'
      adminUserPwD = 'pass123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'mamata'
      foUserPwD = 'pass123'
      foUserName = 'Ms. Mamata Gartaula'
      #IT user
      itUserID = 'admin'
      itUserPwD = 'pass123'
      #pharmacy user
      pharmacyUserID = 'Prekshya'
      pharmacyUserPwD = 'pass123'
      #pharmacyUserName = 'Ms. Prekshya Adhikari'
      pharmacyUserName = 'Prekshya Adhikari' # Ms. is removed due to Rhythm 'User Collection Report' not having salutation field.
      #laboratory user
      labUserID = 'muna'
      labUserPwD = 'pass123'
      #Inventory user
      storeUserID = 'sunita'
      storeUserPwD = 'pass123'
### Bill Items Name:
      opdRate = 500
      deposit = 200
      CBC = "CBC(HB,TC,DC,PLT)"
      TFT = "TFT(T3,T4,TSH)"   #TFT(FT3,FT4,TSH) CLLEA
      T3 = "T3"
      T4 = "T4"
      TSH = "TSH"
      TFTRate = 1050
      LDH = "LACTIC DEHYDROGENASE(LDH)"
      UrineRE = "URINE RE/ME" # this gets changed on V1.49.3
      BTCT = "BT/CT"
      btctRate = 350
      USG = "ULTRA SOUND"
      usgRate = 1000
      admitRate = 1200
###Pharmacy/Dispensary Items Name:
      dispensaryName = "MainDispensary"
      drug1BrandName = "SAMCOBA 1500 MG"
      drug1GenericName = "mecobalamin"
      drug1Rate = 20
      drug2BrandName = 'ASTHALIN 2 MG TAB'
      drug2BrandRate = 1.14
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'SINEX TAB'
      drugSinexRate = 3
      drugAasma = 'AASMA 150 XR TAB'
      Testdrug = "Testdrugreport"
      supplier = "AARATI MEDITCHA PVT"
      drug1NarcoticName = "LOZ 1 MG"
      drug1NarcoticRate ="2"
###Inventory/Store Items Name:
      GeneralInventory = "General Inventory"
      Dispensary1 = "General Inventory"
      A4Paper = 'A4 PAPER'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      stationaryItem1 = "PENCIL"
      File = "FILE"
###Sub Stores Name:
      SubStore1 = "General"
      SubStore2 = "PostOps"
###Doctors/Departments List
      doctorGyno = "Dr. Lata Gautam"
      departmentGyno = "PSYCHIATRIC"
      departmentNephro = "Nephro"
###Suppliers Name list
      supplierShremad = "Shremad Tech."
      supplierName2 = "AARATI MEDITCHA PVT"
###Wards Name:
      generalWard = "General Ward"
      GeneralWard = "ICU"
      #wardid = "General Ward"
      bedFeature = "General"
      ###ADT:
      admitWard = "General Ward"
      admitBed = "Pediatric Bed Charge"
###Users Name:
      user = "admin"
###Discount Scheme
      discountSchemeType = "Staff"
      discountSchemeName = "Staff (50%)"

   #def __str__():
    #  return