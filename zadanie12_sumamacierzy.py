import random

size = 128

m_1 = []
m_2 = []
m_sum = []

for i in range(0,size):
	m_1.append([])
	m_2.append([])
	for j in range(0,size):
		m_1[i].append(int(round(random.random()*100)))
		m_2[i].append(int(round(random.random()*100)))

for i in range(0,size):
	m_sum.append([])
	for j in range(0,size):
		m_sum[i].append(m_1[i][j] + m_2[i][j])
print(m_1)
print(m_2)
print(m_sum)
