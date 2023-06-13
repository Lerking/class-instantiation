import random, string

class Person:
    def __init__(self, name :str, age :int):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old")

class Group:
    def __init__(self, name :str):
        self.name = name
        self.members = []

    def print_members(self):
        for member in self.members:
            print(f"Hello, I'm {member.name} and I'm {member.age} years old")
            
    def add_member(self, member: Person):
        self.members.append(member)
    
    def create_person_member(self, *args):
        self.members.append(Person(*args))
        # Return the last member added
        return self.members[-1]

if __name__ == '__main__':
    #person = Person("John", 36)
    #person.say_hello()
    
    Group = Group("Group 1")
    #Group.members.append(Person("John", 36))
    #Group.members.append(Person("Mary", 24))
    #Group.print_members()
    #Group.add_member(Person("Peter", 48))
    #Group.print_members()
    #Group.add_member(Person("Benjamin", 28))
    #Group.print_members()
    for _ in range(100):
        Group.create_person_member(
            ''.join(random.choices(string.ascii_lowercase, k=5)),
            random.randint(1,100)
            )
    Group.print_members()
    #print(test)
    