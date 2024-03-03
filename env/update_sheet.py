import vfvlib as v

start_number = 780
sts = v.ipt_gsheet(1).iloc[start_number:880]

tot_cnk = []
tot_anal = []
for i in range(len(sts)):
    ana_sts = v.structure_analysis_detail(sts[i+start_number])
    temp = ana_sts.split('\n')
    if temp[-1] == '':
        temp = temp[:-1]
    print(temp)
    n = 0
    cnk = []
    anal = []
    while n < len(temp)/2:
        cnk.append(temp[2*n])
        anal.append(temp[2*n + 1])
        n += 1

    tot_cnk.append(cnk)
    tot_anal.append(anal)
v.ipt_gsheet(3, 'chunk', 'A780:P900', tot_cnk)
v.ipt_gsheet(3, 'analysis', 'A780:P900', tot_anal)
