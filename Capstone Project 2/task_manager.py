#=====importing libraries===========
# iporting the os module
import os

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
            # only admin can register a new user
            if username == 'admin': 

                # open user.txt in append mode
                user_file = open('user.txt','a')

                # new user username, no case sensitivity
                new_user = input("Enter a username: ").lower() 
                    
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

                user_file.close() # closing file

            else:
                # informing users of registration restrictions
                print("Only admin is allowed to register a new user.")
            
        # adding and assigning a task
        elif menu == 'a':
            
            # opening tasks.txt in append mode
            task_file = open('tasks.txt','a')

            # user responsible
            user_responsible = input("Enter the responsible person: ")
            
            # checkin if entered user exists
            if user_responsible in user_cred:
                
                # adding user to file
                task_file.write("\n" + user_responsible + ", ") 

                # adding task title to file
                task_tile = input("Enter task title: ")
                task_file.write(task_tile + ", ")

                # adding description to file
                description = input("Describe task: ")
                task_file.write(description + ", ")

                # adding due date to file
                due_date = input("Enter due date (eg 29 Oct 2021): ")
                task_file.write(due_date + ", ")

                # adding current date to file
                date = input("Enter current date (eg 29 Oct 2021): ")
                task_file.write(date + ", ")

                # indicating if the task is complete or not
                task_complete = input("Task complete? ('Yes' or 'No'): ")
                task_file.write(task_complete)

            # if user does not exist
            else: 
                print("The entered user does not exist.")

            task_file.close() # closing the file
        
        # viewing all tasks
        elif menu == 'va':
            
            # opening task.txt in read mode
            task_file = open('tasks.txt','r')
                
            #checking if file is empty
            if os.stat('tasks.txt').st_size == 0:
                
                print("There are no tasks available. \n")
                    
            else:
                # keeping track of task number
                task_number = 0
                    
                # iterating through file
                for line in task_file:

                    # Seperating the task information
                    line = line.split(', ')
                        
                    task_number += 1 # updating task number
                    
                    headings = [
                        'Person responsible','Title','Description',
                        'Due date','Date task was assigned','Task complete?'
                        ]

                    # string for building task information
                    display = ""

                    for index in range(len(headings)):
                        
                        # space to align the info when displaying it
                        space = " "*(23 - len(headings[index]))

                        # building the output string
                        display += f"{headings[index]} {space}: {line[index]} \n"

                    # displaying task
                    print(f"Task {task_number}")
                    print(display) # displaying contents of each task

            task_file.close() # closing file
        
        # displaying users tasks
        elif menu == 'vm':

            # opening task.txt in read mode
            task_file = open('tasks.txt','r')
                
            #checking if file is empty
            if os.stat('tasks.txt').st_size == 0:
                
                print("There are no tasks available. \n")
                    
            else:
                # keeping track of task number
                task_number = 0

                # iterating through file
                for line in task_file:

                    # Seperating the task information
                    line = line.split(', ')

                    if line[0] == username: # confirminig username

                        task_number += 1 # updating task number

                        headings = [
                            'Person responsible','Title','Description',
                            'Due date','Date task was assigned','Task complete?'
                            ]

                        # string for building task information
                        display = ""

                        for index in range(len(headings)):

                            # space to align the info when displaying it
                            space = " "*(22 - len(headings[index]))
                                
                            # building the output string
                            display += f"{headings[index]} {space}: {line[index]} \n"

                        # displaying task
                        print(f"Task {task_number}")
                        print(display) # displaying contents of each task

                if task_number == 0:
                    print("There are no tasks assigned to you yet. \n")
                    
            task_file.close() # closing file

        # displaying stats
        elif menu == 'vs':
            
            # opening user.txt and tasks.txt in read mode
            user_file = open('user.txt','r')
            task_file = open('tasks.txt','r')

            # initializing number of users storage
            number_of_users = 0

            # initializing number of tasks storage
            number_of_tasks = 0

            print("User statistics")

            #checking if file is empty
            if os.stat('user.txt').st_size == 0:
                
                # displaying user stats
                print(f"Total number of users : {number_of_users}")

            else:
                # counting number of users
                for line in user_file:

                    # updating number of users
                    number_of_users += 1

            user_file.close() # closing file

            # displaying user stats
            print(f"Total number of users : {number_of_users} \n")

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

            #checking if file is empty
            if os.stat('tasks.txt').st_size == 0:

                # displaying user stats
                print(f"Total number of tasks : {number_of_tasks}")

            else:
                # counting number of tasks
                for line in task_file:

                    # updating number of tasks
                    number_of_tasks += 1

            task_file.close() # closing file

            # displaying task stats             
            print(f"Total number of tasks : {number_of_tasks} \n")
            
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
                    # keeping track of task number
                    task_number = 0
                    
                    # iterating through file
                    for line in task_file:
                        
                        # Seperating the task information
                        line = line.split(', ')
                        
                        task_number += 1 # updating task number
                        
                        headings = [
                            'Person responsible','Title','Description',
                            'Due date','Date task was assigned','Task complete?'
                            ]
                        
                        # string for building task information
                        display = ""
                        
                        for index in range(len(headings)):
                            
                            # space to align the info when displaying it
                            space = " "*(23 - len(headings[index]))
                            
                            # building the output string
                            display += f"{headings[index]} {space}: {line[index]} \n"

                        # displaying task
                        print(f"Task {task_number}")
                        print(display) # displaying contents of each task

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
                            # keeping track of task number
                            task_number = 0
                    
                            # iterating through file
                            for line in task_file:
                                # Seperating the task information
                                line = line.split(', ')
                        
                                task_number += 1 # updating task number
                    
                                headings = [
                                    'Person responsible','Title','Description',
                                    'Due date','Date task was assigned','Task complete?'
                                    ]

                                # string for building task information
                                display = ""
                                
                                for index in range(len(headings)):
                                    
                                    # space to align the info when displaying it
                                    space = " "*(23 - len(headings[index]))

                                    # building the output string
                                    display += f"{headings[index]} {space}: {line[index]} \n"

                                # displaying task
                                print(f"Task {task_number}")
                                print(display) # displaying contents of each task

                            task_file.close() # closing file
    
                    else:
                        pass # do nothing

            print()

        # exiting the program
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        # informing the user of incorrect choice
        else:
            print("You have made a wrong choice, Please Try again")
