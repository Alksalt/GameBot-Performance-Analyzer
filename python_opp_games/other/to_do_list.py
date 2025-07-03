from datetime import datetime
class Task:
    def __init__(self, task_name, description, deadline):
        self._task_name = task_name
        self.description = description
        self.deadline = deadline

    def __str__(self):
        return f"{self.task_name} with description: {self.description} has to be done until {self.deadline}"
    @property
    def task_name(self):
        return self._task_name
    @task_name.setter
    def task_name(self, name):
        self._task_name = name

class TaskManager:
    def __init__(self):
        self.all_tasks = []
        self.finished_tasks = []

    def add_task(self, task):
        self.all_tasks.append(task)
        print(f"{task.task_name} was successfully added to the list")
        return self.all_tasks

    def remove_task(self, task):
        if task in self.all_tasks:
            self.all_tasks.remove(task)
            print(f"{task.task_name} was successfully removed from the list")
            return self.all_tasks
        else:
            print("The task was not found.")

    def tick_as_done(self, task):
        if task in self.all_tasks:
            self.finished_tasks.append(task)
            self.all_tasks.remove(task)
            for i in self.finished_tasks:
                print(f"{i.task_name} task was finished")
            return self.finished_tasks
        else:
            print("The task is not in the to do list.")

    def check_deadline(self, task):
        current_time = datetime.now().date()
        if task in self.all_tasks:
            new_task = datetime.strptime(task.deadline, "%Y-%m-%d").date()
        #for t in self.all_tasks:
        #    if task == t:
        #        deadline = datetime.strptime(t.deadline, "%Y-%m-%d").date()
            if new_task < current_time:
                return f"Deadline was expired, the last day was {task}"
            elif new_task == current_time:
                return "Oh, This the last day before the deadline is expired. HURRY UP!"
            else:
                time_left = new_task - current_time
                return f"You have {time_left}"
        else:
            print("The task was not found.")


    def reminder(self):
        deadlines = []
        current_time = datetime.now().date()
        for d in self.all_tasks:
            deadlines_str = datetime.strptime(d.deadline, "%Y-%m-%d").date()
            if deadlines_str == current_time:
                deadlines.append(d)

        # Move return outside loop
        if deadlines:
            all_deadlines = ", ".join(str(i) for i in deadlines)
            return f"Some of your tasks are almost expired! Hurry up! Task(s): {all_deadlines}"
        else:
            return "No tasks are expiring today."


task1 = Task("Laundry", "have to go to laundry", "2024-11-01")
task2 = Task("Gym", "gym on Sunday", "2024-10-20")
task3 = Task("Meeting", "meeting with a friend", "2024-10-18")
task4 = Task("Gym", "gym on Friday", "2024-10-18")
task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)
task_manager.add_task(task4)
task_manager.remove_task(task1)
task_manager.remove_task(task1)
print(task_manager.check_deadline(task2))
print(task_manager.check_deadline(task4))
task_manager.tick_as_done(task2)
print(task_manager.reminder())
