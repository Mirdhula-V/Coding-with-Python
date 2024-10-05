n = int(input())

l_space_count = n - 1 
l_space = " " * l_space_count
first_row = l_space + "*"
print(first_row)

m_space_count = -1
for i in range(2,n+1):
    l_space_count = n - i
    l_space = " " * l_space_count
    m_space_count = m_space_count + 2
    m_space = " " * m_space_count
    row = l_space + "*" + m_space + "*"
    print(row)

for i in range(1,n-1):
    l_space_count = i 
    l_space = " " * l_space_count
    m_space_count = m_space_count - 2 
    m_space = " " * m_space_count
    row = l_space + "*" + m_space + "*"
    print(row)

l_space_count = n - 1  
l_space = " " * l_space_count
last_row = l_space + "*"
print(last_row)