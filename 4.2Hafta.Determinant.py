matris_1=[[1,2],[3,4]]
matris_2=[[1,2,3],[4,5,6],[7,8,9]]
matris_3=[[13,2,3,4],[5,6,7,8],[92,10,31,42],[13,134,15,16]]

def determinant_2_2(m_1):
    s_1=m_1[0][0]*m_1[1][1]
    s_2=m_1[0][1]*m_1[1][0]
    s_3=s_1-s_2
    return s_3
print("2ye 2lik determinant: ",determinant_2_2(matris_1))
print()

def delete_row_col_from_matrix(m_1,m,n):
    result=[]
    size_1=len(m_1)
    size_2=len(m_1[0])

    for i in range(size_1):
        if(i==m):
            continue
        row_1=[]
        for j in range(size_2):
            if(j==n):
                continue
            row_1.append(m_1[i][j])
        result.append(row_1)

    return result
print(delete_row_col_from_matrix(matris_2,1,1))
print()

def det_3_3(m_1):
    a=m_1[0][0]*determinant_2_2(delete_row_col_from_matrix(m_1,0,0))
    b=m_1[0][1]*determinant_2_2(delete_row_col_from_matrix(m_1,0,1))
    c=m_1[0][2]*determinant_2_2(delete_row_col_from_matrix(m_1,0,2))
    det=a-b+c
    return det
print("3e3lük determinant: ",det_3_3(matris_2))
print()

def det_4_4(m_1):
    a=m_1[0][0]*det_3_3(delete_row_col_from_matrix(m_1,0,0))
    b=m_1[0][1]*det_3_3(delete_row_col_from_matrix(m_1,0,1))
    c=m_1[0][2]*det_3_3(delete_row_col_from_matrix(m_1,0,2))
    d=m_1[0][3]*det_3_3(delete_row_col_from_matrix(m_1,0,3))

    deta=a-b+c-d
    return deta
print(det_4_4(matris_3))