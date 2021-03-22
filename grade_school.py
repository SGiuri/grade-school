class School:
    def __init__(self):
        self.school_DB = {}
        self.name_sorted_school_DB = {}
        # self._school_DB = {}
        pass

    def add_student(self, name, grade):
        self.school_DB[name] = grade
        self.name_sorted_school_DB = dict(sorted(self.school_DB.items(),key=lambda item: item[0]))

    def roster(self):
        return([name for name, values in sorted(self.name_sorted_school_DB.items(),
            key=lambda item: item[1])])

    def grade(self, grade_number):
        sub_db = {key: value for key, value in self.name_sorted_school_DB.items() if value == grade_number}
        return ([name for name, values in sorted(sub_db.items(),
                                                 key=lambda item: item[1])])


