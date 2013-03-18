def longest_palindrome_subsequence(x):
    n = len(x);
    reverse = x[::-1];
    print x;
    print reverse;
    lcps = [ [0 for i in range(n+1)] for j in range(n+1)];


    m = 0;
    longest_length = 0;

    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if(x[i] != reverse[j]):
                lcps[i][j] = 0;
            else:
                lcps[i][j] = lcps[i+1][j+1]+1;

            if(lcps[i][j]>longest_length):
                longest_length = lcps[i][j];
                m = i;
    print x[m:m+longest_length:];



def longest_palindrome_subsequence2(x):
    n = len(x);
    reverse = x[::-1];
    print x;
    print reverse;
    prev_lcps =  [0 for i in range(n+1)]; 


    m = 0;
    longest_length = 0;

    for i in range(n-1,-1,-1):
        for j in range(0,n):
            if(x[i] != reverse[j]):
                prev_lcps[j] = 0;
            else:
                prev_lcps[j] = prev_lcps[j+1]+1;

            if(prev_lcps[j]>longest_length):
                longest_length = prev_lcps[j];
                m = i;

    print m;
    print x[m:m+longest_length:];


