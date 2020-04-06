import csv

def createMarks(file_name):
    marks_list = []
    rank_list = []
    with open(file_name, newline='') as csvfile:
        marks_reader = csv.reader(csvfile)
        for row in marks_reader:
            marks_list.append(row[1])
            rank_list.append(0)
    freq_list = [marks_list.count(x) for x in marks_list]
    # Now, get ranks
    mark_set = set(marks_list)
    rank = 1
    for i in sorted(list(mark_set), reverse=True):
        for x in range(0,1000):
            if i==marks_list[x]:
                rank_list[x]=rank
        rank = rank+1

    return marks_list, rank_list, freq_list

def main():
    csv_uri = 'marksheet.csv'
    marks, rank, freq = createMarks(csv_uri)

    while(True):
        inp = input('Enter Roll Number : ')
        if inp == 'stop' :
            break
        roll_no = int(inp) - 1

        print('Marks: ' + str(marks[roll_no]) + ', Rank: ' + str(rank[roll_no]) + ', Tied Between: ' + str(freq[roll_no]))


if __name__ == '__main__':
    main()
