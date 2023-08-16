#Personalized migraine program.

def main():
    print("Welcome to your personal Migraine detector Vanina!")
    answer = input("What level of pain are you feeling today (from 1-10)? ")

    try:
        pain_level = int(answer)

        if pain_level == 1:
            print("Please eat your three meals, have a snack every three hours, take your daily vitamins and pills, and drink a lot of water!")
        elif pain_level == 2:
            print("You do not need to take any of your preventive pills, just stay hydrated and avoid bright light.")
        elif 3 <= pain_level <= 6:
            print("You might want to take your Omeprazol and no more than 2 Advils.\nVanina please remember to stay hydrated and try to lay down as much as you can.")
        elif 7 <= pain_level <= 10:
            greateranswer = input("Did you eat today (Yes/No)? ")
            if greateranswer == "Yes":
                print("Take Diclofenac and if the pain persists throughout the day you can take a second Diclofenac.\nDo not forget to take Omeprazol before.")
            elif greateranswer == "No":
                nextanswer = input("Did you sleep 8-10 hours last night (Yes/No)? ")
                if nextanswer == "Yes":
                    print("You must feel nausea since you did not eat, please make sure to eat and take Metoclopramide, you can take three pills throughout the day if the pain persists.\nDo not forget to take Omeprazol before.")
                elif nextanswer == "No":
                    otheranswer = input("Did you take your daily vitamins and preventive pills right after waking up (Yes/No)? ")
                    if otheranswer == "Yes":
                        print("You must be tired and that is a trigger for your migraines.\nPlease go to sleep and if you can not sleep please take a Naproxen, this will help your pain and it will allow you to rest.")
                    elif otheranswer == "No":
                        print("You have not eaten, you have not slept the hours you need to sleep, and you have not taken your vitamins and preventive pills as you should.\nPlease remember to do this.\nI can imagine the pain is unbearable. You can take Naratriptan.\nDo not forget to take Omeprazol before.")
                    else:
                        print("Invalid response.")
                else:
                    print("Invalid response.")
            else:
                print("Invalid response.")
        else:
            print("Please enter a valid pain level between 1 and 10.")
    except ValueError:
        print("Please enter a valid pain level between 1 and 10.")

if __name__ == "__main__":
    main()
