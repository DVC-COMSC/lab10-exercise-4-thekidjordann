def main():
    ##################################################
    # Comlete your code here
    ##################################################
    str = 'Python Programming'
    sub1 = str[0:7]
    sub2 = str[7:]
    print (sub1)
    print (sub2)
    print (sub1 + sub2)

    coursename = 'Primary Programming'

    first = coursename[:7]
    second = coursename[8:]
    final = first +' ' + second

    print (first)
    print (second)
    print (final)

    coursename = 'Python Programming'

    letters = 'a b c d e f g'
    letters = letters.split()
    print (letters)
    print (letters[0])
    print (letters[1])
    print (letters[2])

    cname = 'C++ and Python and Java'
    cname.split('and')

    coursename = 'Python Programming'
    coursename = coursename.split()
    tab = '\n'
    cname = coursename[1] + tab + coursename[0]
    print (cname)

    pass


if __name__ == '__main__':
    main()
