
a = 1000
d = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
w = ['圆', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿']
Z = [('零仟', '零佰', '零拾', '零零零', '零零', '零亿', '零万', '零圆'),
     ('零', '零', '零', '零', '零', '亿', '万', '圆')]
num = str(abs(a))
s = ''
for i, x in enumerate(num):
    s += d[int(x)] + w[len(num)-i-1]
for z, v in zip(Z[0], Z[1]):
    s = s.replace(z, v)
if a == 0:
    s = '零圆'
if a < 0:
    s = '负'+s
print(s)
