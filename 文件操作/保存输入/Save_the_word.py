def file_write(file_name):
    f = open(file_name, 'w')
    print('Please input the words(input \':w\' to end. ) : ')

    while True:
        word_input = input()
        if word_input != ':w':
            f.write('%s\n' %  word_input)
        else:
            break

    f.close()

file_name = input('Please input the file name: ')
file_write(file_name)
