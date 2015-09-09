class Musician(object): #When we need to model more complicated 
                         #things we can use classes.
    
    def __init__(self, sounds): #You can add any properties to any instance. 
                                #But when you know that instances of a class 
                                #should always contain a property we can use a shortcut: the __init__ method:
        self.sounds = sounds
        
    def solo(self, length): #this is a function- solo is the function name, self and length are it's attributes.
        for i in range(length): #the range function is designed to generate a list of numbers, which is generally used to iterate over with "for" loops.
            print self.sounds [i % len(self.sounds)],
        print ""
    
class Bassist(Musician): 
    def __init__(self): #this is a function
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])
    
class Guitarist(Musician):
    def __init__(self): #this is a function
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
        
        
    def tune(self): #function
        print "Be with you in a moment"
        print "Twoning, sproing, splang"
  
nigel = Guitarist() #nigel is an instance of the musician class
nigel.solo(6) #this is how long his solo is
print nigel.sounds #this will print the sounds that are associated 
                    # with nigel as a guitarist