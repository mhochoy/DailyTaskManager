from typing import Optional


class Task:
    id: int = 0
    completed: bool = False
    mission: str = ""

    log: dict = {
        "id": id,
        "mission": mission,
        "completed": completed
    }

    def __init__(self, _id, _mission):
        self.id = _id
        self.mission = _mission
        self.update_log()

    def __repr__(self):
        return self.log.__str__()

    def __str__(self):
        return self.log.__str__()

    def update_log(self):
        log: dict = {
            "id": self.id,
            "mission": self.mission,
            "completed": self.completed
        }

        self.log = log


class Tasks(Task):
    tasks: dict = {}

    def __init__(self, _id: int, _mission: str, _tasks):
        super().__init__(_id=_id, _mission=_mission)
        if isinstance(_tasks, list):
            for task in _tasks:
                self.add_task(task=task)
        elif isinstance(_tasks, Task):
            self.add_task(task=_tasks)
        else:
            raise TypeError("'_tasks' argument can only be of 'list' type or a 'Task' type.")

    def __str__(self):
        return self.log_tasks().__str__()

    def __repr__(self):
        return self.log_tasks().__str__()

    def __len__(self):
        return len(self.tasks)

    def __add__(self, other):
        if other is Task:
            self.add_task(other)

    def __sub__(self, other):
        if other is Task:
            self.remove_task(other)

    def log_tasks(self):
        self.update_log()
        self.log.setdefault("tasks", self.tasks)

        return self.log

    def add_task(self, task: Task):
        self.tasks.setdefault(task.id, task)

    def remove_task(self, task: Task):
        self.tasks.pop(task.id)

    def remove_task_by_id(self, task_id: int):
        self.tasks.pop(task_id)

    def get_task(self, task_id: int):
        return self.tasks.get(task_id)

    def get_tasks(self):
        return self.tasks.items()

    def update_task(self, task: Task):
        self.tasks.setdefault(task.id, task)


# task_one = Task(0, "Do something")
# task_two = Task(1, "Do another thing")
#
# tasks = [task_one, task_two]
#
# my_tasks = Tasks(0, "Complete these tasks before 3 o'clock", tasks)
#
# print(my_tasks)
