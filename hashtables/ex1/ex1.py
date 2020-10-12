def get_indices_of_item_weights(weights, length, limit):
    weight_cache = {}

    for i in range(length):
        complement = limit - weights[i]

        if complement in weight_cache:
            return (i, weight_cache[complement])
        weight_cache[weights[i]] = i
    return None
