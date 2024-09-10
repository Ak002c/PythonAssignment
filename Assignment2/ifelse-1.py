total_attendence = int(input("enter total number of attendence:"))
stu_attendence = int(input("student present attendence:"))
pre_attendense = stu_attendence / total_attendence *100
reason = input("if he/she is medical cause y/n:")

if pre_attendense>75:
    print("Allowed")

if pre_attendense<75:
    if(reason == 'y'):
        print("allowed")    
    else:
        print("not allowed")

