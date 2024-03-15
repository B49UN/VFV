import vfvlib as v

start_number = int(input('start number: '))
end_number = int(input('end number: '))
sts = v.ipt_gsheet(1).iloc[start_number:end_number]

tot_cnk = []
tot_anal = []
tot_tense = []

for i in range(len(sts)):
    ana_sts = v.structure_analysis(sts[i+start_number])
    temp = ana_sts.split('\n')
    if temp[-1] == '':
        temp = temp[:-1]
    print(temp)
    n = 0
    cnk = []
    anal = []
    tense = [temp[-2], temp[-1]]

    temp = temp[:-3]

    while n < len(temp)/2:
        cnk.append(temp[2*n])
        anal.append(temp[2*n + 1])
        n += 1

    tot_cnk.append(cnk)
    tot_anal.append(anal)
    tot_tense.append(tense)

# should start from start_number + 2
update_start_number = str(start_number + 2)
update_end_number = str(end_number + 1)

update_range = 'A' + update_start_number + ':P' + update_end_number
v.ipt_gsheet(3, 'chunk', update_range, tot_cnk)
v.ipt_gsheet(3, 'analysis', update_range, tot_anal)
