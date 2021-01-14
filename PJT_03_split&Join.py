# 빈칸을 기준으로 문자열 나누기
items = 'zero one tow three' . split()
print (items)

# ","을 기준으로 문자열 나누기
example = 'python,jquery,javascript'
example.split(",")
# 리스트 값을 a,b,c 변수로 packing
a,b,c = example.split(",")

print(a)
print(b)
print(c)
#"."을 기준으로 문자열 나누기
example = 'cSS.Error.Edu'
subdomain,domain,tld = example.split('.')

#############################################
colors = ['red','blue','green']
result = ''.join(colors)
print(result)

result = ' '.join(colors)
print(result)

result = ', '.join(colors)
print(result)

result = '-'.join(colors)
print(result)
