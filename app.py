
from datetime import datetime
from typing import TextIO

import pytz

from models.task import Task, Tasks
import settings
import helpers


def main():
    done = False
    day = helpers.get_date()
    time = helpers.get_time()
    file_name = "My Daily Tasks"
    file_path = f"{settings.path}{file_name} {day}.txt"
    file = open(file_path, "w")
    while not done:
        with file:
            date_string = f"{day}\n{time}\n\n\n"
            file.write(date_string)
            print(date_string)

            print("Welcome to your Daily Task Manager. What do you want to do?")
            decision = input("run/create/quit:   ")
            handle_menu(decision, file)

            print(settings.saved_tasks)

    file.close()
    input("Daily Task Log Finished. Press Enter to exit")


def handle_menu(decision: str, f: TextIO):
    if decision == "run":
        run(f=f)
    if decision == "create":
        mission = input("What task do you want to complete?:    ")
        task: Task = Task(settings.saved_tasks.count() + 1, mission)
        settings.saved_tasks.add_task(task=task)
        settings.saved_tasks.update_log()
    if decision == "quit":
        done = True

    else:
        print(f"'{decision}' isn't a valid command.\n")


def run(f: TextIO):
    my_tasks: Tasks = settings.saved_tasks.get_tasks()
    for _id, _task in my_tasks:
        task = process_task(_task)

        if task:
            settings.saved_tasks.update_task(task)
            settings.saved_tasks.update_log()
            settings.saved_tasks.log_tasks()
            f.write(f"{task.mission}: {'done' if task.completed else 'not done'}\n")


def process_task(task: Task):
    if not task.completed:
        print(f"Have you completed this task yet?: '{task.mission}'\n")
        answer = input()
        if answer.lower() in ['y', 'yes']:
            task.completed = True
            return task
        elif answer.lower() in ['n', 'no']:
            task.completed = False
            return task
        else:
            return
    else:
        pass


main()
