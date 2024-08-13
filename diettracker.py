#diet tracker
#Lets you know how much weight you will gain or lose depending on daily caloric intake and exercise

class Diet:
    #diet class to manage and calculate the weight changes based on diet and exercise 
    def __init__(self, breakfast_calories, lunch_calories, dinner_calories, exercise, bmr):
        #Constructing all the attributes and paramters we need for the diet object 
        self.breakfast_calories = breakfast_calories
        self.lunch_calories = lunch_calories
        self.dinner_calories = dinner_calories
        self.exercise = exercise
        self.bmr = bmr
        
    def calorie_deficit(self):
        #Calculating the daily calorie deficit or surplas
        deficit = self.bmr + self.exercise - (self.breakfast_calories + self.lunch_calories + self.dinner_calories)
        return deficit 

#User inputs for dietary and exercise information
breakfast_calories = int(input("How many calories did you have for brekfast? "))     
lunch_calories = int(input("How many calories did you have for lunch? "))     
dinner_calories = int(input("How many calories did you have for dinner? "))
exercise = int(input("How many calories did you burn exercising? "))
bmr = int(input("What is your basic metabolic rate? "))


#Creating an instance of Diet
fitness = Diet(breakfast_calories, lunch_calories, dinner_calories, exercise, bmr)
weekly_deficit = 7 * fitness.calorie_deficit()

#Outputting the predicted weight changes 
if weekly_deficit > 0:
    print(f"You will lose {round(weekly_deficit / 3600, 2)} lbs. per week")
elif weekly_deficit ==0:
    print(f"Your weight will stay the same. ")
else: 
    print(f"You will gain {round(-1 * weekly_deficit /3600, 2)} lbs. per week")
    
         