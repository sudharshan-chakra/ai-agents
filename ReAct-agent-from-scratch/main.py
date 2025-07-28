from query_handler import query
import os

def main():
    if not os.getenv("GROQ_API_KEY"):
        print("Error: The GROQ_API_KEY environment variable is not set.")
        print("Please set it before running the script.")
        return
    
    print("--- Test 1: Wikipedia Tool ---")
    print("Question: Who was the director of the movie Inception, and what is the plot?")
    try:
        query("Who was the director of the movie Inception, and what is the plot?")
        print("\n--- Test 1 Complete ---\n")
    except Exception as e:
        print(f"An error occurred during Test 1: {e}")

    print("--- Test 2: Calculate Tool ---")
    print("Question: What is 100 divided by 25, multiplied by 3?")
    try:
        query("What is 100 divided by 25, multiplied by 3?")
        print("\n--- Test 2 Complete ---\n")
    except Exception as e:
        print(f"An error occurred during Test 2: {e}")

    print("--- Test 3: Multi-step with both tools ---")
    print("Question: According to Wikipedia, the film 'The Matrix' was released in 1999. How many years ago was that from today?")
    try:
        # This query requires the agent to first find the release year and then calculate the difference.
        query("According to Wikipedia, the film 'The Matrix' was released in 1999. How many years ago was that from today? We are in 2025")
        print("\n--- Test 3 Complete ---\n")
    except Exception as e:
        print(f"An error occurred during Test 3: {e}")

if __name__ == "__main__":
    main()