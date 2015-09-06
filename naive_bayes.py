def load_dataset():
    return [['a','A',1],['a','B',2],['b','C',3],['b','C',1],['a','D',1],['b','D',3]]

def naive_bayes(data,t_sample):
    data_num = len(data)
    symptom,job,disease = t_sample
    selected_data = [[x,y,z] for x,y,z in data if (z == disease)]
    s_data_num = len(selected_data)
    p_d = float(s_data_num) / data_num
    p_s_d = len([x for x,y,z in selected_data if (x == symptom)]) / float(s_data_num)
    p_j_d = len([y for x,y,z in selected_data if (y == job)]) / float(s_data_num)
    p_s = len([x for x,y,z in data if (x==symptom)]) / float(data_num)
    p_j = len([y for x,y,z in data if (y==job)]) / float(data_num)
    
    print p_d,p_s_d,p_j_d,p_s,p_j
    return p_s_d*p_j_d*p_d / (p_s * p_j)

def run():
    data = load_dataset()
    t_sample = ['a','C',1]
    p = naive_bayes(data,t_sample)
    print "p is %f.\n" % p

run()
