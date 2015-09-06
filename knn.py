from math import sqrt

def load_data():
    return [[3,104,1],[2,100,1],[1,81,1],[101,10,2],[99,5,2],[98,2,2]]

def calc_distance(sample1,sample2):
    return sqrt((sample1[0] - sample2[0])**2 + (sample1[1] - sample2[1])**2)

def knn(k,sample):
    train_data = load_data()
    distances = [[calc_distance(sample,[x,y]),z] for x,y,z in train_data]
    distances.sort()
    k_samples = distances[0:k]
    k1_samples = [x for x in k_samples if x[1]==1]
    k2_samples = [x for x in k_samples if x[1]==2]
    k1_len = len(k1_samples)
    k2_len = len(k2_samples)
    sample_class = [2,1][k1_len > k2_len]
#    train_data_tuple = tuple(train_data)
    print "%d neighbors. %d CLASS 1 neighbors, %d CLASS 2 neighbors." % (len(k_samples),k1_len,k2_len)
    print "the sample [%d,%d] may be CLASS %d." % (sample[0],sample[1],sample_class)
    return sample_class

def run():
    knn(3,[50,50])

run()
