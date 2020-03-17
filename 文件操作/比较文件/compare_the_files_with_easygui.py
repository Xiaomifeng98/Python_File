import easygui as g

#file compare function to give which rows are different_____________________________________
def file_compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0   #statistics rows
    differ = []     #Count the number of different rows

    for line1 in f1:
        line2 = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ

#choose the files you want to compare with the function of fileopenbox______________________
def choose_files():
    file_list = g.fileopenbox('Please choose the two files you want to compare,', default = '*.txt', multiple = True)
    if len(file_list) == 1:
        file_list.append(g.fileopenbox('Please select another file.', 'Tips', default = '*.txt', multiple = False))
        return file_list
    elif len(file_list) ==2:
        return file_list
    else:
        g.msgbox('Please select only two files.', 'Error')
        return 0

#main function______________________________________________________________________
while 1:
    file_list = choose_files()
    if(file_list == 0):
        pass
    else:
        differ = file_compare(file_list[0], file_list[1])
        break

if len(differ) == 0:
    g.msgbox('Both files are exactly the same.', 'Tips')
else:
    msg = 'There are ' +  str(len(differ)) + ' differences between the two files.\nThe differen rows are: ' + str(differ)
    g.msgbox(msg, title = 'Result')
