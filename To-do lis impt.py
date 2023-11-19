class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def remove_task(self, task_index):
        try:
            task = self.tasks.pop(task_index)
            print(f"Task '{task['task']}' removed.")
        except IndexError:
            print("Task index out of range.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def mark_as_completed(self, task_index):
        try:
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed.")
        except IndexError:
            print("Task index out of range.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_tasks(self, status=None):
        filtered_tasks = self.tasks if status is None else [task for task in self.tasks if task["completed"] == status]
        if not filtered_tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for idx, task in enumerate(filtered_tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{idx}. [{status}] {task['task']}")

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task['task']},{task['completed']}\n")
            print(f"Tasks saved to '{filename}'.")
        except Exception as e:
            print(f"An error occurred while saving tasks: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    task, completed = line.strip().split(',')
                    self.tasks.append({"task": task, "completed": bool(completed)})
            print(f"Tasks loaded from '{filename}'.")
        except FileNotFoundError:
            print("File not found. Starting with an empty task list.")
        except Exception as e:
            print(f"An error occurred while loading tasks: {e}")


def main():
    todo_list = TodoList()

    while True:
        print("\n==== TO-DO LIST ====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Show All Tasks")
        print("5. Show Pending Tasks")
        print("6. Show Completed Tasks")
        print("7. Save Tasks to File")
        print("8. Load Tasks from File")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(index - 1)
        elif choice == '3':
            index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_as_completed(index - 1)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            todo_list.show_tasks(status=False)
        elif choice == '6':
            todo_list.show_tasks(status=True)
        elif choice == '7':
            filename = input("Enter the file name to save tasks: ")
            todo_list.save_to_file(filename)
        elif choice == '8':
            filename = input("Enter the file name to load tasks: ")
            todo_list.load_from_file(filename)
        elif choice == '9':
            print("Exiting the to-do list app. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
