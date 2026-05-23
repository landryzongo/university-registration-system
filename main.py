class Person:
   def __init__(self, name,firstname, age, is_active):
      self.name = name
      self.firstname = firstname
      self.age = age
      self.is_active = is_active

   def display_info(self):
      print(f"Name: {self.name}")
      print(f"First Name: {self.firstname}")
      print(f"Age: {self.age}")
      print(f"Active: {'Yes' if self.is_active else 'No'}")
      
   def __str__(self):
      return f"{self.firstname} {self.name}, Age: {self.age}, Active: {'Yes' if self.is_active else 'No'}"
    

