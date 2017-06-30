
if __name__ == '__main__':
    count = 0
    f = open("resource.txt",'r')
    for line in f:
        words = line.split(' ')
        count += len(words)

    print("word count:{0}".format(count))