import sys
import json

def read_algo():
    a = open('hmmmodel.txt', 'r').read()
    m = json.loads(a)
    return m

def read_data(file_name):
    f = open(file_name, 'r').read()
    data = f.splitlines()
    return data




def first_word(one):
    s = {}
    w = one
    if w not in emission.keys():
        s = s_p
    else:
        s = emission[w]
    for tag in s:
        if tag == 'START' or tag=='EOS':
            continue
        elif w in emission:
            p = emission[w][tag]
        else:
            p = 1  
        update(0,transition[tag]['START'] * p,'START',tag)
        
    





def last_word(l):
    
    s = l.keys()
    ans_p ={'no':0,'back_point':''}
    algo.append({})
    for tag in s:
        if tag !='EOS':
            prev = transition['EOS'][tag] *  algo[-2][tag]['no'] 
            if (prev>ans_p['no']):
                ans_p['no'] = prev
                ans_p['back_point'] = tag
            
        else:
            continue
           
    update(-1,ans_p['no'],ans_p['back_point'],'EOS')
   





def middle_word(i):
    cur = line_word[i]
    algo.append({})
    if cur not in emission:
       
        s = s_p
    else:
        s = emission[cur]
        
    for tag in s:
        if tag=='START' or tag=='EOS':
            continue
        elif cur in emission:
            p = emission[cur][tag]
        else:
            p = 1  
        ans_p ={'no':0,'back_point':''}

        for l in algo[i-1]:
            if l=='START' or l=='EOS':
                continue
            else:
                prev =  transition[tag][l]  * p * algo[i-1][l]['no']

                if(prev>ans_p['no']):
                    ans_p['no'] = prev
                    ans_p['back_point'] = l
        update(i,ans_p['no'],ans_p['back_point'],tag)
        

def update(i,a,b,tag):
    algo[i][tag] = {}
    algo[i][tag]['no'] = a
    algo[i][tag]['back_point'] = b
    
def write_data(ans):
    with open('hmmoutput.txt', 'w') as file:
        for line in ans:
            file.write(line)
        file.close()

        
learb = read_algo()
file_name = sys.argv[1]
data = read_data(file_name)
transition = learb['transition']
emission = learb['emission']
tag_total = learb['tags']
s_p = learb['s_p']
ans = []


for line in data:
    line_word = line.split()
    algo = []
    algo.append({}) 
    for i in range(0,len(line_word)+1):
        
        if i==len(line_word):
            last_word(algo[-1]) 
        elif i == 0:
            first_word(line_word[0])
        else:  
            middle_word(i)
    
    k = ""
    s = len(line_word)
    t = 'EOS'
    j = len(line_word)-1
    while j>=0:
        temp = line_word[j]+"/"+algo[s][t]['back_point'] 
        k = temp+ " " + k
        j = j-1
        t = algo[s][t]['back_point']
        s = s-1
    k = k +'\n'
    ans.append(k)

write_data(ans)               

    

