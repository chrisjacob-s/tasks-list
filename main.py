# Christopher Soriano and Justin Donate
# 4/25/23
# This program allows the user to keep track of their tasks that need to be done.

import check_input
from tasklist import Tasklist

def main_menu():
  '''Displays the main menu and returns the user’s valid input'''
  print("1. Display current task")
  print("2. Mark current task complete")
  print("3. Postpone current task")
  print("4. Add new task")
  print("5. Save and quit")

  menu_selection = check_input.get_int_range("Enter choice: ", 1, 5)
  
  return menu_selection

def get_date():
  '''Prompts the user to enter the year, month, and day and returns the date in the format YYYY/MM/DD'''
  year = check_input.get_int_range('Enter year: ' ,2000,3000)
  month = check_input.get_int_range('Enter month: ', 1, 12)
  day = check_input.get_int_range('Enter day: ', 1, 31)
  
  return f"{year}/{month:02d}/{day:02d}"
 
def get_time():
  '''Prompts the user to enter the hour (military time) and minute and returns the time in the format HH:MM'''
  hour = check_input.get_int_range('Enter hour: ', 0,23)
  minute = check_input.get_int_range('Enter minute: ',0,59)
  
  return f"{hour:02d}:{minute:02d}"

def main():
  task_list = Tasklist()
  play_again = True
  
  while play_again == True:
    print("-Tasklist-")
    print(f"Tasks to complete: {len(task_list)}")
    selection = main_menu()

    # When user inputs 1, it prints the first/current task
    if selection == 1:
      if len(task_list) == 0:
        print("All tasks are completed!")
      else:
        print(task_list.get_current_task())
        
    # When user inputs 2, the current task will be marked complete and deleted from the list.
    # Then the following task will be printed
    elif selection == 2:
      if len(task_list) == 0:
        print("All tasks are completed!")
      elif len(task_list) == 1:
        print("Marking current task as complete:")
        print(task_list.get_current_task())
        task_list.mark_complete()
        print("All tasks are completed!")
      else:
        print("Marking current task as complete:")
        print(task_list.get_current_task())
        task_list.mark_complete()
        print("New current task:")
        print(task_list.get_current_task())
    
    # When user inputs 3, the user will assign a new date and time for the current task.
    # Then the task will be sorted in the list based on the date
    elif selection == 3:
      if len(task_list) == 0:
        print("All tasks are completed!")
      if task_list:
        print("Postponing task: ")
        print(task_list.get_current_task())
        
        print("Enter new due date: ")
        new_date = get_date()
        
        print("Enter new time:")
        new_time = get_time()

        task_list.postpone_task(new_date, new_time)
    
    # When user inputs 4, a new task will be written down along with its new date and time of when to be completed.
    # then it is sorted in the list, task_list will add 1
    elif selection == 4:
      description = input("Enter a task: ")
      date = get_date()
      time = get_time()

      task_list.add_task(description, date, time)
    
    # When user inputs 5, the list will be saved and written in the file and the program will end
    elif selection == 5:
      task_list.save_file()
      break

    print("")


main()