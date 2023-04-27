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
  print("-Tasklist-")
  print(f"Tasks to complete: {len(task_list)}")

  

main()