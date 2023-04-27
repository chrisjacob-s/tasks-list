from task import Task

class Tasklist:
  def __init__(self):
    ''' reads in the initial list of tasks from the file ‘tasklist.txt’, constructs the tasks, and stores them in the tasklist. Sort the list. '''
    self._tasklist = []
    with open('tasklist.txt', 'r') as f:
      for line in f:
        desc, date, time = line.strip().split(',')
        new_task = Task(desc, date, time)
        self._tasklist.append(new_task)
    self._tasklist.sort()

  def add_task(self, desc, date, time):
    ''' use the parameters to construct a new task object
  then stores it into the tasklist. Sort the list after the task is added. '''
    new_task = Task(desc, date, time)
    self._tasklist.append(new_task)
    self._tasklist.sort()
    
  def get_current_task(self):
    ''' return the first task object. '''
    return self._tasklist[0]
    
  def mark_complete(self):
    ''' remove the first task from the tasklist and return it. '''
    return self._tasklist.pop(0)
    
  def postpone_task(self, date, time): 
    ''' remove the first task from the tasklist. Use its description, the new date, and the new time to construct a new task. Add that task to the tasklist. Sort the list. '''
    desc = self._tasklist[0].desc
    new_task = Task(desc, date, time)
    self._tasklist.pop(0)
    self._tasklist.append(new_task)
    self._tasklist.sort()
    
  def save_file(self):
    '''– loop through the list and overwrite the contents of the file with the contents of the tasklist using the repr method in the Task class. '''
    with open('tasklist.txt', 'w') as f:
      for task in self._tasklist:
        f.write(repr(task) + '\n')

  def __len__(self) :
    ''' return the number of Task objects in the tasklist. '''
    return len(self._tasklist)

  def __iter__(self):
    ''' initialize the iterator attribute and return self. '''
    self._n = 0
    return self

  def __next__(self):
    ''' iterate the iterator one position at a time. Raise a StopIteration if the iterator reaches the end of the tasklist, otherwise return the Task object at the iterator’s current position. '''
    self._n += 1
    if self._n >= len(self._tasklist):
      raise StopIteration
    else:
      return self._tasklist[self._n]