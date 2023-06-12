
class Person:
    def __init__(self, name :str, age :int):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, I'm {self.name}")

class Group:
    def __init__(self, name :str):
        self.name = name
        self.members = []

    def print_members(self):
        for member in self.members:
            print(f"Hello, I'm {member.name}")
            
    def add_member(self, member: Person):
        self.members.append(member)
    
    def create_person_member(self, *args):
        self.members.append(Person(*args))
        # Return the last member added
        return self.members[-1]
            
if __name__ == '__main__':
    person = Person("John", 36)
    person.say_hello()
    
    Group = Group("Group 1")
    Group.members.append(Person("John", 36))
    Group.members.append(Person("Mary", 24))
    Group.print_members()
    Group.add_member(Person("Peter", 48))
    Group.print_members()
    Group.add_member(Person("Benjamin", 28))
    Group.print_members()
    test = Group.create_person_member("Julia", 32)
    Group.print_members()
    print(test)
    