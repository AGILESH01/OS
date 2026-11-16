# QUESTION 8
# LAB-8: FILE SYSTEM SIMULATOR

import os

print("=========================================")
print("          File System Simulator")
print("=========================================")

filename = "student.txt"
new_filename = "student_record.txt"

# Create and write into the file
with open(filename, "w") as file:
    file.write("Operating Systems Lab\n")
    file.write("Experiment 8\n")
    file.write("File System Simulator\n")

print("File Created Successfully.")

# Append data
with open(filename, "a") as file:
    file.write("Python File Handling Example\n")

print("Data Appended Successfully.")

# Read file
print("\nReading File Contents:\n")
with open(filename, "r") as file:
    print(file.read())

# Rename file
os.rename(filename, new_filename)
print("File Renamed Successfully.")

# Delete file
os.remove(new_filename)
print("File Deleted Successfully.")

print("\nExperiment Completed Successfully.")
