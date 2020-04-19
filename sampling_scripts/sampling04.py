import random

files = [
    'coronavirus-tweet-id-2020-04-01-00.txt',
    'coronavirus-tweet-id-2020-04-01-01.txt',
    'coronavirus-tweet-id-2020-04-01-02.txt',
    'coronavirus-tweet-id-2020-04-01-03.txt',
    'coronavirus-tweet-id-2020-04-01-04.txt',
    'coronavirus-tweet-id-2020-04-01-05.txt',
    'coronavirus-tweet-id-2020-04-01-06.txt',
    'coronavirus-tweet-id-2020-04-01-07.txt',
    'coronavirus-tweet-id-2020-04-01-08.txt',
    'coronavirus-tweet-id-2020-04-01-09.txt',
    'coronavirus-tweet-id-2020-04-01-10.txt',
    'coronavirus-tweet-id-2020-04-01-11.txt',
    'coronavirus-tweet-id-2020-04-01-12.txt',
    'coronavirus-tweet-id-2020-04-01-13.txt',
    'coronavirus-tweet-id-2020-04-01-14.txt',
    'coronavirus-tweet-id-2020-04-01-15.txt',
    'coronavirus-tweet-id-2020-04-01-16.txt',
    'coronavirus-tweet-id-2020-04-01-17.txt',
    'coronavirus-tweet-id-2020-04-01-18.txt',
    'coronavirus-tweet-id-2020-04-01-19.txt',
    'coronavirus-tweet-id-2020-04-01-20.txt',
    'coronavirus-tweet-id-2020-04-01-21.txt',
    'coronavirus-tweet-id-2020-04-01-22.txt',
    'coronavirus-tweet-id-2020-04-01-23.txt',
    'coronavirus-tweet-id-2020-04-02-00.txt',
    'coronavirus-tweet-id-2020-04-02-01.txt',
    'coronavirus-tweet-id-2020-04-02-02.txt',
    'coronavirus-tweet-id-2020-04-02-03.txt',
    'coronavirus-tweet-id-2020-04-02-04.txt',
    'coronavirus-tweet-id-2020-04-02-05.txt',
    'coronavirus-tweet-id-2020-04-02-06.txt',
    'coronavirus-tweet-id-2020-04-02-07.txt',
    'coronavirus-tweet-id-2020-04-02-08.txt',
    'coronavirus-tweet-id-2020-04-02-09.txt',
    'coronavirus-tweet-id-2020-04-02-10.txt',
    'coronavirus-tweet-id-2020-04-02-11.txt',
    'coronavirus-tweet-id-2020-04-02-12.txt',
    'coronavirus-tweet-id-2020-04-02-13.txt',
    'coronavirus-tweet-id-2020-04-02-14.txt',
    'coronavirus-tweet-id-2020-04-02-15.txt',
    'coronavirus-tweet-id-2020-04-02-16.txt',
    'coronavirus-tweet-id-2020-04-02-17.txt',
    'coronavirus-tweet-id-2020-04-02-18.txt',
    'coronavirus-tweet-id-2020-04-02-19.txt',
    'coronavirus-tweet-id-2020-04-02-20.txt',
    'coronavirus-tweet-id-2020-04-02-21.txt',
    'coronavirus-tweet-id-2020-04-02-22.txt',
    'coronavirus-tweet-id-2020-04-02-23.txt',
    'coronavirus-tweet-id-2020-04-03-00.txt',
    'coronavirus-tweet-id-2020-04-03-01.txt',
    'coronavirus-tweet-id-2020-04-03-02.txt',
    'coronavirus-tweet-id-2020-04-03-03.txt',
    'coronavirus-tweet-id-2020-04-03-04.txt',
    'coronavirus-tweet-id-2020-04-03-05.txt',
    'coronavirus-tweet-id-2020-04-03-06.txt',
    'coronavirus-tweet-id-2020-04-03-07.txt',
    'coronavirus-tweet-id-2020-04-03-08.txt',
    'coronavirus-tweet-id-2020-04-03-09.txt',
    'coronavirus-tweet-id-2020-04-03-10.txt',
    'coronavirus-tweet-id-2020-04-03-11.txt',
    'coronavirus-tweet-id-2020-04-03-12.txt',
    'coronavirus-tweet-id-2020-04-03-13.txt',
    'coronavirus-tweet-id-2020-04-03-14.txt',
    'coronavirus-tweet-id-2020-04-03-15.txt',
    'coronavirus-tweet-id-2020-04-03-16.txt',
    'coronavirus-tweet-id-2020-04-03-17.txt',
    'coronavirus-tweet-id-2020-04-03-18.txt',
    'coronavirus-tweet-id-2020-04-03-19.txt',
    'coronavirus-tweet-id-2020-04-03-20.txt',
    'coronavirus-tweet-id-2020-04-03-21.txt',
    'coronavirus-tweet-id-2020-04-03-22.txt',
    'coronavirus-tweet-id-2020-04-03-23.txt',
    'coronavirus-tweet-id-2020-04-04-00.txt',
    'coronavirus-tweet-id-2020-04-04-01.txt',
    'coronavirus-tweet-id-2020-04-04-02.txt',
    'coronavirus-tweet-id-2020-04-04-03.txt',
    'coronavirus-tweet-id-2020-04-04-04.txt',
    'coronavirus-tweet-id-2020-04-04-05.txt',
    'coronavirus-tweet-id-2020-04-04-06.txt',
    'coronavirus-tweet-id-2020-04-04-07.txt',
    'coronavirus-tweet-id-2020-04-04-08.txt',
    'coronavirus-tweet-id-2020-04-04-09.txt',
    'coronavirus-tweet-id-2020-04-04-10.txt',
    'coronavirus-tweet-id-2020-04-04-11.txt',
    'coronavirus-tweet-id-2020-04-04-12.txt',
    'coronavirus-tweet-id-2020-04-04-13.txt',
    'coronavirus-tweet-id-2020-04-04-14.txt',
    'coronavirus-tweet-id-2020-04-04-15.txt',
    'coronavirus-tweet-id-2020-04-04-16.txt',
    'coronavirus-tweet-id-2020-04-04-17.txt',
    'coronavirus-tweet-id-2020-04-04-18.txt',
    'coronavirus-tweet-id-2020-04-04-19.txt',
    'coronavirus-tweet-id-2020-04-04-20.txt',
    'coronavirus-tweet-id-2020-04-04-21.txt',
    'coronavirus-tweet-id-2020-04-04-22.txt',
    'coronavirus-tweet-id-2020-04-04-23.txt',
    'coronavirus-tweet-id-2020-04-05-00.txt',
    'coronavirus-tweet-id-2020-04-05-01.txt',
    'coronavirus-tweet-id-2020-04-05-02.txt',
    'coronavirus-tweet-id-2020-04-05-03.txt',
    'coronavirus-tweet-id-2020-04-05-04.txt',
    'coronavirus-tweet-id-2020-04-05-05.txt',
    'coronavirus-tweet-id-2020-04-05-06.txt',
    'coronavirus-tweet-id-2020-04-05-07.txt',
    'coronavirus-tweet-id-2020-04-05-08.txt',
    'coronavirus-tweet-id-2020-04-05-09.txt',
    'coronavirus-tweet-id-2020-04-05-10.txt',
    'coronavirus-tweet-id-2020-04-05-11.txt',
    'coronavirus-tweet-id-2020-04-05-12.txt',
    'coronavirus-tweet-id-2020-04-05-13.txt',
    'coronavirus-tweet-id-2020-04-05-14.txt',
    'coronavirus-tweet-id-2020-04-05-15.txt',
    'coronavirus-tweet-id-2020-04-05-16.txt',
    'coronavirus-tweet-id-2020-04-05-17.txt',
    'coronavirus-tweet-id-2020-04-05-18.txt',
    'coronavirus-tweet-id-2020-04-05-19.txt',
    'coronavirus-tweet-id-2020-04-05-20.txt',
    'coronavirus-tweet-id-2020-04-05-21.txt',
    'coronavirus-tweet-id-2020-04-05-22.txt',
    'coronavirus-tweet-id-2020-04-05-23.txt',
    'coronavirus-tweet-id-2020-04-06-00.txt',
    'coronavirus-tweet-id-2020-04-06-01.txt',
    'coronavirus-tweet-id-2020-04-06-02.txt',
    'coronavirus-tweet-id-2020-04-06-03.txt',
    'coronavirus-tweet-id-2020-04-06-04.txt',
    'coronavirus-tweet-id-2020-04-06-05.txt',
    'coronavirus-tweet-id-2020-04-06-06.txt',
    'coronavirus-tweet-id-2020-04-06-07.txt',
    'coronavirus-tweet-id-2020-04-06-08.txt',
    'coronavirus-tweet-id-2020-04-06-09.txt',
    'coronavirus-tweet-id-2020-04-06-10.txt',
    'coronavirus-tweet-id-2020-04-06-11.txt',
    'coronavirus-tweet-id-2020-04-06-12.txt',
    'coronavirus-tweet-id-2020-04-06-13.txt',
    'coronavirus-tweet-id-2020-04-06-14.txt',
    'coronavirus-tweet-id-2020-04-06-15.txt',
    'coronavirus-tweet-id-2020-04-06-16.txt',
    'coronavirus-tweet-id-2020-04-06-17.txt',
    'coronavirus-tweet-id-2020-04-06-18.txt',
    'coronavirus-tweet-id-2020-04-06-19.txt',
    'coronavirus-tweet-id-2020-04-06-20.txt',
    'coronavirus-tweet-id-2020-04-06-21.txt',
    'coronavirus-tweet-id-2020-04-06-22.txt',
    'coronavirus-tweet-id-2020-04-06-23.txt',
    'coronavirus-tweet-id-2020-04-07-00.txt',
    'coronavirus-tweet-id-2020-04-07-01.txt',
    'coronavirus-tweet-id-2020-04-07-02.txt',
    'coronavirus-tweet-id-2020-04-07-03.txt',
    'coronavirus-tweet-id-2020-04-07-04.txt',
    'coronavirus-tweet-id-2020-04-07-05.txt',
    'coronavirus-tweet-id-2020-04-07-06.txt',
    'coronavirus-tweet-id-2020-04-07-07.txt',
    'coronavirus-tweet-id-2020-04-07-08.txt',
    'coronavirus-tweet-id-2020-04-07-09.txt',
    'coronavirus-tweet-id-2020-04-07-10.txt',
    'coronavirus-tweet-id-2020-04-07-11.txt',
    'coronavirus-tweet-id-2020-04-07-12.txt',
    'coronavirus-tweet-id-2020-04-07-13.txt',
    'coronavirus-tweet-id-2020-04-07-14.txt',
    'coronavirus-tweet-id-2020-04-07-15.txt',
    'coronavirus-tweet-id-2020-04-07-16.txt',
    'coronavirus-tweet-id-2020-04-07-17.txt',
    'coronavirus-tweet-id-2020-04-07-18.txt',
    'coronavirus-tweet-id-2020-04-07-19.txt',
    'coronavirus-tweet-id-2020-04-07-20.txt',
    'coronavirus-tweet-id-2020-04-07-21.txt',
    'coronavirus-tweet-id-2020-04-07-22.txt',
    'coronavirus-tweet-id-2020-04-07-23.txt',
    'coronavirus-tweet-id-2020-04-08-00.txt',
    'coronavirus-tweet-id-2020-04-08-01.txt',
    'coronavirus-tweet-id-2020-04-08-02.txt',
    'coronavirus-tweet-id-2020-04-08-03.txt',
    'coronavirus-tweet-id-2020-04-08-04.txt',
    'coronavirus-tweet-id-2020-04-08-05.txt',
    'coronavirus-tweet-id-2020-04-08-06.txt',
    'coronavirus-tweet-id-2020-04-08-07.txt',
    'coronavirus-tweet-id-2020-04-08-08.txt',
    'coronavirus-tweet-id-2020-04-08-09.txt',
    'coronavirus-tweet-id-2020-04-08-10.txt',
    'coronavirus-tweet-id-2020-04-08-11.txt',
    'coronavirus-tweet-id-2020-04-08-12.txt',
    'coronavirus-tweet-id-2020-04-08-13.txt',
    'coronavirus-tweet-id-2020-04-08-14.txt',
    'coronavirus-tweet-id-2020-04-08-15.txt',
    'coronavirus-tweet-id-2020-04-08-16.txt',
    'coronavirus-tweet-id-2020-04-08-17.txt',
    'coronavirus-tweet-id-2020-04-08-18.txt',
    'coronavirus-tweet-id-2020-04-08-19.txt',
    'coronavirus-tweet-id-2020-04-08-20.txt',
    'coronavirus-tweet-id-2020-04-08-21.txt',
    'coronavirus-tweet-id-2020-04-08-22.txt',
    'coronavirus-tweet-id-2020-04-08-23.txt',
    'coronavirus-tweet-id-2020-04-09-00.txt',
    'coronavirus-tweet-id-2020-04-09-01.txt',
    'coronavirus-tweet-id-2020-04-09-02.txt',
    'coronavirus-tweet-id-2020-04-09-03.txt',
    'coronavirus-tweet-id-2020-04-09-04.txt',
    'coronavirus-tweet-id-2020-04-09-05.txt',
    'coronavirus-tweet-id-2020-04-09-06.txt',
    'coronavirus-tweet-id-2020-04-09-07.txt',
    'coronavirus-tweet-id-2020-04-09-08.txt',
    'coronavirus-tweet-id-2020-04-09-09.txt',
    'coronavirus-tweet-id-2020-04-09-10.txt',
    'coronavirus-tweet-id-2020-04-09-11.txt',
    'coronavirus-tweet-id-2020-04-09-12.txt',
    'coronavirus-tweet-id-2020-04-09-13.txt',
    'coronavirus-tweet-id-2020-04-09-14.txt',
    'coronavirus-tweet-id-2020-04-09-15.txt',
    'coronavirus-tweet-id-2020-04-09-16.txt',
    'coronavirus-tweet-id-2020-04-09-17.txt',
    'coronavirus-tweet-id-2020-04-09-18.txt',
    'coronavirus-tweet-id-2020-04-09-19.txt',
    'coronavirus-tweet-id-2020-04-09-20.txt',
    'coronavirus-tweet-id-2020-04-09-21.txt',
    'coronavirus-tweet-id-2020-04-09-22.txt',
    'coronavirus-tweet-id-2020-04-09-23.txt',
    'coronavirus-tweet-id-2020-04-10-00.txt',
    'coronavirus-tweet-id-2020-04-10-01.txt',
    'coronavirus-tweet-id-2020-04-10-02.txt',
    'coronavirus-tweet-id-2020-04-10-03.txt',
    'coronavirus-tweet-id-2020-04-10-04.txt',
    'coronavirus-tweet-id-2020-04-10-05.txt',
    'coronavirus-tweet-id-2020-04-10-06.txt',
    'coronavirus-tweet-id-2020-04-10-07.txt',
    'coronavirus-tweet-id-2020-04-10-08.txt',
    'coronavirus-tweet-id-2020-04-10-09.txt',
    'coronavirus-tweet-id-2020-04-10-10.txt',
    'coronavirus-tweet-id-2020-04-10-11.txt',
    'coronavirus-tweet-id-2020-04-10-12.txt',
    'coronavirus-tweet-id-2020-04-10-13.txt',
    'coronavirus-tweet-id-2020-04-10-14.txt',
    'coronavirus-tweet-id-2020-04-10-15.txt',
    'coronavirus-tweet-id-2020-04-10-16.txt',
    'coronavirus-tweet-id-2020-04-10-17.txt',
    'coronavirus-tweet-id-2020-04-10-18.txt',
    'coronavirus-tweet-id-2020-04-10-19.txt',
    'coronavirus-tweet-id-2020-04-10-20.txt',
    'coronavirus-tweet-id-2020-04-10-21.txt'
]

for filename in files:
    with open(filename, 'r+') as f:
        line = f.readline()
        arr = []
        while line:
            line = f.readline()
            if len(line) > 0:
                arr.append(line)
        
        random.shuffle(arr)
        arr = arr[:int(len(arr) / 10)]

        f.seek(0)
        f.writelines(arr)
        f.truncate()
        f.close()
    print("Finished Sampling ", filename)
