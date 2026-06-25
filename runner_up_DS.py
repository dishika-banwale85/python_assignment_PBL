def find_runner_up_score(scores):
    # 1. Convert to a set to remove duplicate scores
    unique_scores = set(scores)
    
    # 2. Remove the maximum score to find the runner-up
    unique_scores.remove(max(unique_scores))
    
    # 3. The new maximum is the runner-up score
    return max(unique_scores)

# Example usage:
if __name__ == "__main__":
    sample_input = [2, 3, 6, 6, 5]
    result = find_runner_up_score(sample_input)
    print(f"Runner-up score: {result}")