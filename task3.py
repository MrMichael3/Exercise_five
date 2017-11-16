
### implement class Module here ###

################################################################################

### implement class Lecture here ###

################################################################################

### implement class Thesis here ###

################################################################################

### implement class Seminar here ###

################################################################################

### test cases ###

info1 = Lecture(6,"Info 1",1,"Harald Gall")
info1.set_exam_date("11-11-2017")
info1.get_important_dates_overview()

internet_economics = Seminar(3,"Internet Economics",5,"Burkhardt Stiller")
internet_economics.set_presentation_date("12-12-2019")
internet_economics.set_deadline_date("1-1-2020")
internet_economics.get_important_dates_overview()
