# To-Do List Application
  ### Video Demo:  https://www.youtube.com/watch?v=Ey6fFEDn2Hw
## Description:
    
This is a Python-based console application for managing a personal To-Do list. The application allows users to create, modify, and manage tasks with associated due dates, and it features various functionalities to help track task completion status.

## Key Features
- **Add Tasks**: Users can add new tasks with an associated deadline.
- **Modify Tasks**: Users can update the task description or change the due date.
- **Task Completion**: Mark tasks as complete or incomplete. Completed tasks are displayed with a green checkmark (:heavy_check_mark:), while overdue tasks are shown with a red cross (:x:).
- **Display Tasks**: Tasks are displayed in a sorted list by due date, using colored text to indicate their status:
  - :heavy_check_mark: **Green** for completed
  - :x: **Red** for overdue
  - :yellow_circle: **Yellow** for pending tasks
- **Save/Load Tasks**: The application saves the current to-do list to a CSV file and loads it upon startup, ensuring task data persists across sessions.
- **Command Menu**: An interactive menu allows users to add, remove, edit, mark, or unmark tasks, as well as save and exit the program.

## How It Works
1. The application starts by loading tasks from a `save.csv` file if available.
2. The user is presented with a menu to manage tasks.
3. Each task includes an activity description and a deadline (in `mm/dd/yyyy` format).
4. Available commands:
   - `a`: Add a new task
   - `r`: Remove an existing task
   - `ct`: Change a task’s deadline
   - `ca`: Change a task’s description
   - `mc`: Mark a task as complete
   - `mu`: Mark a task as incomplete
   - `s`: Save tasks to the CSV file
   - `e`: Exit without saving
   - `es`: Exit with saving

## Dependencies
- **emoji**: Used to display checkmarks and cross symbols for task statuses.
- **csv**: Handles reading and writing tasks to a CSV file for persistence.

## Installation
Clone the repository and install the required dependencies using `pip`:

```bash
git clone https://github.com/your-username/todo-list-app.git
cd todo-list-app
pip install -r requirements.txt
