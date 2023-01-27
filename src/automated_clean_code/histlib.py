# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse


# method to get args
def get_args() -> argparse.Namespace:
    """Get args."""
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("fname", metavar="N", type=str, help="filename to compute the histogram")
    return parser.parse_args()


def create_counter_hist(lines: list[str]) -> dict:
    """Create counter histogram.

    Args:
        lines (list[str]): line by line list

    Returns:
        dict: counter histogram
    """
    counter = {}

    for line in lines:
        line = line.strip()
        if line in counter:
            counter[line] += 1
        else:
            counter[line] = 1
    return counter


def find_min_counter(counter: dict) -> tuple:
    """Find min key and min counter.

    Args:
        counter (dict): counter histogram

    Returns:
        tuple: min key and min counter
    """
    min_key = None
    min_counter = 0
    for k, v in counter.items():
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v
    return min_key, min_counter


def find_max_counter(counter: dict) -> tuple:
    """Find max key and max counter.

    Args:
        counter (dict): counter histogram

    Returns:
        tuple: max key and max counter
    """
    max_key = None
    max_counter = 0
    for k, v in counter.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v
    return max_key, max_counter


def main():
    """Find min and max with counter."""
    args = get_args()
    lines = []

    with open(args.fname, "r") as f:
        for line in f:
            lines.append(line)

    counter = create_counter_hist(lines)

    min_key, min_counter = find_min_counter(counter)
    max_key, max_counter = find_max_counter(counter)

    print(f"Min Key = {min_key} with count = {min_counter}")
    print(f"Max Key = {max_key} with count = {max_counter}")


if __name__ == "__main__":
    main()
