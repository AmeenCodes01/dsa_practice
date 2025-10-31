def setZeroes(matrix):
    c = set()
    r= set()
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0 :
                # loop through all rows
                for i in range(len(matrix)):
                    matrix[i][col]=0
                matrix[row]=[0]*len(matrix[0])    
            continue
        continue
    
                
                
    
    # for row in range(len(matrix)):
    #     for col in range(len(matrix[0])):
    #         if row in r:
    #             matrix[row]=[0]*len(matrix[0])
    #         if col in c:
    #             matrix[row][col]=0
    print(matrix," matrix")
                
setZeroes([[1,1,1],[1,0,1],[1,1,1]])
