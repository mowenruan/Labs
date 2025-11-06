def resample(series, tgt_length):
    """对 series 输入序列进行重采样，使得重采样后的长度等于 tgt_length
        注：请使用分段线性插值方法，假设 x0, x1, ... 依次是 0, 1, ...
        Args:
            series (List[float]): 对应函数值 y0, y1, ... 的一维实数序列（长度大于 0）
            tgt_length (int): 期望输出的序列长度（一定大于 0）
        Returns:
            ret (List[float]): 重采样后的一维序列
    """
    if len(series) == tgt_length:
        return series
    if tgt_length == 1:
        return [series[0]]
    if len(series) == 1:
        return [series[0]] * tgt_length
    resampled = []
    resampled.append(series[0])
    step = (len(series) - 1) / (tgt_length - 1)
    now = 1
    for i in range(1, tgt_length - 1):
        x =  i * step
        while x > now:
            now += 1
        resampled.append(series[now - 1] + (x - (now - 1)) * (series[now] - series[now - 1]))
    resampled.append(series[-1])
    return resampled


if __name__ == "__main__":
    import json
    series = json.loads(input())
    tgt_length = int(input())
    resampled_series = resample(series, tgt_length)
    print(json.dumps(resampled_series))