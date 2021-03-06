
import event_manager as EM

def checkId(id_member):
    if(id_member[0]=='0'):
        return False
    if(len(id_member) != 8):
        return False
    return True

def checkName(name):
    for ch in name:
        if(not((ord(ch)==ord(' ')) 
        or (ord(ch)>=ord('a') and ord(ch)<=ord('z')) 
        or (ord(ch)>=ord('A') and ord(ch)<=ord('Z')))):
            return False
    return True

def checkAge(age):
    if(int(age) > 120 or int(age) <16):
        return False
    return True

def checkYear(year, age):
    new_age = 2020-int(year)
    if (new_age != int(age)):
        return False
    return True

def checkSimester(simester):
    if(int(simester) < 1):
        return False
    return True



#### PART 1 ####
# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    f = open(orig_file_path, 'r')
    c = "11401830, Homer Simpson, 50, 1970, 3"
    new_rows =[]
    original = f.readline()
    while(original):
        arr = original.split(',')
        if(checkId(arr[0]) and checkName(arr[1]) 
        and checkAge(arr[2]) and checkYear(arr[3], arr[2]) and checkSimester(arr[4])):
            new_rows.append(arr)
        original = f.readline()
    print(new_rows)
    sorted(new_rows)
    result =""
    for line in new_rows:
        print(line)
        for i, proper in enumerate(line):
            if(i!=1):
                proper ="".join( proper.split())
                if(i!=0):
                    proper=" "+proper
            proper =" ".join( proper.split())
            result += proper
            result += ', '
        result = result[:-2]
        result += "\n"

    f = open(filtered_file_path, 'w')
    f.write(result)    

    
    
# Writes the names of the K youngest students which subscribed 
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    pass
    #TODO
    
    
# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   retuns the avg, else error codes defined.
def correctAgeAvg(in_file_path: str, semester: int) -> float:
    pass
    #TODO
    

#### PART 2 ####
# Use SWIG :)
# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
def printEventsList(events :list,file_path :str): #em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    pass
    #TODO   
    
    
def testPrintEventsList(file_path :str):
    events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
                    {"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
                                 {"name" : "Improv","id":3,"date": EM.dateCreate(13, 3, 2021)}, \
                                     {"name" : "Student Festival","id":4,"date": EM.dateCreate(13, 5, 2021)},    ]
    em = printEventsList(events_lists,file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)

#### Main #### 
# feel free to add more tests and change that section. 
# sys.argv - list of the arguments passed to the python script
if __name__ == "__main__":
    print("run!")
    import sys
    if len(sys.argv)>1:
        testPrintEventsList(sys.argv[1])
    fileCorrect("tests/input", "tests/out3")
    # id_m = "123456748"
    # name = "da$#%#$sda fsdfScsacM"
    # age = "20"
    # year = "2001"
    # simester = "-5"
    # if(checkAge(age)):
    #     print(True)
    # if(not checkId(id_m)):
    #     print(True)
    # if(not checkYear(year, age)):
    #     print(True)
    # if(not checkName(name)):
    #     print(True)
    # if(not checkSimester(simester)):
    #     print(True)
