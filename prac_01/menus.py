'''
CP1404/CP5632 - Practical
Creating Menus
One very common programming task is to make menus by combining looping (repeat the program until the user quits) with
selection (let the user decide what to do).

The general pattern of a menu-driven program is as follows:

display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed
=============================================
Use this pattern to create a very simple menu-driven program according to the pseudocode below:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
=====================================================
Sample output for this program should look like:

Enter name: Guido
(H)ello
(G)oodbye
(Q)uit
>>> A
Invalid choice
(H)ello
(G)oodbye
(Q)uit
>>> H
Hello Guido
(H)ello
(G)oodbye
(Q)uit
>>> G
Goodbye Guido
(H)ello
(G)oodbye
(Q)uit
>>> Q
Finished.
'''

user_name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
user_choice = input(">>> ").upper()

while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello {user_name}")
    elif user_choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    user_choice = input(">>> ").upper()
print("Finished.")