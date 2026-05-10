'''
Sierra Andreason
IS 303 -A02
Security Access Checker

Goal: Determines access level based on role and clearance

Decision Logic: Different access for admin/employee/visitor, 
modified by clearance level or time of day

Inputs
-Name (string)
-access level (string)
-security code (integer)
-time of day (integer)

Processes: 
- Validate acess level based on role and time of day

Outputs:
-print name, level, time of day and acceptance or denial
-print an error for any invalid inputs

Notes: only works on a 24 hr clock

'''

print("--- SECURITY TERMINAL ---")
name = input("What's your name? ").capitalize()
access_type = input("What's your Clearance Level? Admin/Employee/Visitor? ").lower()
admin_name = "Megan"
correct_admin_code = "7754"
employee_code = "4432"
attempts = 0

#Converting Time-->24hrs
raw_time = input("Current Time (e.g. 9am, 5pm): ").lower().strip()

if "pm" in raw_time:
    hour = int(raw_time.replace("pm", ""))
    if hour != 12:
        hour += 12
elif "am" in raw_time:
    hour = int(raw_time.replace("am", ""))
    if hour == 12:
        hour = 0
else:
    hour = int(raw_time)

#Admin While Loop (for fun) 

if access_type == "admin":
    while attempts < 3:
     input_code = input("Enter Admin Security Code: ")
    
     if admin_name == "Megan" and input_code == correct_admin_code:
        print(f"Welcome, {name.capitalize()}. Access Granted.")
        break
     else:
        attempts += 1
        print(f"Incorrect code. Attempt {attempts}/3.")
        
        if attempts == 3:
            print(f"\n Access Denied.\n{name.capitalize()} has failed to check in three times.") 
            print("A security guard will be sent to your location in 5 minutes.")

elif access_type == "employee":
    input_code = input("Enter Employee Security Code: ")
    if input_code == employee_code:
        print("Access Granted: Welcome, Employee!")
    else:
        print("Access Denied: Invalid Employee Code.")

elif access_type == "visitor":
    if 9 <= hour <= 17:
        print("Access Granted: Welcome, Visitor. Please wear your name tag!")
    else:
        print(f"Access Denied: Visitors are restricted after hours. Please return during open hours! Current hour: {hour}:00")

else:
    print("Error: Unknown Access Level. Please try again. ")
