#Напишіть програму яка перевіряє чи стрічка містить лише великі і малі літери, числа та нижнє підкреслення.
import re
demo_str = 'asdfsdfasfasfdSGSADGAGSDGASG'
pattern = (r'\w+')
result = re.fullmatch(pattern, demo_str)
print (result)


#Напишіть програму, що видаляє область дужок в стрічці
#["example (.com)", "github (.com)", "stackoverflow (.com)"] ->example

demo_str1 ='[ "github (.com)"]'
result = (re.sub(r'\(.*\)', "", demo_str1))
print(result)

#Напишіть програму, що. вставляє пробіл перед великою літерою
demo_str2 = 'my name isInna'
result = (re.sub('([A-Z])', r' \1', demo_str2))
print(result)

