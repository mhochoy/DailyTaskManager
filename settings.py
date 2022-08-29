from models.task import Tasks, Task

task_one = Task(0, "Do something")
task_two = Task(1, "Do another thing")

_tasks = [task_one, task_two]


path = "C:\\Users\\Michael\\Desktop\\Documents\\Tasks\\"
saved_tasks: Tasks = Tasks(0, "Complete these missions", _tasks)