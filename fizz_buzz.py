class Solution:
    """
    Implements the FizzBuzz problem using a configurable set of divisors and words.

    The `fizzBuzz` function takes an integer `n` and a dictionary `config` that maps divisors to words. It returns a list of strings, where each string represents the value at that index (1-indexed) according to the following rules:

    - If the index is divisible by any key in `config`, the corresponding value from `config` is used.
    - If the index is not divisible by any key in `config`, the string representation of the index is used.

    The function is designed to be flexible and configurable, allowing the FizzBuzz behavior to be customized by providing a different `config` dictionary.
    """

    def fizzBuzz(self, n: int, config: dict) -> list[str]:
        """
        Runs the FizzBuzz algorithm with the provided configuration.

        Args:
            n (int): The upper bound for the FizzBuzz algorithm.
            config (dict): A dictionary mapping numbers to their corresponding string values.

        Returns:
            list: A list of strings representing the FizzBuzz output for the given range.
        """
        # for storing the result
        result = []

        for i in range(1, n + 1):
            entry = ""
            for divisor, word in config.items():
                if i % divisor == 0:
                    entry += word

            if not entry:
                entry = str(i)

            result.append(entry)

        return result
    


solution = Solution()
config = {
    3: "Fizz",
    5: "Buzz"
}
print(solution.fizzBuzz(15, config))
