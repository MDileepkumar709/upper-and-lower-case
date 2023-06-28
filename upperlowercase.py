def string_test(s):
  
    upper_case=0
    lower_case=0
    for i in s:
        if i.isupper():
       
         upper_case+=1
        elif i.islower():
      
         lower_case+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", upper_case)
    print ("No. of Lower case Characters : ", lower_case )

string_test('The quick Brow Fox')
