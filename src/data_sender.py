import requests
import argparse
import csv


json_data = {
    'id': 1,
    'deparment_name':'Product Management',
}

def send_files(file="departments"):
    files = {'file': open('src\data_challenge_files\{}.csv'.format(file), 'rb')}

    r = requests.post('http://localhost:5000/file/v1/{}'.format(file), files=files)
    print(r.text)

def send_bulk(file="departments"):
    spamreader = csv.reader(open('src\data_challenge_files\{}.csv'.format(file), newline=''), delimiter=',')
    sender_bulk = [row for row in spamreader]
    url = 'http://localhost:5000/{}/v1/bulk'.format(file)
    response = requests.post(url, json=sender_bulk)

    if response.status_code == 200:
        print('JSON data sent successfully!')
    else:
        print('Failed to send JSON data:', response.content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", type=int, choices=[1, 2], required=True, help="Send bulk or file")
    parser.add_argument("-f", type=str, choices=['departments', 'jobs', 'hired_employees'], help="the file name")

    args = parser.parse_args()
    print(f'Parametters {args}')
    if args.t == 1:
        send_bulk(args.f)
    if args.t == 2:
        if args.f:
            send_files(args.f)
        else:
            send_files()