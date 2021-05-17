import sys
import FileHashChecker

path_to_log_file = sys.argv[1]
path_to_directory = sys.argv[2]

file = open(path_to_log_file, 'r')
data = file.readline().split()
while data:
    fileName = data[0]
    funcName = data[1]
    code = data[2]

    print(FileHashChecker.check(path_to_directory, fileName, funcName, code))
    data = file.readline().split()

file.close()


