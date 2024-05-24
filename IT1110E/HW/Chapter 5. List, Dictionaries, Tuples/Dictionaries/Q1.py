#In US, the president is not elected by direct vote, but by a two-level vote. First, elections are held
#in each state and the winner of the elections in that state is determined. Then state elections are held:
#in these elections, each state has a certain number of votes - the number of electors from that state.
#In practice, all state electors vote according to the results of intra-state voting, that is, states with a
#different number of votes vote in the final stage of elections. You know who each state voted for and how many
#votes were cast by that state. Summarize the results of the elections: for each of the voting participants,
#determine the number of votes cast for him.

d = dict()


def info(s):
    lst = s.split()
    return {'sur': lst[-2], 'vote': int(lst[-1])}


s = input()
while True:
    if info(s)['sur'] not in d:
        d[info(s)['sur']] = info(s)['vote']
    else:
        d[info(s)['sur']] += info(s)['vote']

    try:
        s = input()
    except:
        break

lst = [(k, v) for (k, v) in d.items()]
lst.sort()
# print(lst)
for ele in lst:
    print(ele[0], ele[1])