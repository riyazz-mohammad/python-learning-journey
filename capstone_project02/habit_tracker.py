import datetime as datetime
import json

habit=['Exercise','Studying','Playing']
habit_palnning={}
daily_progress={}
def display_habit():
   for i,item in enumerate(habit,1):
      print(f"{i}.{item}")
def display():
   print("You can add habit(1) and You need to plan habit(2)!")
   
def get_date():
   return datetime.datetime.now()

def add_habits():
    display_habit()
    ha_bit=input("Enter the Habit:")
    if ha_bit not in habit:
      habit.append(ha_bit)
      print(f"{ha_bit} successfully added!")
      return
    print(f"{ha_bit} already in list!")

def planning():
  
   
   while True:
      for i,hab in enumerate(habit,1):
         print(f"{i}.{hab}")

      try:
         print("Habit Tracking Set ..")
         choice=int(input("Enter the Choice: or Enter 0 to exit!"))
         if choice==0:
            break
         if 1<=choice<=len(habit):
            hab=habit[choice-1]
            comment=input(f"Do you want to add something({hab}) or press enter!")
            habit_palnning[hab]={
               'name':hab.lower().strip(),
               'date':get_date().isoformat(),
               'status':'incomplete',
               'comment':comment or 'No Comment'
            }
            print("Planned Successfully!")
         else:
            print("\n Invalid Choice!")
      except ValueError:
         print("Invalid input!")


def mark_complete():
   if not habit_palnning:
      print("No habits have been Tracked!")
      return
   print("Tracked habits..")
   for key,value in habit_palnning.items():
      print(f"{value['name']}")
      
   try:
      
      habi_t=input("Enter the Habit name want to mark complete!").lower().strip()
      found=False
      for key,value in habit_palnning.items():

         if habi_t==value['name']:
            value['status']='completed'
            print("Marked successfully!")
            found=True
            break

      if not found:
         print("Habit not found!")
         return

      # When user marks "Exercise" complete today
      today =datetime.date.today().strftime("%Y-%m-%d")

      if today not in daily_progress:
         daily_progress[today] = []
      if habi_t not in daily_progress[today]:
         daily_progress[today].append(habi_t)
         

   except ValueError:
      print("Invalid input!")
   

def view_today():
   today=get_date()
   print(f"Habit for {today.strftime('%A, %B %d, %Y')}")
   print("-"*40)
   if not  habit_palnning:
      print("No habits to track!")
      return
   for habit_key, habit_info in habit_palnning.items():
        # Get streak for this habit
        streak = calculate_streak(habit_info['name'])
        
        # Status symbol
        status_symbol = "✅" if habit_info['status'] == 'completed' else "⬜"
        
        print(f"{status_symbol} {habit_info['name'].title():<15} "
              f"Status: {habit_info['status']:<12} "
              f"🔥 Streak: {streak} days")
        
        if habit_info['comment'] != 'No Comment':
            print(f"   💬 {habit_info['comment']}")
   print("-"*40)
 
   completion_percentage()

   print("-"*40)


def completion_percentage():
   count=0
   for i, j in habit_palnning.items():
      if j['status']=='completed':
         count+=1
   print(f"The Completion percentage:{count/len(habit_palnning)*100:.1f}%")

def calculate_streak(habit_name):
   if not daily_progress:
      return 0
   today=datetime.date.today()
   current_streak=0
   check_date=today

   while True:

     
        # Convert check_date to string format
      date_string = check_date.strftime("%Y-%m-%d")
        
        # Check if this date exists in daily_progress
      if date_string in daily_progress:
            if habit_name in daily_progress[date_string]:
                current_streak += 1
                # Check previous day
                check_date = check_date - datetime.timedelta(days=1)
            else:
                # Habit wasn't done on this day - streak breaks
                break
      else:
            # No record for this day - streak breaks
            break

   return current_streak

def save_data():
    data = {
        "habits": habit,
        "progress": daily_progress,
        "habit_planning":habit_palnning
        
    }
    try:

      with open('habit_tracker_data.json','w') as file:
      
         json.dump(data,file,indent=4)
      print("Data saved successfully!")
    except Exception as e:
        print(f"Error saving data:{e}")

def load_data():
    global habit,habit_palnning,daily_progress

    try:

        with open('habit_tracker_data.json','r') as file:
            data=json.load(file)
            habit=data.get('habits',[])
            habit_palnning=data.get('habit_planning',{})
            daily_progress=data.get('progress',{})

        print("Data loaded successfully!")
        print(f"Loaded {len(habit_palnning)} transactions")

    except FileNotFoundError:
        print("No saved data found. Starting fresh!")

    except Exception as e:
        print(f"Error loading data:{e}")




while True:
    print("1. Add Habit")

    print("2. Plan Habit")
    print("3. Mark Complete")
    print("4. View Today")
    print("5.Save Data")
    print("6.Load data")
    print("7. Exit")
    display()
    print('-'*40)
    try:
        choice=int(input("enter the choice:"))
        if choice==1:
         add_habits()
        elif choice==2:
             planning()
        elif choice==3:
            mark_complete()
        elif choice==4:
            view_today()
        elif choice==5:
           save_data()
        elif choice==6:
           load_data()
        elif choice==7:
           exit()
    except ValueError:
        print("Invalid choice! or plan habit first!")





      

      
         
      

  


    

  
    
   
    




    
   

    