#!/usr/bin/env python3


MAX_TIPP = 440 * 1000000


def M_numbers(upto):
    input_length = len(str(upto))
    pre_calc = [0] + [i**i for i in range(1,10)]
    pre_calc_length = [ len(str(i)) for i in pre_calc ]
    index_length_limit = [-1, 2, 3, 4, 5, 6, 7, 7, 8, 9 ]  #megfelelő hosszú szó melyik számot veheti fel anélkül, hogy túlcsordulna
    curr_value = [0 for i in range(input_length)]
    result = []
    
    for curr_index in range(1,input_length+1):
        while curr_value[input_length - curr_index] != index_length_limit[curr_index] and T_calc(curr_value) < upto:
            limit = index_length_limit[curr_index]+1
            #print(curr_index, curr_value)
            if  limit in curr_value:
                temp_index = curr_value.index(limit)
                curr_value[temp_index - 1] += 1
                curr_value[temp_index] = 0
            else:
                if T_calc(curr_value) == M_calc(curr_value, pre_calc):
                    result.append(int(''.join([str(i) for i in curr_value])))
                curr_value[input_length-1] += 1
            
    return result
        
        
            
def M_calc(lm, pre_calc):
    sum = 0
    for e in lm:
        sum += pre_calc[e]
    return sum
    
    
def T_calc(li):
    sum = 0
    for e in enumerate(li):
        sum += e[1] * 10 ** (len(li)-1-e[0])
    return sum


def main():
    #print(M_numbers(10000))
    print(M_numbers(MAX_TIPP))


if __name__ == "__main__":
    main()
