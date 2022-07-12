
import re
import zipfile


archive = zipfile.ZipFile('access_log_Jul95.zip', 'r')
archive.extractall()


def time_to_sec(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s


with open('access_log_Jul95', 'r') as f:
    count = 0

    for i in f:
        i = i.strip('\n')

        status_code_regex = re.search(r"\s([4-5][0-5][0-9])(.*(?<!\d)$)", i)
        type_regex = re.search(r"((.gif)|(.jpg)|(.jpeg)|(.mpg))\s", i)
        time_regex = re.search(r"0[3-6]:[0-5][0-9]:[0-5][0-9]", i)

        if time_regex is not None:
            time_limit = time_to_sec("03:22:33") <= time_to_sec(time_regex.group()) <= time_to_sec("06:08:59")

        if status_code_regex and type_regex and time_regex and time_limit:
            print(i)
            count += 1

print(f"\nNumber of requests: {count}")
