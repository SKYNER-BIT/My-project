import time

subjects = []
seconds = 0
width = 70

def add_subject():
    subject = input("Enter the subject you will study: ")
    subjects.append(subject)
def add_hour():
    global seconds
    seconds += 3600
    print("1 hours have been added")
def show_subject():
    global subjects
    for i in range(0,len(subjects)):
        for subject in subjects:
            print(f"{i+1}:{subject}")
def remove_subject():
    print("""
==================================================================
==   To remove a subject pick it on index start with 0          ==
==================================================================
""")
    index = int(input("Enter the number of index: "))
    subjects.pop(index)
    
def start_timer():
    global seconds
    for i in range(seconds, -1, -1):
        hour = i // 3600
        min = (i % 3600) // 60
        seconds = i % 60
        timer = f"{hour:02d}:{min:02d}:{seconds:02d}"
        print(f"\r{timer}", end="", flush=True)
        time.sleep(1)
    print("\nTime up!!!")

def save():
    global subjects
    with open("save.txt", "w") as f:
       f.write("\nToday study subject")
       for i, subject in enumerate(subjects):
           f.write(f"\n{i+1} : {subject}\n")
       f.write(f"""
total hours : {(seconds // 3600):02d}:{((seconds % 3600) // 60):02d}:{(seconds % 60):02d}
===============================================================================================
""")
    print("Saved Succefully")
print("""
=============Study=Tracking=App===================
==    0. Quit                                   ==
==    1. add the subject                        ==
==    2. add how many hour you want to study    ==
==    3. Show the subject you have selected     ==
==    4. remove the subject                     ==
==    5. Save your stuff                        ==
==    6. start the timer                        ==
==================================================
""") 
while True:
    option = input("Enter the option: ")
    if option == "0":
        break
    elif option == "1":
        add_subject()
    elif option == "2":
        add_hour()
    elif option == "3":
        show_subject()
    elif option == "4":
        remove_subject()
    elif option == "5":
        save()
    elif option == "6":
        start_timer()
    else:
        "There is no such option"