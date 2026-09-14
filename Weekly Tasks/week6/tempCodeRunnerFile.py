def step_function(value):
    if value >= 0:
        return 1
    else:
        return 0

# Perceptron function
def perceptron(x1, x2, w1, w2, bias):
    # Calculate weighted sum
    weighted_sum = (x1 * w1) + (x2 * w2) + bias
    # Apply step function
    output = step_function(weighted_sum)
    return weighted_sum, output

# Weights and bias
w1 = 1
w2 = 1
bias = -1.5

# Test cases for AND gate
test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Test the perceptron
for x1, x2 in test_cases:
    weighted_sum, output = perceptron(x1, x2, w1, w2, bias
    )
    print("Input:", x1, x2, "| Weighted Sum:", weighted_sum, "| Output:", output)