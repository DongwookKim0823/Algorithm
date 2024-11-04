def solution(plans):
    
    def convert_time(time_str):
        hour, time = map(int, time_str.split(':'))
        return hour * 60 + time

    convert_plan = list(map(lambda x: [x[0], convert_time(x[1]), int(x[2])], plans))
    convert_plan.sort(key=lambda x: -x[1])
    
    ongoing = []
    done = []
    while len(convert_plan) > 1:
        subject1, start_time1, remain_time1 = convert_plan.pop()
        subject2, start_time2, remain_time2 = convert_plan[-1]

        remain_time = remain_time1 - (start_time2 - start_time1)
        if remain_time > 0:
            ongoing.append([subject1, remain_time])
        else:
            done.append(subject1)
            
            available_time = (start_time2 - start_time1) - remain_time1
            
            while available_time > 0 and ongoing:
                subject, remain_time = ongoing.pop()
                if remain_time <= available_time:
                    done.append(subject)
                    available_time -= remain_time
                else:
                    ongoing.append([subject, remain_time - available_time])
                    available_time = 0
                            
    done.append(convert_plan[0][0])
    done.extend(map(lambda x: x[0], reversed(ongoing)))
    
    return done
