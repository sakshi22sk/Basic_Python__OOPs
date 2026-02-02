class university:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f"University Name: {self.name}, Location: {self.location}"
class teacher(university):
    def __init__(self, name, location, subject):
        super().__init__(name, location)
        self.subject = subject

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Subject: {self.subject}"
class student(university):
    def __init__(self, name, location, major):
        super().__init__(name, location)
        self.major = major

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Major: {self.major}"
class teaching_assistant(teacher,student):
    def __init__(self,name,Location,subject,major):
        teacher.__init__(self,name,Location,subject)
        student.__init__(self,name,Location,major
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Major: {self.major}"  
s=student("ABC University", "New York", "Computer Science")
t=teacher("ABC University", "New York", "Mathematics")
print(s.get_info())
print(t.get_info())
#################33

class vehicle:
    def __init__(self,type):
        self.type=type
    def get_info(self):
        return f"Vehicle Type: {self.type}"
class car(vehicle):
    def __init__(self,type,brand):
        super().__init__(type)
        self.brand=brand
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Brand: {self.brand}"  
class boat(vehicle):
    def __init__(self,type,length):
        super().__init__(type)
        self.length=length
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Length: {self.length} feet"
b=boat("Boat","30")
print(b.get_info())
###################33333
class device:
    def __init__(self,type):
        self.type=type
class camera(device):
    def __init__(self,type,resolution):
        super().__init__(type)
        self.resolution=resolution
class phone(device):
    def __init__(self,type,os):
        super().__init__(type)
        self.os=os
    def get_info(self):
        return f"Device Type: {self.type}, Operating System: {self.os}"
class smartgadget(camera,phone):
    def __init__(self,type,resolution,os):
        camera.__init__(self,type,resolution)
        phone.__init__(self,type,os)
    def get_info(self):
        base_info=phone.get_info(self)
        return f"{base_info}, Camera Resolution: {self.resolution} MP"
s=smartgadget("Smartphone","108","Android")
print(s.get_info())
##########################
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"
class dancer(person):
    def __init__(self,name,age,style):
        super().__init__(name,age)
        self.style=style
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Dance Style: {self.style}"
class singer(person):
    def __init__(self,name,age,genre):
        super().__init__(name,age)
        self.genre=genre
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Music Genre: {self.genre}"
class performer(dancer,singer):
    def __init__(self,name,age,style,genre):
        dancer.__init__(self,name,age,style)
        singer.__init__(self,name,age,genre)
    def get_info(self):
        base_info=dancer.get_info(self)
        return f"{base_info}, Music Genre: {self.genre}"
p=performer("Alice",25,"Ballet","Pop")
print(p.get_info())
#################33
class company:
    def __init__(self,name,industry):
        self.name=name
        self.industry=industry
    def get_info(self):
        return f"Company Name: {self.name}, Industry: {self.industry}"
class programmer:
    def __init(sel,language):
        self.language=language
    def get_info(self):
        return f"Programming Language: {self.language}"
class tester:
    def __init__(self,tools):
        self.tools=tools
    def get_info(self):
        return f"Testing Tools: {self.tools}"
t=tester("Selenium")
print(t.get_info())
#######################
class bank:
    def __init__(self,name,location):
        self.name=name
        self.location=location  
    def get_info(self):
        return f"Bank Name: {self.name}, Location: {self.location}"
class savings_account(bank):
    def __init__(self,name,location,interest_rate):
        super().__init__(name,location)
        self.interest_rate=interest_rate
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Interest Rate: {self.interest_rate}%"
class loan_account(bank):
    def __init__(self,name,location,loan_amount):
        super().__init__(name,location)
        self.loan_amount=loan_amount
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Loan Amount: ${self.loan_amount}"
s=saving_account("XYZ Bank","Los Angeles",3.5)
print(s.get_info())
#######################3
class media:
    def __init__(self,title):
        self.title=title
    def get_info(self):
        return f"Title: {self.title}"
class audio(media):
    def __init__(self,title,duration):
        super().__init__(title)
        self.duration=duration
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Duration: {self.duration} minutes"
class video(media):
    def __init__(self,title,resolution):
        super().__init__(title)
        self.resolution=resolution
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Resolution: {self.resolution}p"
v=video("Nature Documentary","1080")
print(v.get_info())
#######################
class school:
    def __init__(self,name,location):
        self.name=name
        self.location=location  
    def get_info(self):
        return f"School Name: {self.name}, Location: {self.location}"
class sports_student(school):
    def __init__(self,name,location,sport):
        super().__init__(name,location)
        self.sport=sport
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Sport: {self.sport}"
class music_students(school):
    def __init__(self,name,location,instrument):
        super().__init__(name,location)
        self.instrument=instrument
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Instrument: {self.instrument}"
s=sports_student("Highland School","Chicago","Basketball")
print(s.get_info())
###################
class online_platform:
    def __init__(self):
        pass
class buyer:
    def __init__(self,budget):
        self.budget=budget
    def get_info(self):
        return f"Budget: ${self.budget}"
class seller:
    def __init__(self,sell):
        self.sell=sell
    def get_info(self):
        return f"Items for Sale: {self.sell}"
class marketplaceuser(self,buyer,seller):
    def __init__(self,budget,sell):
        buyer.__init__(self,budget)
        seller.__init__(self,sell)
    def get_info(self):
        base_info=buyer.get_info(self)
        return f"{base_info}, Items for Sale: {self.sell}"
m=marketplaceuser(500,"Electronics")
print(m.get_info())
#################
class transport:
    def __init__(self,mode):
        self.mode=mode
    def get_info(self):
        return f"Transport Mode: {self.mode}"
class busservice(transport):
    def __init__(self,mode,route):
        super().__init__(mode)
        self.route=route
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Route: {self.route}"
class trainsservice(transport):
    def __init__(self,mode,line):
        super().__init__(mode)
        self.line=line
    def get_info(self):
        base_info=super().get_info()
        return f"{base_info}, Line: {self.line}"
b=busservice("Bus","Downtown Loop")
print(b.get_info())
###############