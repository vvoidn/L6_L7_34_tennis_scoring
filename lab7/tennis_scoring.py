
def parse_score(text):
    if not isinstance(text, str):
        raise ValueError("Score must be a string")

    parts = text.split('-')

    if len(parts) != 2:
        raise ValueError("Score must contain exactly two values")

    try:
        a, b = map(int, parts)
    except ValueError:
        raise ValueError("Score values must be integers")

    if a < 0 or b < 0:
        raise ValueError("Score values cannot be negative")

    return a, b


def game_lead(text):
    if not isinstance(text, str):
        raise ValueError("Game score must be a string")

    points = {'0': 0, '15': 1, '30': 2, '40': 3}

    parts = text.split('-')

    if len(parts) != 2:
        raise ValueError("Game score must contain two values")

    first, second = parts

    if first not in points or second not in points:
        raise ValueError("Invalid tennis point value")

    return points[first] - points[second]


def set_spread(games_csv):
    if not isinstance(games_csv, str):
        raise ValueError("Games must be provided as a string")

    parts = games_csv.split(',')

    if not parts or any(not g.strip() for g in parts):
        raise ValueError("Games list cannot contain empty values")

    try:
        games = [int(g.strip()) for g in parts]
    except ValueError:
        raise ValueError("Games must contain integers")

    if any(g < 0 for g in games):
        raise ValueError("Games cannot be negative")

    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    print("Spread:", result)


if __name__ == "__main__":
    main()
