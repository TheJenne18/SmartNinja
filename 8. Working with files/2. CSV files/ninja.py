with open('ninja.csv', 'r') as csv_file:
    csv_lines = csv_file

    for line in csv_lines:
        print(line)
        name = line.split(",")[0]
        age = line.split(",")[1]
        gender = line.split(",")[2]

        print(name + " is " + gender + " and " + age + " years old.")