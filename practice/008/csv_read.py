import csv

# with open('csv_example_1.csv', 'r', encoding='utf-8') as csvfile:
#     csv_reader_1 = csv.reader(csvfile, delimiter=',')
#     for row in csv_reader_1:
#         print(row, ' - ', type(row))


with open('csv_example_2.csv', 'r', encoding='utf-8') as csvfile2:
    csv_reader_2 = csv.DictReader(csvfile2)
    max_id = 1
    for row in csv_reader_2:
        if max_id < int(row['id']):
            max_id = int(row['id'])

with open('csv_example_2.csv', 'a', encoding='utf-8') as csvfile3:
    fieldnames_3 = ['id', 'first_name', 'second_name', 'last_name']
    csv_writer = csv.DictWriter(csvfile3, fieldnames=fieldnames_3)

    csv_writer.writerow({'id': max_id+1, 'first_name': f"Andrey",
                         'second_name': f"-", 'last_name': f"Solters"})
