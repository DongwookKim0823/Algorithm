def solution(id_list, report, k):
    
    answer = {}
    for i in id_list:
        answer[i] = 0
    
    report_cnt = {}
    report_dic = {}
    for i in report:
        a, b = i.split()
        if a in report_dic:
            if b in report_dic[a]:
                continue
            else:
                report_dic[a].append(b)
        else:
            report_dic[a] = [b]
    
    for i in report_dic:
        for j in report_dic[i]:
            if j in report_cnt:
                report_cnt[j] += 1
            else:
                report_cnt[j] = 1
    
    stoped_user = []
    for i in report_cnt:
        if report_cnt[i] >= k:
            stoped_user.append(i)
    
    for i in report_dic:
        for j in stoped_user:
            if j in report_dic[i]:
                answer[i] += 1 
    ans = []
    for i in answer:
        ans.append(answer[i])
    
    return list(answer.values())