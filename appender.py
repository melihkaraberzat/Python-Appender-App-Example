
file = open("inputFile.txt", "r")
x = 0
içerik = file.read()
Lines = içerik.split("\n")
x = len(Lines) -1  # boş satırı da saydığı için -1 yaptık 


print("Hello,there are " + str(x) + " entries have been entered.")
answer = input("Would you like to enter a new one? ")

while True: 
    if answer == "yes":
        name = str(input ("Enter name "))
        surname = str(input ("Enter surname "))
        age =int(input("Enter age "))
        idnumber =int(input("Enter identity number "))
        income =int(input("Enter the amount of income "))
        debt =int(input("Enter the amount of debt "))
        multiplier =float(input("Enter the multiplier "))
        print(name,surname,age,idnumber,income,debt,multiplier)
        with open ('inputFile.txt','a') as f:
            f.write(str(name)+',' ) 
            f.write(str(surname)+ ',')
            f.write(str(age)+ ',')
            f.write(str(idnumber)+ ',')
            f.write(str(income)+ ',')
            f.write(str(debt)+ ',')
            f.write(str(multiplier))   
            f.write("\n")
        x = x+1
    elif answer != "no" :
        break
    else:
        print("Your answer is invalid please try again.")
    print ("Hello,there are " + str(x) + " entries have been entered.")
    answer = input("Would you like to enter a new entry? ")
    
