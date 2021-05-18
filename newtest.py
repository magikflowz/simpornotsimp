
class student:
    def __init__(self):
        self.name = ""
        self.classes = []
        self.grades = []
        self.homework = ""
        self.test = ""
    
    def grading_verification(self, grades):
        if grades >= .90:
            return "Grade is a A"
        elif grades >= 0.80:
            return "Grade is a B"
        elif grades >= .70:
            return "Grade is a C"
        elif grades >= .60:
            return "Grade is a D"

    def student(self):
        class_entries = 0
        self.name = input("What is the students name?: ")
        while True:
            class_entries += 1
            classes = input("Enter a Class %d: "%class_entries)
            if classes == "exit":
                print(self.grading_verification(grades))
                break
            while True:
                try:
                    grades = input("Enter a Grade percent of class %d: "%class_entries)
                    if grades == "exit":
                        break
                    else:
                        grades = float(grades)
                        break
                except:
                    print("\nPlease enter a propper grade or type 'exit' to quit program.\n")
                    continue
            if grades == "exit":
                print(self.grading_verification(grades))
                break
            #self.grades.append(grades)
            #self.classes.append(classes)
           # print(self.classes + self.grades)




test1 = student()
test1.student()

