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
    _tasks: dict = {}

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
        return len(self._tasks)

    def __add__(self, other):
        if other is Task:
            self.add_task(other)

    def __sub__(self, other):
        if other is Task:
            self.remove_task(other)

    def log_tasks(self):
        self.update_log()
        self.log.setdefault("tasks", self._tasks)
        self.check_tasks()

        return self.log

    def check_tasks(self):
        true_list = []
        for _task in self._tasks.values():
            true_list.append(_task.completed)

        all_tasks_completed: bool = all(true_list)
        if all_tasks_completed:
            self.completed = True
        else:
            self.completed = False

    def add_task(self, task: Task):
        self._tasks.setdefault(task.id, task)

    def remove_task(self, task: Task):
        self._tasks.pop(task.id)

    def remove_task_by_id(self, task_id: int):
        self._tasks.pop(task_id)

    def get_task(self, task_id: int):
        return self._tasks.get(task_id)

    def get_tasks(self):
        return self._tasks.items()

    def update_task(self, task: Task):
        self._tasks.setdefault(task.id, task)

    def update_log(self):
        for _id, _task in self._tasks.items():
            log: dict = {
                "id": _task.id,
                "mission": _task.mission,
                "completed": _task.completed
            }
            _task.log = log

        log: dict = {
            "id": self.id,
            "mission": self.mission,
            "completed": self.completed
        }
        self.log = log

    def count(self) -> int:
        return len(self._tasks)
