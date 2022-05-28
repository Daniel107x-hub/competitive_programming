def max_profit(prices):
    if len(prices) < 2:
        return 0
    min_value = prices[0]
    max_diff = prices[1] - prices[0]
    for i in range(1, len(prices)):
        diff = prices[i] - min_value
        if diff > max_diff:
            max_diff = diff
        if prices[i] < min_value:
            min_value = prices[i]
    if max_diff <= 0:
        max_diff = 0
    return max_diff

if __name__ == '__main__':
    prices = [int(n) for n in input().split(" ")]
    print(max_profit(prices))