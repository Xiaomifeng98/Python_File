import urllib.request
import chardet

def main():
    i = 0

    with open('urls.txt', 'r') as f:
        #Read the specified URL
        #Beacuse each line stores a URL, it is separated by newlines.
        urls = f.read().splitlines()

    for each_url in urls:
        response = urllib.request.urlopen(each_url)
        html = response.read()
        #Identify webpage encode.
        encode = chardet.detect(html)['encoding']
        if encode == 'GB2312':
            encode = 'GBK'
        i +=1
        filename = 'url_%d.txt' % i
        with open(filename, 'w', encoding = encode) as each_file:
            each_file.write(html.decode(encode, 'ignore'))

if __name__ == '__main__':
    main()

