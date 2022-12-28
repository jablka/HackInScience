def select_student(students, threshold):
    passed = [ ]
    not_passed = [ ]
    for stud in students:
        if stud[1]>=threshold:
            passed.append(stud)
            # print(stud)
        else:
            not_passed.append(stud)
            # print("neprešiel", stud)

    passed.sort(key= lambda a:a[1], reverse=True)
    # passed = sorted(passed, key= lambda a:a[1], reverse=True) # 
    # print(passed)
    
    not_passed.sort(key= lambda a:a[1])
    # print(not_passed)

    mydict = {'Accepted': passed, 'Refused': not_passed}
    return mydict