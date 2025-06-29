from pony.orm import * # type: ignore

from datetime import datetime


db = Database("sqlite", "estore.sqlite", create_db=True)

class Student(db.Entity):
    MilitaryDistrict = Optional(str)
    MilitaryUnitName = Optional(str)
    MilitaryUnitNumber = Optional(int) 
    IsConscript = Optional(bool)
    PersonalNumber = Optional(str)
    Rank = Optional(str)
    Name = Optional(str)
    Surname = Optional(str)
    Patronimic = Optional(str)
    BirthDate = Optional(datetime) 
    SNILS = Optional(str)
    IsVeteran = Optional(bool)
    Education = Optional(str)
    EducationalInstitution = Optional(str)
    PhoneNumber = Optional(str)
    ArrivalDate = Optional(datetime)
    Faculty = Optional(int)
    Post = Optional(str)
    BirthPlace = Optional(str)
    StateRewards = Optional(str)
    DepartmentRewards = Optional(str)
    IsMarried = Optional(bool)
    IsSMOMember = Optional(bool)
    EducationEndDate = Optional(datetime)
    IsChild = Optional(bool)
    Squad = Optional(int)
    Division = Optional(int)
    IsFired = Optional(bool)
    IsTransfered = Optional(bool)
    TransferedTo = Optional(int)
    InHospital = Optional(bool)


sql_debug(True)
db.generate_mapping(create_tables=True)