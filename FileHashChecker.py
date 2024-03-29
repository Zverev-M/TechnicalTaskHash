import hashlib

BUF = 65536
func_list = {'md5': hashlib.md5, 'sha1': hashlib.sha1, 'sha256': hashlib.sha256}


def check(path, file_to_check, func_name, expected_hash_code):
    h = func_list[func_name]()
    try:
        file = open(path + "\\" + file_to_check, 'rb')
        while True:
            part = file.read(BUF)
            if not part:
                break
            h.update(part)

        file.close()

        if h.hexdigest() == expected_hash_code:
            return file_to_check + " OK"
        else:
            return file_to_check + " FAIL"
    except FileNotFoundError as e:
        return file_to_check + " NOT FOUND"

