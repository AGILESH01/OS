#!/bin/bash
# QUESTION 1
# LAB-1: LINUX/UBUNTU COMMANDS
# Execute this file in an Ubuntu/Linux terminal.

# 1. Display current directory
pwd

# 2. List files
ls
ls -l
ls -a

# 3. Create directory
mkdir -p OSLab

# 4. Change directory
cd OSLab

# 5. Create file
touch sample.txt

# 6. Write into file
echo "Operating Systems Lab" > sample.txt

# 7. View file
cat sample.txt

# 8. Copy file
cp sample.txt copy.txt

# 9. Rename copied file
mv copy.txt renamed.txt

# 10. Remove renamed file
rm -f renamed.txt

# 11. Change file permissions and list details
chmod 755 sample.txt
ls -l

# 12. Display date
date

# 13. Display logged-in user
whoami

# 14. Display running processes
ps

# 15. Clear screen (kept last because it clears previous output)
clear
