# hello -> hello
# hellloooo -> hel3o4
# helllooooll -> hel3o4ll

# This solution doesn't work

def encode(input_str):
    if input_str is None:
        return None
    
    output = []
    
    record = {}
    flag = [] # record whether this position is a repetition, will reset when character changes
    
    # first pass, record repetition times of each character
    for p in range(0, len(input_str)):
        
        if input_str[p] in record:
            flag[p] = 0
            record[i] += 1
        else:
            record[i] = 1
    
    # second pass, iterater the record to decide what to output
    for k in record:
        if record[k] > 2:
            output.append("{0}{1}".format(k, record[k]))
        elif record[k] == 2:
            output.append("{0}{0}".format(k, k))
        else:
            output.append(k)
    
    return ''.join(output)