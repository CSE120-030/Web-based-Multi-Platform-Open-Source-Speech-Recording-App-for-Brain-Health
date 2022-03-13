from helper_functions import *
from datetime import date
language=1
expert=1
d = date(2000,9,15)
print(d)
#create_expert("expert1","1234","fName","lName","00000","123@asd.com")
#create_language(name="English",prefix="eng")
create_patient(username="patient2",password="1234",firstName="fName",lastName="lName",languageId=language,e="1234@asd.com",expertId=expert,dob=d,sex="M")


