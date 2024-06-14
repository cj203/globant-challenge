import requests
import csv


url = 'http://localhost:5000/hired_employees/v1/bulk'
json_data = {
    'id': 1,
    'deparment_name':'Product Management',
}
files = {'file': open('src\data_challenge_files\hired_employees.csv', 'rb')}

r = requests.post('http://localhost:5000/file/v1/hired_employees', files=files)
print(r.text)
# spamreader = csv.reader(open('src\data_challenge_files\hired_employees.csv', newline=''), delimiter=',')
# sender_bulk = [row for row in spamreader]
# print(sender_bulk[11:20])
# # for row in sender_bulk:
# #    print(row)

# response = requests.post(url, json=sender_bulk[11:20])

# if response.status_code == 200:
#     print('JSON data sent successfully!')
# else:
#     print('Failed to send JSON data:', response.content)
