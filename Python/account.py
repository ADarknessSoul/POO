class Account:
    id = int
    name = str
    document = str
    email = str
    password = str

    def __init__(self,name,document):
        self.name = name
        self.document = document

    def drive(self):
        print(self.name + "está conduciendo")