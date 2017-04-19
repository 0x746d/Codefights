# more than 90 % of all messages had fewer than 5 words
#   (here, a word is defined as a sequence of consecutive Latin
#   letters which is neither preceded nor followed by a Latin letter);
# more than 50 % of messages to any one user had the same content,
#   assuming that there were at least 2 messages to that user;
# more than 50 % of all messages had the same content,
#   assuming that there were at least 2 messages;
# more than 50 % of all messages contained at least one of the words
#   from the given list of spamSignals (the letters' case doesn't matter).

# COULD write loops that create variables for ALL MESSAGES and IDs

from fractions import Fraction
from collections import Counter

def spamDetection(messages, spamSignals):

    messages_to_user = 0

    same_content = 0

    spam_words = 0

    latin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # check for number of words
    # user = messages[1]

    fails = 0

    user_ids = []
    out_message = []
    all_messages = []
    new_messages = []

    for msg in range (len(messages)):
        all_messages.append(messages[msg][0])

    # add all users to one list

# loop through characters to find words
# add to total_words if less than 5
    for x in range(len(messages)):
        total_words = 0
        new_message = ''
        message = messages[x][0].lower()
        user = messages[x][1]
        user_ids.append(user)
        for char in message:
            if char in latin:
                new_message += char
            else:
                new_message += " "
        new_messages.append(new_message)

        # print(new_message)

        total_words = len(new_message.split())

        if total_words < 5:
            fails += 1

    # for each user id go through list and see if messages are equal
    # count number of messages to that user first

    for i in range(len(messages)):
        current_user = messages[i][1]
        for j in range(len(messages)):
            other_user = messages[j][1]
            if j == i:
                continue
            elif current_user == other_user:
                if messages[i][0] == messages[j][0]:
                    user_ids.append(current_user)


    # Check for message similarity

    user_ids = []
    same_message = []   # collection of all same messages, used to collect id instances per message
    user_id_count = []
    one_id = []     # stores single instance of all ids

    for i in range(len(messages)):
        user_id_count.append(messages[i][1])

    id_count = Counter(user_id_count)   # number of instances of each id



    for i in range(len(messages)):
        current_user = messages[i][1]

        for j in range(len(messages)):
            other_user = messages[j][1]
            if j == i:
                continue
            elif current_user == other_user:
                if messages[i][0] == messages[j][0]:
                    user_ids.append([current_user, other_user])
                    same_message.append(messages[i])

    for i in range(len(messages)):
        if messages[i][1] not in one_id:
            one_id.append(messages[i][1])
        else:
            pass

    id_counter = []
    for msg in range(len(same_message)):
        id_counter.append(same_message[msg][1])

    fails_id_counter = Counter(id_counter)
    failed_users = []

    for id in one_id:
        if id_count[id] > 0 and fails_id_counter[id] > 0:
            if fails_id_counter[id] / id_count[id] > 0.5:
                failed_users.append(id)

    toString = "failed: "

    for i in failed_users:
        toString += i
        if failed_users.index(i) != -1:
            toString += " "

    # print("failed: ", out_message)
    failed_users_string = toString[:-1]


    # THIRD part of spambot
    # if fail, print failed messages
    content_check = []

    for msg in range(len(messages)):
        content_check.append(messages[msg][0])

    content_counter = Counter(content_check)

    part_3 = "failed: "
    if len(messages) >= 2:
        for i in content_counter:
           if content_counter[i] / len(messages) > 0.5:
               part_3 += str(i)

    if part_3 == "failed: ":
        part_3 = "passed"

    # FOURTH part of spambot
    spam_count = 0
    spams = []

    # compare message content to spam words
    # append spam words to list
    # then append to string

    spam_message = ""

    for msg in new_messages:
        lower_message = msg.split()
        for wrd in lower_message:
            for spam in spamSignals:
                spam_lower = spam.lower()
                if spam_lower == wrd:
                    spam_count += 1

                    if spam_lower not in spams:
                        spams.append(spam)
                continue


    if len(spams) > 0:
        if spam_count / len(messages) > 0.5:
            spam_message = "failed: "
            spams.sort()
            for x in spams:
                spam_message += x + " "

        else:
            spam_message = "passed "
    else:
        spam_message = 'passed '





# Constructs first element of output

    if fails / len(messages) < 0.9:
        out_message.append("passed")

    else:
        f = Fraction(fails, len(messages))
        if f == 1:
            out_message.append("failed: 1/1")
        else: out_message.append("failed: " + str(f))

# Constructs second part of output

    if len(failed_users) == 0:
        out_message.append("passed")
    else:
        out_message.append(failed_users_string)

# Construct third part of output

    out_message.append(part_3)

# Fourth output part

    out_message.append(spam_message[:-1])


    return out_message

# Test cases

print(spamDetection([["Sale today!","2837273"],
 ["Unique offer!","3873827"],
 ["Only today and only for you!","2837273"],
 ["Sale today!","2837273"],
 ["Unique offer!","3873827"]],["sale", "discount", "offer"]))

print(spamDetection([["Check Codefights out","7284736"],
 ["Check Codefights out","7462832"],
 ["Check Codefights out","3625374"],
 ["Check Codefights out","7264762"]], ["sale", "discount", "offer"]))

print(spamDetection([["Jkl ABA ty","111"],
 ["Jkl aba TY","222"],
 ["Jkl abA Ty","111"],
 ["jkl Aba tY","111"],
 ["JKl ABA ty","222"],
 ["Jkl aba tY","222"],
 ["Jkl abA Ty","111"],
 ["jkl Aba tY klk TY","111"],
 ["Jkl aBa tY","222"],
 ["Jkl aBA Ty","111"],
 ["Jkl aBA TY","111"]], ["ty",
 "jk",
 "ab"]))



