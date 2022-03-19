playesr = open('tennis.txt','w')
playesr.write('one\n')
playesr.write('two\n')
playesr.write('three\n')
playesr.write('four\n')
playesr.write('five\n')
playesr.close()

country = open('nonu.pdf', 'w')
print(playesr)
country.write("kjugcgjyyyfyujkjbmnfyyjk")
country.close()
n = open('tennis.txt','r')
pn = []
for l in n:
   pn.append(l[:-1])
print(pn)   
