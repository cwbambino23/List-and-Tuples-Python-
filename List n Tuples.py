             #List and Tuples 

month = ("Jaunuary", "Febuary", "March", "April", "May", "June", "July", "August ", "Seoptember", "October", "November", "December")      #List of names stored in friends 
birthday = input ("Enter your birthday in the formatt of DD-MM-YYYY: ")       #user enters their birthday in the format like XX-XX-XXXX

index = int(birthday[3:5]) - 1                  #Convert to interger to use use as an index; subtract 1 because the index start at 0 
bd_month = month[index]                         #Whatever the index is relates to the biorthday month 

print ("You was born on", bd_month )            #print the month of the persomn that the user input sq


           #Ask the user 
           
friends = ["Caleb", "Yoan", "Jered", "Samira"]       #List of names stored in friends 
user = input("Enter your friends name ")             #user enters a name 

friends.append(user)                                 #Modify the list by adding the string at the emd of the list  
print("The new list is....", friends)                #Display the new list with the user input at the end of the list 