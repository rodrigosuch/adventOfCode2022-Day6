INPUT_FILE = "input.txt"

def check_array(array):
    ocurrence = 0
    for search in array:
        for item in array:
            if item == search:
                ocurrence += 1
        if ocurrence > 1:
            return False
        ocurrence = 0
    return True


with open(INPUT_FILE) as file:
    line = file.readline()
    for idx in range(0, len(line)-13):
        if check_array(line[idx:idx+14]) == True:
            print(f"found in  idx {idx+14}")
            break
