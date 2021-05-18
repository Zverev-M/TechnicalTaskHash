import sys
import FileHashChecker

path_to_log_file = sys.argv[1]
path_to_directory = sys.argv[2]

try:
    file = open(path_to_log_file, 'r')
    data = file.readline().split()
    while data:
        file_name = ' '.join(data[0:len(data) - 2])
        func_name = data[len(data) - 2]
        code = data[len(data) - 1]

        print(FileHashChecker.check(path_to_directory, file_name, func_name, code))
        data = file.readline().split()

    file.close()
except IOError as e:
    print("Can't open input file")
