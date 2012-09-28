from sys import exit
num_women= 0
num_men = 0
num_social = 0
num_facebook = 0
num_hours_social = 0

def leave():
    print("Number of women       : %d" % num_women)
    print("Number of men         : %d" % num_men)
    print("Number on social media: %d" % num_social)
    print("Number on facebook    : %d" % num_facebook)
    print("Number of hours total : %d" % num_hours_social)
    exit()


while True:
    sex = input("Please state your sex (m/f): ")
    if sex == 'm':
        num_men+=1
    elif sex == 'f':
        num_women+=1
    elif sex == 'hade':
        leave()
    else:
        continue
    age = input("Please state your age      : ")
    if age == 'hade':
        leave()
    try:
        if int(age) not in range(16,26):
            print("You are not in our target audience. Thanks for participating")
            continue
    except:
        print("Please don't try to break the survey, bitch")
        continue
    on_social = input("Are you active on a social media site(y/n)?")
    if on_social == 'y':
        num_social+=1
    elif on_social == 'n':
        print("Thank you for participating!")
        continue
    else:
        leave()
    if sex == 'm':
        on_facebook = input("Between 40-45% of Facebooks users are men. Are you one of these(y/n)? ")
    elif sex == 'f':
        on_facebook = input("Between 55-60% of Facebooks users are women. Are you one of these(y/n)? ")
    else:
        leave()
    if on_facebook == 'y':
        num_facebook+=1
    hours_social = input("How many hours do you use on social media a day? ")
    if hours_social == 'hade':
        leave()
    try:
        num_hours_social += int(hours_social)
    except:
        print("You are not in our target audience. Thanks for participating")
        continue
        
    
