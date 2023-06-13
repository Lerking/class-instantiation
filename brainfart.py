import timeit
from memory_profiler import profile

@profile
class BrainFart:
    """
    Class to test for benefit of replacing all local
    variables, in favor of instanciated variable space in the class it self.
    """
    def __init__(self):
        self.__reset_locals()

    def __reset_locals(self):
        self.local1 = None
        self.local2 = None
        self.local3 = None
        self.local4 = None
        self.local5 = None
        self.local6 = None
        self.local7 = None
        self.local8 = None
        self.local9 = None
        self.local10 = None
    
    @profile
    def test_with_local_var(self):
        loc1 = [x for x in range(10)]
        loc2 = [y for y in range(10)]
        loc3 = [z for z in range(10)]
        loc4 = [x for x in range(10)]
        loc5 = [y for y in range(10)]
        loc6 = [z for z in range(10)]
        loc7 = [x for x in range(10)]
        loc8 = [y for y in range(10)]
        loc9 = [z for z in range(10)]
        loc10 = [x for x in range(10)]
    
    @profile
    def test_without_local_var(self):
        self.local1 = [x for x in range(10)]
        self.local2 = [y for y in range(10)]
        self.local3 = [z for z in range(10)]
        self.local4 = [x for x in range(10)]
        self.local5 = [y for y in range(10)]
        self.local6 = [z for z in range(10)]
        self.local7 = [x for x in range(10)]
        self.local8 = [y for y in range(10)]
        self.local9 = [z for z in range(10)]
        self.local10 = [x for x in range(10)]
        self.__reset_locals()

if __name__ == "__main__":
    bf = BrainFart()
    #print(timeit.timeit(bf.test_with_local_var))
    #print(timeit.timeit(bf.test_without_local_var))
    bf.test_with_local_var()
    bf.test_without_local_var()