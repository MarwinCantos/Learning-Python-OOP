class Menu:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_task(self):
        return self.tasks

    def mark_complete_task(self, num):
        if 0 <= num < len(self.tasks):
            self.tasks[num]["completed"] = True
            return True
        return False

    def remove_task(self, num):
        if 0 <= num < len(self.tasks):
            return self.tasks.pop(num)
        return None
