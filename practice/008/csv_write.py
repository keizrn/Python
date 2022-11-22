#

import csv
#
# with open('csv_example_1.csv', 'w', encoding='utf-8') as csvfile:
#     csv_writer = csv.writer(csvfile, delimiter=',')
#
#     csv_writer.writerow(['Color', 'Size', 'Quantity', 'Responsible'])
#     csv_writer.writerow(['Red', '15', '3', None])
#     csv_writer.writerow([i for i in enumerate(range(1, 6))])


with open('csv_example_2.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames_2 = ['id', 'first_name', 'second_name', 'last_name']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames_2)

    csv_writer.writeheader()
    for i in range(1, 11):
        csv_writer.writerow({'id': i, 'first_name': f"имя_{i}",
                             'second_name': f"отчетство_{i}", 'last_name': f"фамилия_{i}"})
