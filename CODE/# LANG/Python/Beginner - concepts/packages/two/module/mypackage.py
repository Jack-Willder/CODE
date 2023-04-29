class Mypackage:
    def studentnames(self):
        print("Enter the names of the students are : ")
        self.name = {}
        self.rollno = 0
        self.studentinput()
    def studentinput(self):
        name = str(input("-> "))
        if not name:
            if not self.name:
                print("No Name")
            else:
                print(self.name)
        else:
            self.rollno += 1
            self.name.update({self.rollno: name})
            self.studentinput()
