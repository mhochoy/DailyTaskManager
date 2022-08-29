from datetime import date
from datetime import datetime
import pytz

from models.task import Task, Tasks
import settings


def main():
    current_day = date.today()
    timezone = pytz.timezone('America/New_York')
    now = datetime.now(timezone)
    current_time = now.strftime("%I:%M:%S")

    with open(f"{settings.path}My Daily Tasks {current_day}.txt", "w") as f:
        date_string = f"{current_day}\n{current_time}\n\n\n"
        f.write(date_string)
        print(date_string)
        my_tasks: Tasks = settings.saved_tasks.get_tasks()
        for _id, _task in my_tasks:
            task = process_task(_task)

            if task:
                settings.saved_tasks.update_task(task)
                settings.saved_tasks.update_log()
                settings.saved_tasks.log_tasks()
                f.write(f"{task.mission}: {'done' if task.completed else 'not done'}\n")

        f.close()
        print(settings.saved_tasks)
        input("Daily Task Log Finished. Press Enter to exit")


def process_task(task: Task):
    if not task.completed:
        print(f"Have you completed this task yet?: '{task.mission}'\n")
        answer = input()
        if answer.lower() in ['y', 'yes']:
            task.completed = True
            task.update_log()
            return task
        elif answer.lower() in ['n', 'no']:
            task.update_log()
            task.completed = False
            return task
        else:
            return
    else:
        pass


main()
