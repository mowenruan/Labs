def get_significant_figure(ref, est):

    """计算实数估计值 est 相对于实数参考值 ref 的有效数字位数

         注：应支持负数情况。【可选】支持 1.5e-3 科学计数法形式的输入

    Args:

        ref (str): 实数参考值的字符串形式

        est (str): 实数估计值的字符串形式

    Returns:

        n (int): 有效数字位数

    """
    def to_normal(s):
        flag = 0 #符号位
        value = '' #数值部分
        new_exponent = 0 #指数部分
        # 处理符号
        if s[0] == '-':
            s = s[1:]
            flag = -1
        else:
            flag = 1
        # 处理科学计数法
        if 'e' in s or 'E' in s:
            value = s.split('e' if 'e' in s else 'E')[0]
            power = int(s.split('e' if 'e' in s else 'E')[1])
        else:
            value = s
            power = 0
        value = value.strip().lstrip('0')
        # 处理小数点
        if '.' in value:
            #寻找小数点位置
            dot_index = value.index('.')
            #去掉小数点
            value = value.replace('.','')
            #寻找第一个非零数字位置
            index = 0
            for i in range(len(value)):
                if(value[i]!='0'):
                    index=i
                    value=value[i:]
                    break
            #计算小数点移动后的指数
            new_exponent = power + (dot_index - index - 1)
        else:
            #寻找第一个非零数字位置
            index = 0
            for i in range(len(value)):
                if(value[i]!='0'):
                    index=i
                    value=value[i:]
                    break
            new_exponent = power + len(value) - 1
        return flag,value,new_exponent
  
    ref_flag,ref_value,ref_exponent = to_normal(ref)
    est_flag,est_value,est_exponent = to_normal(est)
    len_ref = len(ref_value)
    len_est = len(est_value)
    if len_ref > len_est:
        est_value = est_value + '0' * (len_ref - len_est)
    elif len_est > len_ref:
        ref_value = ref_value + '0' * (len_est - len_ref)
    ref_value = int(ref_value)
    est_value = int(est_value)
    len_num = len(str(ref_value))
    #print(ref_flag,ref_value,ref_exponent)
    #print(est_flag,est_value,est_exponent)
    # 保持一样的数量级
    exponent = min(est_exponent,ref_exponent)
    ref_value = ref_value * (10 ** (ref_exponent - exponent))
    est_value = est_value * (10 ** (est_exponent - exponent))
    # 符号
    if ref_flag == -1:
        ref_value = -ref_value
    if est_flag == -1:
        est_value = -est_value
    # 计算差
    diff = abs(ref_value - est_value)
    # 计算差的科学计数法指数
    diff_exponent = exponent - (len_num - 1) + (len(str(diff)) - 1)
    if diff == 0:
        return  min(len_ref,len_est)
    #print(diff, diff_exponent)
    # diff_exponent = est_exponent - n 
    # 计算有效数字位数
    diff = str(diff)
    if diff[0] < '5':
        n = est_exponent - diff_exponent
    elif diff[0] == '5' and diff.rstrip("0") == "5":
        n = est_exponent - diff_exponent
    else:
        n = est_exponent - diff_exponent - 1
    return min(max(n, 0), len_ref)

if __name__ == "__main__":

    # 可自行在此代码块下面添加更多测试样例
    assert get_significant_figure("3.1415926", "3.1415") == 4
    assert get_significant_figure("0.001234", "0.00123") == 3

    
    
   
    
    