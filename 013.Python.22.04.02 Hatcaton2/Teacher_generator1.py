def students_data():

    with open('Students.csv') as f:
      students_data = f.readlines()

    return students_data

def clear_column_value(value):
    return value.strip()

def main():

    students_class = []
    students_name = []
    students_surname = []
    students_missing_task = []
    students_rating = []


    for line in students_data():
        splitted_line = line.split(',')
        students_class.append(clear_column_value(splitted_line [0]))
        students_name.append(clear_column_value(splitted_line[1]))
        students_surname.append(clear_column_value(splitted_line[2]))
        students_missing_task.append(clear_column_value(splitted_line[3]))
        students_rating.append(clear_column_value(splitted_line[4]))


    counter = len(students_rating)

    for i in range(1,counter):

        try:
            if not students_rating[i].isdigit():
               raise ValueError('Intcorrect rating')
        except:
            with open('blacklist.txt', 'a+') as f:
                f.write(f'{students_name[i]} {students_surname[i]} --> nieobecnośc na zajeciach. \n Prosimy zgłosić się do wykładowcy.\n')
                f.write('\n')

        if (students_rating[i] != '5'):
            message = f"Hi {students_name[i]} {students_surname [i]},\n\nThis is a reminder that you have number of ({students_missing_task[i]}) tasks left to submit before you can graduate. \n You're current grade is {students_rating[i]} and can increase to {5} if you submit all assignments before the due date.\n\n"

            print(message)

            with open('message.txt', 'a+') as f:
                f.write(message)
                f.write('***************\n ')


        else:
            message = f"Hi {students_name[i]} {students_surname [i]},\n\nThis is a reminder that you have {students_missing_task[i]} tasks left to submit before you can graduate. \n You're current grade is {students_rating[i]} - CONGRATULATIONS ! ! !.\n\n"

            print(message)

            with open('message.txt', 'a+') as f:
                f.write(message)
                f.write('-------------\n ')

if __name__ == '__main__':
    main()