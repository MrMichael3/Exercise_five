### implement class Module here ###
class Module:
    def __init__(self, ects, title, semester, grade=None):
        self.ects = ects
        self.title = title
        self.semester = semester
        self.grade = grade
        self.dates = []
        self.elements = []

    def get_important_dates_overview(self):
        for date in self.dates:
            print(date)

    def set_grade(self, new_value):
        self.grade = new_value

    def add_module_element(self, cl, d):
        new = cl(self)
        new.add_important_date(d)
        self.elements.append((cl, d))



################################################################################

### implement class ModuleElement here ###


class ModuleElement(object):
    def __init__(self, module):
        self.module = module

    def add_important_date(self, kind, date):
        self.module.dates.append((kind, date))


################################################################################

### implement class Lesson here ###
class Lesson(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Lesson", date)


################################################################################

### implement class Lab here ###
class Lab(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Lab", date)


################################################################################

### implement class Midterm here ###
class Midterm(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Midterm", date)


################################################################################

### implement class FinalExam here ###
class FinalExam(ModuleElement):

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "FinalExam", date)


################################################################################

### test cases ###

info1 = Module(6, "Info 1", 1)
info1.add_module_element(Midterm, "31.10.2017")
info1.add_module_element(FinalExam, "20.12.2017")
info1.get_important_dates_overview()
