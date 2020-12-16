
import sys
import json

def transition(total_tag,data):
    t_prob = {}
    for tags in total_tag:
        t_prob[tags] = {}
    for line in data:
        for i in range(len(line)+1): 
            if i==0:
                t = line[i].split('/')[-1]
                if 'START' not in t_prob[t]: 
                    t_prob[t]['START'] = 1
                else:
                    t_prob[t]['START'] += 1
            elif i==len(line):

                t2 = line[i-1].split('/')[-1]

                if t2 not in t_prob['EOS']:
                    t_prob['EOS'][t2] = 1
                else:
                    t_prob['EOS'][t2] += 1                
            else:
                t = line[i].split('/')[-1]
                t2 = line[i-1].split('/')[-1]
                if t2 not in t_prob[t]:
                    t_prob[t][t2] = 1
                else:
                    t_prob[t][t2] += 1
    return t_prob

def trans_smoothing(t_prob,total_tag):
    for cur_tag in t_prob:
        for prev_tag in total_tag:
            if prev_tag == 'EOS':
                continue
        
            elif prev_tag not in t_prob[cur_tag]:
                t_prob[cur_tag][prev_tag] = 1/(total_tag[prev_tag]+(len(total_tag))+1)
            else:
                t_prob[cur_tag][prev_tag] = (t_prob[cur_tag][prev_tag]+1)/(total_tag[prev_tag]+(len(total_tag))+1)
    return t_prob       

def emission(tag, word_tag):
    e_prob = {}
    for tag in word_tag:
        for word in word_tag[tag]:
            if word not in e_prob:
                e_prob[word] = {}
            if tag not in e_prob[word]:
                e_prob[word][tag] = word_tag[tag][word]/total_tag[tag]


    
    return e_prob


def smoothing(s_p):
    s_p = sorted(s_p, key=lambda k: len(s_p[k]), reverse=True)
    return s_p[0:4]
    

def read(train_files):
    file = open(train_files)
    data = []
    for line in file:
        a = line.strip('\n').split()
        data.append(a)

    return data




total_tag = {}
word_tag = {}
s_p = {}
train_files = sys.argv[1]
data = read(train_files)   

total_tag['START'] = len(data)
total_tag['EOS'] = len(data)


for line in data:
    for words in line:
        temp = words.split('/')
        tag = temp[-1]
        word = temp[:-1]
        key = word
        word = '/'.join(word)
        
        if tag not in total_tag:
            total_tag[tag] = 1
        else:
            total_tag[tag]+=1
        if tag not in word_tag:
            word_tag[tag] = {}
        if word not in word_tag[tag]:
            word_tag[tag][word] = 1
        else:
            word_tag[tag][word]+=1
         
        if tag not in s_p:
            s_p[tag] = []
        if key[0] not in s_p[tag]:
            s_p[tag].append(key[0])
        
            





smoothing = smoothing(s_p)
e_prob = emission(tag, word_tag)
t_prob = transition(total_tag,data)
t_prob = trans_smoothing(t_prob,total_tag)

ans = { 'transition': t_prob, 'emission': e_prob, 's_p': smoothing,'tags': total_tag}            

with open('hmmmodel.txt','w') as file:
    file.write(json.dumps(ans))
    file.close()