import requests
import time
import json
import csv
import syndi
import config


def refresh(refresh_token):
    ACCESS_TOKEN, REFRESH_TOKEN = syndi.refresh(config.CLIENT_ID,
                                                config.CLIENT_SECRET,
                                                refresh_token)
    return(ACCESS_TOKEN, REFRESH_TOKEN)


def convert_time(month, year):
    date = str(month) + '.1.' + str(year)
    pattern = '%m.%d.%Y'
    return int(time.mktime(time.strptime(date, pattern)))


def get_user_count(start_time, end_time, access_token):
    ADDUSERS = 'http://api.syndicaster.tv/reports/additional_users?'
    HEADERS = {'Authorization': 'OAuth ' + access_token}
    r = requests.get(ADDUSERS + 'start_time=' + start_time + '&end_time=' + end_time + '&company_id=117',
                     headers=HEADERS)
    pjson = json.loads(r.text)
    return pjson['total_active_users']


def main():
    f = csv.writer(open("users.csv", "w"))
    f.writerow(['Month',
                'Total Active Users'])
    CUTOFF = 1509508800
    ACCESS_TOKEN, REFRESH_TOKEN = syndi.get_token(config.CLIENT_ID,
                                                  config.CLIENT_SECRET,
                                                  config.USERNAME,
                                                  config.PASSWORD)
    month, year = (7, 2013)
    start_time = 0
    while start_time < CUTOFF:
        month_cell = (str(month) + '/' + str(year))
        start_time = convert_time(month, year)
        if month < 12:
            month += 1
            end_time = convert_time(month, year)
        else:
            month = 1
            year += 1
            end_time = convert_time(month, year)
        userval = get_user_count(str(start_time), str(end_time), ACCESS_TOKEN)
        f.writerow([month_cell,
                    userval])
        ACCESS_TOKEN, REFRESH_TOKEN = refresh(REFRESH_TOKEN)


if __name__ == '__main__':
    main()
