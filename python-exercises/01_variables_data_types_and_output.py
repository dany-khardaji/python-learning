name = "Dany"                   # Stored text "Dany" under variable "name" 
age = 23                        # Stored integer "23" under variable "age"
favorite_food = "Hummus"        # Stored text "Hummus" under variable "favorite_food"


print("Name:", name)              # Concatentation = connecting strings together            
print("Age: " + str(age))         # Had to convert integer to string in order to print variable 
print(f"Age: {age}")              # Used f-string to print variable without converting to string (Modern Approach)
print(f"Favorite Food: {favorite_food}")