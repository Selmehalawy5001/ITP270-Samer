#!/usr/bin/python3

print("Welcome to the ITP270 SPRING 2022 Course!")

user_choice = input("Do you want to proceed with the program?[y/n]")

if user_choice == "y":
	user_name = input("Enter your user name: ") 
	user_course = input("Enter the name of the course: ")
	print("Thanks "  + user_name + " for taking the course " + user_course + ".")
else: 
	print("Have a good day!")
