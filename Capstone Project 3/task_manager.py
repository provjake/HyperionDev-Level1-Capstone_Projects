#=====importing libraries===========
# iporting the os module
import os

#=====Functions==============
def reg_user(user):
    """This function is used to register a new user by admin"""

    if user == 'admin':
        # new user username, no case sensitivity
        new_user = input("Enter a username: ").lower()

        # if username already exists
        while new_user in user_cred.keys():

            print("The username already exists. \n")

            new_user = input("Enter a different username: ").lower()

        # new user password
        new_pass = input("Enter password: ")

        # confirming password
        confirm_pass = input("Confirm password: ")

        # checking if passwords match
        if new_pass == confirm_pass:

            # adding credentials to user.txt
            user_file.write("\n" + new_user + ", " + new_pass)

            # adding user to dictionary
            user_cred[new_user] = new_pass

        else:
            print("The passwords do not match! \n")
            
    else:
        print("Only admin can register a new user.")

def add_task(user):
    """This function is used to add a task to the task manager system"""

    task_file = open('tasks.txt','a') # open in append mode

    task = user # string to build task

    # list of required info
    req_list = [
        'Enter task tile: ','Describe task: ','Enter due date (eg 29 Oct 2021): ',
        'Enter current date (eg 29 Oct 2021): ','Task complete?: '
        ]
    
    # building task string
    for request in req_list:

        task += ", " + input(request) # getting user input

    # adding task to file
    task_file.write(f"\n{task}") 
    
    task_file.truncate()
    task_file.close() # closing file

def view_all(line,task_number):
    """This function is used to view all the available tasks in the task manager"""
    
    line = line.strip()
    
    line = line.split(', ') # Seperating information

    display = "" # output string
    
    headings = [
        'Person responsible','Title','Description',
        'Due date','Date task was assigned','Task complete?'
        ]
    
    for index in range(len(headings)):
        # space to align the info when displaying it
        space = " "*(23 - len(headings[index]))

        # building the output string
        display += f"{headings[index]} {space}: {line[index]} \n"
    
    # displaying task
    print(f"Task {task_number}")
    print(display) # displaying contents of each task

def update_task(line,new_line):
    """This function is for updating task information"""

    task_file = open('tasks.txt','r') # open task file

    tasks = [] # list to store tasks

    for old_line in task_file: 

        # looking for the updated task
        if old_line == line:

            tasks.append(new_line) # replacing updated task

        else:

            tasks.append(old_line) # keeping unupdated tasks

    task_file.close() # closing file

    task_file = open('tasks.txt','w') # open task file

    # rewriting task.txt with the new task info
    for line in tasks:

        if line[-1] == '\n': 

            task_file.write(line[:len(line)-1] + "\n") 

        else:
            task_file.write(line + "\n")

    task_file.close() # closing file

def view_mine():
    """This function is to view tasks assigned to a specific user"""

    tasks = [] # list to store user tasks

    # keeping track of task number
    task_number = 0

    for line in task_file:
        
        if line[:line.index(',')] == username: # confirminig username

            task_number += 1 # updating task number
            
            # storing users tasks in a list 
            tasks.append(line)
            
            view_all(line,task_number) # viewing tasks

    # asking the user to choose a task to view

    if task_number == 0:
        print("You have no assigned tasks. \n")

    else:
        print("Select a task by number (e.g 1) or -1 for main menu")
        view_task = int(input("Enter task number: "))

        if view_task == -1:
            pass # do nothing

        else:

            line = tasks[view_task-1].strip() # getting task

            line_list = line.split(',') # task list
            
            # possible yes combination that can read from file
            yes_list = [' Yes\n',' yes\n']

            if line_list[5] in yes_list:

                line_list[5] = " Yes" # removing new line
            
            else:
                line_list[5] = " No" # removing new line

            # possible yes combination that can read from file
            yes_list = [' Yes',' yes']

            # viewing the selected task
            view_all(line,view_task)

            # Edit task
            print("Enter - mark as complete, edit task or pass")
            complete = input("Update task: ").lower()

            if complete == "mark as complete":

                line_list[-1] = " Yes" # changing No to Yes

                line = ",".join(line_list)

                update_task(tasks[view_task-1],line)
            
            elif complete == "edit task" and line_list[-1] not in yes_list:

                print("Enter what to update: Username or Due date")
                choice = input("Enter a choice: ").lower()

                # updating username
                if choice == 'username':

                    line = tasks[view_task-1].split(',')

                    # Getting new username
                    change = input("Enter new responsible person: ").lower()

                    line[0] = change # updating username

                    line = ",".join(line)

                    # upadating task in file
                    update_task(tasks[view_task-1],line)

                # updating due date
                elif choice == 'due date':
                    line = tasks[view_task-1].split(',')
                
                    # getting new due date
                    change = input("Enter new due date (eg 09 Nov 2021): ")

                    line[3] = " " + change # updating due date

                    line = ",".join(line)

                    # updating due date in file
                    update_task(tasks[view_task-1],line)

                else:
                    print("You have entered a wrong choice.")

            # preventing editing of a completed task
            elif line_list[-1] in yes_list:
                print("Task is completed and cannot be edited.")
                
            else:
                print("Incorrect input.")

def user_count():
    """This function is to count the number of users in the task manager"""

    user_file = open('user.txt','r') 

    # initializing number of users storage
    number_of_users = 0

    #checking if file is empty
    if os.stat('user.txt').st_size == 0:
        
        # displaying user stats
        return f"Total number of users : {number_of_users} \n"

    else:
        # counting number of users
        for line in user_file:
            
            # updating number of users
            number_of_users += 1

        return f"Total number of users : {number_of_users} \n"
    
    user_file.close()

def task_count():
    """This function is for counting the number of tasks in the task manager"""

    task_file = open('tasks.txt','r')
    
    # initalizing task number
    number_of_tasks = 0

    #checking if file is empty
    if os.stat('tasks.txt').st_size == 0:
        
        # displaying user stats
        return f"Total number of tasks : {number_of_tasks} \n"

    else:
        # counting number of tasks
        for line in task_file:
            
            # updating number of tasks
            number_of_tasks += 1

        return f"Total number of tasks : {number_of_tasks} \n"
    
    task_file.close()

def task_overview(current_date,months):
    """This function is for generating a report on the tasks availabe"""

    current_date = current_date.split(' ') # splitting day,month,year
    
    # initialising overdue tracking variable
    overdue = 0

    task_stat = open('task_overview.txt','w') # creating file

    task_stat.write(task_count()) # total number of tasks
    
    # openning file
    task_file = open('tasks.txt','r')
    
    # tracking completed and uncompleted tasks 
    completed = 0 
    uncompleted = 0 

    count = 0 # counting number of tasks

    for line in task_file:

        count += 1 # updating number of tasks

        line = line.strip()

        line = line.split(", ") # list of task information

        line[-1] = line[-1].strip() # removing new line
        
        # counting completed tasks
        if line[-1] in ['Yes','yes']:
            completed += 1
        
        else:
            uncompleted += 1 # counting incomplete tasks
            
            # due date day - current day date
            day = int(line[3][:2]) - int(current_date[0])

            # previuos due months - current month number
            month = months[line[3][3:6].lower()] - months[current_date[1].lower()]

            # previous year - current year
            year = int(line[3][7:]) - int(current_date[2])
            
            # When the year of due date has passed
            if year < 0:
                overdue += 1
            
            # when the month of due date has passed in same year
            elif month < 0 and year == 0:
                overdue += 1
            
            # when day of due date has passed in the same month and year it was due
            elif day < 0 and month == 0 and year == 0:
                overdue += 1

            else:
                pass # do nothing 
    
    incomplete = round((uncompleted/count)*100,2) # percent of incomplete tasks
    overdue_percent = round((overdue/count)*100,2) # percent of incomplete overdue tasks
    
    # writing task stats into the new file
    task_stat.write(f"Total number of completed tasks: {completed}" + "\n")
    task_stat.write(f"Total number of incomplete tasks: {uncompleted}" + "\n")
    task_stat.write(f"Total number of overdue tasks: {overdue}" + "\n")
    task_stat.write(f"Percentage of incomplete tasks: {incomplete}%" + "\n")
    task_stat.write(f"Percentage of overdue tasks: {overdue_percent}%" + "\n")
    
    # closing files
    task_file.close()
    task_stat.close()

def user_overview(current_date,months):
    """This function is for generating a report on the users availabe"""

    current_date = current_date.split(' ') # splitting day,month,year

    user_stat = open('user_overview.txt','a') # creating file

    user_stat.write(user_count()) # total number of users
    user_stat.write(task_count() + "\n") # total number of tasks

    # closing file
    user_stat.close()
    
    for user in list(user_cred.keys()):

        task_file = open('tasks.txt','r')
        user_stat = open('user_overview.txt','a')
        
        count = 0 

        # initialising overdue tracking variable
        overdue = 0

        user_tasks = 0 # tracking users tasks

        # tracking completed and uncompleted tasks
        completed = 0 
        uncompleted = 0 
        
        for line in task_file:
            
            line = line.strip() # removing new line
            
            count += 1

            line = line.split(", ") # list of task information

            # confirming task belongs to user
            if user == line[0]:
                user_tasks += 1 # tracking user tasks

                # counting completed tasks

                if line[5] in ['Yes','yes']:
                    completed += 1

                else:
                    uncompleted += 1 # counting incomplete tasks

                    # due date day - current day date
                    day = int(line[3][:2]) - int(current_date[0])

                    # previuos due months - current month number
                    month = months[line[3][3:6].lower()] - months[current_date[1].lower()]

                    # previous year - current year
                    year = int(line[3][7:]) - int(current_date[2])
            
                    # When the year of due date has passed
                    if year < 0:
                        overdue += 1
            
                    # when the month of due date has passed in same year
                    elif month < 0 and year == 0:
                        overdue += 1
            
                    # when day of due date has passed in the same month and year it was due
                    elif day < 0 and month == 0 and year == 0:
                        overdue += 1

                    else:
                        pass # do nothing

        if user_tasks != 0:

            incomplete = round((uncompleted/user_tasks)*100,2) # percent of incomplete tasks
            overdue_percent = round((overdue/user_tasks)*100,2) # percent of incomplete overdue tasks
            user_tasks_percent = round((user_tasks/count)*100,2) # percent of user tasks
            complete = round((completed/user_tasks)*100,2) # percent of incomplete tasks
    
            # writing task stats into the new file
            user_stat.write(f"---------Task report for {user}----------- \n")
            user_stat.write(f"Total number of user tasks: {user_tasks}" + "\n")
            user_stat.write(f"Percentage of assigned tasks: {user_tasks_percent}%" + "\n")
            user_stat.write(f"Percentage of completed tasks: {complete}%" + "\n")
            user_stat.write(f"Percentage of incomplete tasks: {incomplete}%" + "\n")
            user_stat.write(f"Percentage of overdue tasks: {overdue_percent}%" + "\n")
            user_stat.write("\n")
        
        # closing file
        user_stat.close()
        task_file.close()
        
def display_reports():
    """This function is for displaying the user and task reports"""
    
    # opening files
    task_overview = open('task_overview.txt','r')
    user_overview = open('user_overview.txt','r')
    
    print("Task overview report \n")
    print(task_overview.read()) # reading and displaying task report

    print()
    
    print("User overview report \n")
    print(user_overview.read()) # reading and displaying user report
    
    # closing files
    task_overview.close()
    user_overview.close()

#====Login Section====
# opening and reading the user.txt
user_info = open('user.txt','r')

# credentials dictionary
user_cred = {}

# empty user.txt file
if os.stat('user.txt').st_size == 0:

    print("No user information available.")
    user_info.close() # closing file

else:
    # iterating through file lines
    for line in user_info:

        #removin \n from password
        if line[-1] == "\n":
            # getting username
            username = line[:line.index(",")]

            # getting password
            password = line[line.index(" ")+1:line.index("\n")]

            # storing credentials
            user_cred[username] = password
        
        else:
            # getting username
            username = line[:line.index(",")]

            # getting password
            password = line[line.index(" ")+1:]

            # storing credentials
            user_cred[username] = password
        
    user_info.close() # closing file

    # getting username, no case sensitivity 
    username = input("Enter your username: ").lower()

    # getting password
    password = input("Enter your password: ")

    #===The code to perform tasks===
    while True:
        # checking if username is correct
        not_found = username not in user_cred

        # confirming credentials
        while not_found or user_cred[username] != password:

            # invalid username
            if not_found:

                print("Invalid user credentials.")
                
                # getting username, no case sensitivity 
                username = input("Enter your username: ").lower()
                
                # getting password
                password = input("Enter your password: ")
            
            # invalid password
            else: 
                print("Invalid password.")
                
                # getting password
                password = input("Enter your password: ")
            
            # username determines if password is correct
            not_found = username not in user_cred
        
        # user menu coneverted to lower case.
        if username == 'admin':
            # admin user menu
            menu = input('''Select one of the following Options below:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - view my task
            gr - generating reports
            vs - view statistics
            e - Exit\n: ''').lower()

        else:
            # general user menu
            menu = input('''Select one of the following Options below:
            a - Adding a task
            va - View all tasks
            vm - view my task
            e - Exit\n: ''').lower()
        
        # registering a new user
        if menu == 'r':
        
            user_file = open('user.txt','a') # opening file

            reg_user(username) # registration fuction call

            user_file.close() # closing file
            
        # adding and assigning a task
        elif menu == 'a':

            # user responsible
            user_responsible = input("Enter the responsible person: ")
            
            # checkin if entered user exists
            if user_responsible in user_cred:

                add_task(user_responsible) # add_task fuction call
                 
            # if user does not exist
            else: 
                print("The entered user does not exist.")
        
        # viewing all tasks
        elif menu == 'va':
            
            # opening task.txt in read mode
            task_file = open('tasks.txt','r')
                
            #checking if file is empty
            if os.stat('tasks.txt').st_size == 0:
                print("There are no tasks available. \n")
                    
            else:
                task_number = 0 

                for line in task_file:
                    task_number += 1 # updating task number
                    
                    view_all(line,task_number) # viewing task

            task_file.close() # closing file
        
        # displaying users tasks
        elif menu == 'vm':

            # opening task.txt in read mode
            task_file = open('tasks.txt','r')
                
            #checking if file is empty
            if os.stat('tasks.txt').st_size == 0:
                print("There are no tasks available. \n")
                    
            else:
                
                view_mine() # viewing task
                    
            task_file.close() # closing file
        
        # generating reports
        elif menu == 'gr':

            # dictionary of month numbers in a year
            months = {
                'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,
                'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12
                }
            
            # getting current date to check overdue tasks
            current_date = input("Enter current date (eg 07 Jan 2021): ")

            task_overview(current_date,months) # generating task_overview report

            user_overview(current_date,months) # generating user_overview report


        # displaying stats
        elif menu == 'vs':
            user_count() # calling user_count function
            
            print("User statistics")

            # displaying user stats
            print(user_count())

            # viewing users
            view_users = input("View users? (Enter 'Yes' or 'No'): ")
            
            # removing case sensitivity
            view_users = view_users.lower()
                
            if view_users == 'yes':
                # displaying user
                for user in user_cred.keys():
                    print(user)

            elif view_users == 'no':
                pass # do nothing
            
            # asking admin to re-enter their choice
            else:
                choices = ['yes','no']

                while view_users not in choices:
                    print("Invalid choice")

                    # viewing users
                    view_users = input("View users? (Enter 'Yes' or 'No'): ")
                    
                    # removing case sensitivity
                    view_users = view_users.lower()
                    
                    if view_users == 'yes':
                        
                        # displaying user
                        for user in user_cred.keys():
                            print(user)
    
                    else:
                        pass # do nothing
            print()

            print("Tasks statistics")

            # displaying task stats             
            print(task_count())
            
            # viewing tasks
            view_tasks = input("View tasks? (Enter 'Yes' or 'No'): ")
            
            # removing case sensitivity
            view_tasks = view_tasks.lower()
                
            if view_tasks == 'yes':
                # opening task.txt in read mode
                task_file = open('tasks.txt','r')
                
                #checking if file is empty
                if os.stat('tasks.txt').st_size == 0:
                    
                    print("There are no tasks available. \n")
                
                else:
                    task_number = 0 
                    
                    for line in task_file:
                        task_number += 1 # updating task number
                        
                        view_all(line,task_number) # viewing tasks

                task_file.close() # closing file

            elif view_tasks == 'no':
                pass # do nothing
            
            # asking admin to re-enter their choice
            else:
                choices = ['yes','no']

                while view_tasks not in choices:
                    print("Invalid choice")

                    # viewing tasks
                    view_tasks = input("View tasks? (Enter 'Yes' or 'No'): ")
                    
                    # removing case sensitivity
                    view_tasks = view_tasks.lower()
                    
                    if view_tasks == 'yes':
                        # opening task.txt in read mode
                        task_file = open('tasks.txt','r')
                        
                        #checking if file is empty
                        if os.stat('tasks.txt').st_size == 0:
                            print("There are no tasks available. \n")
                    
                        else:
                            task_number = 0 # initializing task count
                            
                            for line in task_file:
                                task_number += 1 # updating task number
    
                                view_all(line,task_number) # viewing tasks

                        task_file.close() # closing file

            print()

            # displaying reports
            print("Enter Yes or No to view user and task reports")
            choice = input("View reports: ").lower()
            
            print()

            if choice == 'yes':

                # checking if files exist 
                user_file_non = os.path.isfile('user_overview.txt')

                task_file_non = os.path.isfile('task_overview.txt')

                if user_file_non == False or task_file_non == False:

                    # dictionary of month numbers in a year
                    months = {
                        'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,
                        'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12
                        }
            
                    # getting current date to check overdue tasks
                    current_date = input("Enter current date (eg 07 Jan 2021): ")

                    task_overview(current_date,months) # generating task_overview report

                    user_overview(current_date,months) # generating user_overview report
                    
                    display_reports() # displaying reports
                    
                else:
                    display_reports() # displaying reports

            else:
                pass # do  nothing  

            print()

        # exiting the program
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        # informing the user of incorrect choice
        else:
            print("You have made a wrong choice, Please Try again")
