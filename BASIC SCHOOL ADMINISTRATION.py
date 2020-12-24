#PROJECT1 : BASIC SCHOOL ADMINISTRATION TOOL
import csv
def write_into_csv (info_list):
    with open('Student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["NAME","AGE","CONTACT NUMBER","E-MAIL ID"])
        writer.writerow(info_list)
if __name__ == '__main__':
    condition = True
    student_num = 1
    while(condition):
        student_info = input("Enter Student Info for Student #{}(Format: Name Age Contact_Number Email_ID): ".format(student_num))
        student_info_list = student_info.split(' ')
        print("\nThe entered info is -\n Name: {} \n Age: {} \n Contact No.: {} \n Email ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Is the entered Information Correct??(yes/no): ")
        if choice_check == 'yes':
            write_into_csv(student_info_list)
            condition_check = input("Enter (yes/no) if you want to enter information of another Student: ")
            if condition_check == "yes":
                conditon = True
                student_num += 1
            elif condition_check == "no":
                condition = False
        elif choice_check == 'no':
            print('PLEASE RE-ENTER THE VALUES!')
