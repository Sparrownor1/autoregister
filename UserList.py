def getUserList(filename):
    users = {}
    for line in filename:
        # line = "XXXX = Name"
        id, name = line.strip().split(' = ')
        #line.strip() = "XXXX=Name"
        #id = "XXXX" , # name = "Name"
        # print(id + name)
        users[int(id)] = str(name)
    return users

def writeUserList(filename, userDict):
    for num in userDict:
        filename.write(str(num) + " = " + str(userDict[num]) + "\n")
