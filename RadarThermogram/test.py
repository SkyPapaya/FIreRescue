# 输入字符串
position_str = "-2.1,1.3; 0,0 ; 0,0 ; 0,0 ; 0,0 ;"

# 移除多余的空格并用分号分割字符串
parts = [part.strip() for part in position_str.split(';') if part.strip()]

# 初始化两个空数组
before_comma = []
after_comma = []

# 遍历分割后的每一部分，并按逗号分开
for part in parts:
    before, after = part.split(',')
    before_comma.append(float(before))
    after_comma.append(float(after))


