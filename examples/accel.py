def read_float_values_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    #extract the header line and split it to get the column names
    header = lines[0].strip().split()
    num_columns = len(header)
    column_lists = [[] for _ in range(num_columns)]

    #rows of values
    for line in lines[1:]:
        values = line.strip().split()
        for i, value in enumerate(values):
            column_lists[i].append(float(value))

    return dict(zip(header, column_lists))


def check_value(data):
    flag = True
    out_str = ""
    #lists of values for each target_qdd_i
    for key, value_list in data.items():
        #print(key) can remove 
        #print(value_list) can remove 
        #check for valid value of accel 
        for value in value_list:
            if value > 3:
                print(key + " Not Valid " + str(value))
                flag = False
        if flag == False:
            out_str = "Not Valid Accel"
        else:
            out_str = "Valid Accel"        
    return out_str 
        
