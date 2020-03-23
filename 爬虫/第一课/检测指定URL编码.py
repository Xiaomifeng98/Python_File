import urllib.request
import chardet

def main():
    url = input('Please input the URL: ')
    response = urllib.request.urlopen(url)
    html = response.read()

    #Identify webpage encoding
    encode = chardet.detect(html)['encoding']
    if encode == 'GB2312':
        encode = 'GBK'

    print('Encoding used on this page is %s' % encode)

if __name__ == '__main__':
    main()

