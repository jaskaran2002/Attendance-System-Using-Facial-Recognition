import pandas as pd
import matplotlib.pyplot as plt

class UserData():
    csvfile = 'data.csv'
    df = pd.read_csv(csvfile)
    students_present = {}
    for i in range (21,32):
        students_present[f'{i}-5'] = df[f'{i}-5'].sum()
        # sum = 0
        # for j in df[f'{i}-5']:
        #     sum += j
        # students_present[f'{i}-5'] = sum
        # print(students_present[f'{i}-5'])

def plt_students_present(datainstance):
    names = list(datainstance.students_present.keys())
    values = list(datainstance.students_present.values())

    plt.bar(range(len(datainstance.students_present)), values, tick_label=names)
    plt.xlabel('Date')
    plt.ylabel('No. of students present')
    plt.show()


if __name__ == "__main__":
    test = UserData()
    print(test.students_present['21-5'])
    plt_students_present(test)
# print(test.df)