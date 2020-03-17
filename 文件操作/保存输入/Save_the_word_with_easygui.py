import easygui as g

def save_file(words):
    file_name = g.enterbox('Please input the file name: ', '')
    file_path = g.filesavebox(default = file_name)
    f = open(file_path, 'w')
    f.write(words)
    f.close()

def input_words():
    words = g.textbox('Please input the words what you want to save.', '')
    return words

save_file(input_words())

