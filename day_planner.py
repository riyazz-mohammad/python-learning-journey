# Program 10: Day of Week Planner
# Gives schedule based on day

day = input("Enter day of week: ").lower()

if day == "monday":
    print("MONDAY - Start strong!")
    print("Focus: Deep learning session")
    print("Goal: 2 hours of Python practice")
elif day == "tuesday":
    print("TUESDAY - Build momentum!")
    print("Focus: Git and GitHub practice")
    print("Goal: 5 new commits")
elif day == "wednesday":
    print("WEDNESDAY - Midweek grind!")
    print("Focus: Open source exploration")
    print("Goal: Find 5 repos to contribute to")
elif day == "thursday":
    print("THURSDAY - Almost there!")
    print("Focus: Code review and fixing bugs")
    print("Goal: Clean up existing code")
elif day == "friday":
    print("FRIDAY - End strong!")
    print("Focus: Build a mini project")
    print("Goal: Complete one full project")
elif day == "saturday":
    print("SATURDAY - Weekend warrior!")
    print("Focus: First open source contribution")
    print("Goal: Submit one PR")
elif day == "sunday":
    print("SUNDAY - Reflect and plan!")
    print("Focus: Weekly review and journaling")
    print("Goal: Plan next week's goals")
else:
    print("Invalid day! Please enter a valid day of the week")