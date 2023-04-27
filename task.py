class Task:
  '''Represents a task that needs to be done on a specific day and time
  Attributes: 
    description (str): description of task
    date (str): due date of task; formatted YYYY/MM/DD
    time (str): time task is due; formatted HH:MM
  '''

  def __init__(self, desc, date, time):
    '''Sets the task's description, date, and time'''
    self._desc = desc
    self._date = date
    self._time = time

  @property
  def description(self):
    '''Returns the task's description''' 
    return self._desc

  def __str__(self): 
    '''Returns description with the date and time'''
    return str(self._desc) + " - Due: " + str(self._date) + " at " + str(self._time)

  def __repr__(self):
    '''Returns a string used to write the task to the file'''
    return f'{self._desc},{self._date},{self._time}'

  def __lt__(self, other):
    '''Returns true if the self task is less than the other task'''
    # Checks if the years, dates, and times are equivalent; if they are then check if the self._desc is less than the other task. If they aren't check which is less than which
    if self._date[0:4] == other._date[0:4]:
      if self._date[5:7] == other._date[5:7]:
        if self._date[8:10] == other._date[8:10]:
          if self._time[0:2] == other._time[0:2]:
            if self._time[3:5] == other._time[3:5]:
              return self._desc < other._desc
            else: 
              return self._time[3:5] < other._time[3:5]
          else: 
            return self._time[0:2] < other._time[0:2]
        else: 
          return self._date[8:10] < other._date[8:10]
      else:
        return self._date[5:7] < other._date[5:7]
    else:
      return self._date[0:4] < other._date[0:4]
