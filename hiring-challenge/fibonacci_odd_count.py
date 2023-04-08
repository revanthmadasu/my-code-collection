def count_odd_fibonacci(limit):
    series = [0, 1]
    odd_count = 1
    cur_len = 2
    while series[cur_len - 1] < limit:
        next_series_val = series[cur_len - 1] + series[cur_len - 2]
        if next_series_val >= limit:
            break
        series.append(next_series_val)
        cur_len += 1
        if next_series_val % 2 == 1:
            odd_count += next_series_val
    print(series)
    return odd_count


print(count_odd_fibonacci(10000))
print(count_odd_fibonacci(100))
