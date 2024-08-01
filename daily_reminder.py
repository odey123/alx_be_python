# daily_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder = f"Reminder: '{task}' is a {priority} priority task"

    match priority:
        case 'high':
            if time_bound == 'yes':
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". Make sure to complete it soon."
        case 'medium':
            if time_bound == 'yes':
                reminder += " that needs to be completed today."
            else:
                reminder += ". Try to complete it in the next few days."
        case 'low':
            if time_bound == 'yes':
                reminder += " that should be completed today."
            else:
                reminder += ". Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority level entered."

    print(reminder)

if __name__ == "__main__":
    main()
