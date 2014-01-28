__author__ = 'marek'

import string, random, sqlite3, os


def randomStringGenerator(size):
    return ''.join(random.choice(string.ascii_letters) for x in range(size))


def randomNumberGeneraor(size):
    return ''.join(random.choice(string.digits) for x in range(size))


def randomNumberStringGenerator(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(size))



def generateUsers():
    file = open("users.txt", "w")

    for i in range(1100,1200):
        user_list = []
        user_list.append(i.__str__())
        name = randomStringGenerator(6)
        user_list.append(name)
        lastName = randomStringGenerator(8)
        user_list.append(lastName)
        pesel = randomNumberGeneraor(11)
        user_list.append(pesel)
        nrDowodu = randomNumberStringGenerator(9)
        user_list.append(nrDowodu)
        glosowal = False
        user_list.append(glosowal.__str__())
        user_list.append("\n")
        file.write(",".join(user_list))


    file.close()


def main():
    try:
        file = open("users.txt", 'r')
    except IOError:
        generateUsers()
        file = open("users.txt", 'r')
        conn = sqlite3.connect('database.db')

        c = conn.cursor()
        lines = []
        for line in file.readlines():
            values = line.split(",")
            values.pop()
            print values
            c.execute("INSERT INTO voting_obywatel VALUES (?, ?, ?, ?, ?, ?)", values)
            lines.append(values)

        conn.commit()

        # file = open("users.txt", 'wba')
        # generateUsers(file)
    lines = []
    for line in file.readlines():
        values = line.split(",")
        values.pop()
        lines.append(values)

    #c = pycurl.Curl()
    #c.setopt(c.URL, "localhost:8000")

    for line in lines:
        cmd = '"firstName=%s&lastName=%s&pesel=%s&pass=%s&candidate=2"' % (line[1], line[2], line[3], line[4])
    
        os.system("curl -d " + cmd + " http://127.0.0.1:8000")
        
    # c.setopt(c.POSTFIELDS, cmd)
    #c.setopt(c.COOKIEFILE, '')
    #c.setopt(c.VERBOSE, False)

    # c.perform()





if __name__ == "__main__":
    main()
