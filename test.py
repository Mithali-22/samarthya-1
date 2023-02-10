# class person:
#           def __init__ (self,name,age):
#                   self.name = name
#                   self.age=age
#           def myfunc(self):
#                    print("hello my name is"+ self.name)
#           def __str__(self):
#                    return "Name:" + self.name +",age:"+ str(self.age)
# p1 =person("john",36)
# p1.myfunc()
# print(p1)

# class person:
#           def __init__ (self,name,age):
#                   self.name = name
#                   self.age=age
#           def myfunc(self):
#                    print(f"hello my name is {self.name} and my age is{self.age}")
#           def __str__(self):
#                    return "Name:" + self.name +",age:"+ str(self.age)
# p1 =person("john",36)
# p1.myfunc()
# print(p1)

# class car:
#     def __init__(details,brand,model,colour):
#         details.brand=brand
#         details.model=model
#         details.colour=colour
#     def myfunc(details):
#         print(f"brand of the car is {details.brand} ,model of the car is {details.model} and colour of the car is {details.colour}")
#     def __str__(details):
#         return "brand:" + details.brand + ",model:" + details.model + ",colour:" +details.colour
# p1=car("x1","BMW","White")
# p1.myfunc()
# print(p1)

# class person:
#           def __init__ (self,name,age):
#                   self.name = name
#                   self.age=age
#           def __add__(self,other):
#                   return self.name + other.name 
#                   return self.age + other.age      
#           def myfunc(self):
#                    print("hello my name is "+ self.name)
#           def __str__(self):
#                    return "Name:" + self.name +",age:"+ str(self.age)
# p1 =person("john",36)
# p2=person("keerthana",19)
# p1.myfunc()
# print(p1 + p2)


      