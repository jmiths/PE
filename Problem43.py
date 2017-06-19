#!/usr/bin/python

div_two = {}
div_three = {}
div_five = {}
div_seven = {}
div_eleven = {}
div_thirteen = {}
div_seventeen = {}

score = 0

def finish(num):
    arr = [0] * 10
    for char in num:
        arr[int(char)] += 1
    for element in arr:
        if element > 1:
            return False
    for element in range(0,len(arr)):
        if arr[element] == 0:
            return int(str(element) + num)

def satanize(num):
    seen = {}
    #print num
    for element in num:
        if element not in seen:
            seen[element] = 0
        else:
            return False
    #print "I am returning true"
    return True

def add_to_dict(dicty,num):
    if (num[1]+num[2]) in dicty:
        dicty[num[1]+num[2]].append(num)
    else:
        dicty[num[1]+num[2]] = [num]

for i in range(10,1000):
    tmp = list(str(i))
    if i < 100:
        tmp.insert(0,'0')
    if satanize(tmp) == False:
        continue
    if i % 2 == 0:
        add_to_dict(div_two,tmp)
    if i % 3 == 0:
        add_to_dict(div_three,tmp)
    if i % 5 == 0:
        add_to_dict(div_five,tmp)
    if i % 7 == 0:
        add_to_dict(div_seven,tmp)
    if i % 11 == 0:
        add_to_dict(div_eleven,tmp)
    if i % 13 == 0:
        add_to_dict(div_thirteen,tmp)
    if i % 17 == 0:
        add_to_dict(div_seventeen,tmp)

#print div_three['63']
#print div_two['06']

for seventeen_key,seventeen_value in div_seventeen.iteritems():
    #print seventeen_key
    #print seventeen_value
    for seventeen_element in seventeen_value:
        tmp17 = seventeen_element
        if tmp17[0]+tmp17[1] in div_thirteen:
            for thirteen_element in div_thirteen[tmp17[0]+tmp17[1]]:
                tmp13 = thirteen_element
                if tmp13[0]+tmp13[1] in div_eleven:
                    for eleven_element in div_eleven[tmp13[0]+tmp13[1]]:
                        tmp11 = eleven_element
                        if tmp11[0]+tmp11[1] in div_seven:
                            for seven_element in div_seven[tmp11[0]+tmp11[1]]:
                                tmp7 = seven_element
                                if tmp7[0]+tmp7[1] in div_five:
                                    for five_element in div_five[tmp7[0]+tmp7[1]]:
                                        tmp5 = five_element
                                        if tmp5[0]+tmp5[1] in div_three:
                                            for three_element in div_three[tmp5[0]+tmp5[1]]:
                                                tmp3 = three_element
                                                if tmp3[0]+tmp3[1] in div_two:
                                                    for two_element in div_two[tmp3[0]+tmp3[1]]:
                                                        tmp2 = two_element
                                                        prospect =  ''.join(tmp2 + tmp7 + tmp17)
                                                        score += finish(prospect)
                



print score
'''
CURRENT STATUS DOESN'T SEEM TO READ WHOLE LIST.... PROGRAM CAN'T OUTPUT 406357289 which is in the orginal spec
'''
'''
for seventeen_key,seventeen_value in div_seventeen.iteritems():
    for seventeen_element in seventeen_value:
        tmp17 = seventeen_element
        if tmp17[0]+tmp17[1] in div_thirteen:
            for thirteen_element in div_thirteen[tmp17[0]+tmp17[1]]:
                #print tmp17
                #print thirteen_element
                tmp13 = tmp17[:]
                tmp13.insert(0,thirteen_element[0])
                #print tmp13
        #        if satanize(tmp13):
        #            continue
                if tmp13[0]+tmp13[1] in div_eleven:
                    for eleven_element in div_eleven[tmp13[0]+tmp13[1]]:
                        tmp11 = tmp13[:]
                        tmp11.insert(0,eleven_element[0])
    #                    print tmp11
        #                if satanize(tmp11):
        #                    continue
                        if tmp11[0]+tmp11[1] in div_seven:
                            for seven_element in div_seven[tmp11[0]+tmp11[1]]:
                                tmp7 = tmp11[:]
                                tmp7.insert(0,seven_element[0])
   #                             print tmp7
        #                        if satanize(tmp7):
        #                            continue
                                if tmp7[0]+tmp7[1] in div_five:
                                    for five_element in div_five[tmp7[0]+tmp7[1]]:
                                        tmp5 = tmp7[:]
                                        tmp5.insert(0,five_element[0])
  #                                      print tmp5
        #                                if satanize(tmp5):
        #                                    continue
                                        print "5Trying key5: " + tmp5[0]+tmp5[1]
                                        if tmp5[0]+tmp5[1] in div_three:
                                            for three_element in div_three[tmp5[0]+tmp5[1]]:
                                                tmp3 = tmp5[:]
                                                tmp3.insert(0,three_element[0])
       #                                         if satanize(tmp3):
       #                                             continue
                                            print "Trying key: " + tmp3[0]+tmp3[1]
                                            if tmp3[0]+tmp3[1] in div_two:
                                                print "My key is: " + tmp3[0]+tmp3[1]
                                                for two_element in div_two[tmp3[0]+tmp3[1]]:
                                                    print two_element
                                                    print tmp3
                                                    tmp2 = tmp3[:]
                                                    tmp2.insert(0,two_element[0])
#                                                    print tmp2
     #                                               if satanize(tmp3):
     #                                                   continue
      #                                              else:
#                                                    print tmp2
            
#        for thirteen_key,thirteen_value in div_thirteen.iteritems():
#            for thirteen_element in thirteen_value:
#                for eleven_key,eleven_value in div_eleventeen.iteritems():
#                    for eleven_element in eleven_value:
#                        for seven_key,seven_value in div_seven.iteritems():
#                            for seven_element in seven_value:
#                                for five_key,five_value in div_five.iteritems():
#                                    for five_element in five_value:
#                                        for three_key,three_value in div_three.iteritems():
#                                            for three_element in three_value:
#                                                for two_key,two_value in div_two.iteritems():
#    for two_value in two_value:
'''
