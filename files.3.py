f=open("people1.txt","w")
lines=[
    "priyanka - shimla\n",
    "neela - delhi\n"
    "sashi - jaipur\n"
    "sarika - delhi\n"
    "deepti - shimla\n"
    "harshad - delhi\n"
    "trishna - delhi\n"
    "pradeep - jaipur\n"
    "sekhar - delhi\n"
    "nand - delhi\n"
    "anoop - delhi\n"
    "balwinder - jaipur"]
# f.writelines(lines)
# f.close()
# my_file = open("people1.txt")
# print (my_file.read())
# my_file.close()
my_file=open("data.txt","r")
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("other.txt","w")
for data in my_file:
    if "delhi" in data:
        file1.write(data)
    elif "shimla"in data:
        file2.write(data)
    else:
        file3.write(data)
file1.close()
file2.close()
file3.close()
file1=open("delhi.txt","r")
files=file1.read()
print(files)




















# my_file2 = open("people2.txt", "w")
# my_file2.write("Abhishek - Gurgaon")
# my_file2.write("Ranveer - Delhi")
# my_file2.close()

# batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
# students_file = open("navgurukul_students.html", "w")
# students_file.write("\n")
# students_file.write("\n")
# students_file.write("\n")
# students_file.write("\n")
# students_file.write("\n")
# students_file.write("\n")
#     for student in batch1_students:
#         students_file.write("
#     " + student + "
#     \n")
#     students_file.write("

# \n")
# students_file.write("\n")
# students_file.write("\n")
# students_file.close()
