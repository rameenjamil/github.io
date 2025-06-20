import datetime

def user_mood():
    mood= input("How are you feeling today? \n")
    date= datetime.datetime.now().strftime("%d-%m-%Y")
    with open("user_mood.txt" , "a") as file:
        file.write(f"{date}, {mood} \n")
    print("Your mood have been saved!")

def view_mood():
    try:
        with open("user_mood.txt","r") as file:
            print("\nMood History:\n")
            for line in file:
                date, mood = line.strip().split(", ", 1)  # Split on first comma only
                print(f"Date: {date} - Mood: {mood}")
    except FileNotFoundError:
        print("No mood log found.")
while True:
    select = input("Would you like to:\nA.Enter your mood\nB.View history\nC.Exit\n(Please type A/B/C)\n").lower()
    if select == "a":
        user_mood()
    elif select == "b":
        view_mood()
    elif select == "c":
        break
    else:
        print("Choice not valid.\nPlease select the right option\n")
