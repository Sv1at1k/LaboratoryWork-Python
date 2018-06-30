import re

if __name__ == "__main__":
    count = 0
    with open("access_log_Jul95") as file:
        for line in file:
            if re.search('01/Jul/1995:[0-0][1-1]:[3-3][5-8]:[1-9][1-9] ',
                         str(line)) and re.search('\\b5\d{2}\\b',
                                                                                                   str(line)):
                count += 1
                print(line)
print(count)

