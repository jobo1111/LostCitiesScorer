def score(expedition):
    multiplier = 1
    total = -20
    extra = 20 if len(expedition) >= 8 else 0
    if len(expedition) == 0:
        return 0
    for card in expedition:
        if card.lower() == "w":
            multiplier += 1
        else:
            try:
                total += int(card)
            except:
                print("Invalid card entered, score may not be accurate")
    return (total * multiplier) + extra



def main():
    places = ["volcano", "mountain", "sea", "arctic", "desert"]
    extended = input("Playing extended?(Y/N) ").lower() == "y"
    if extended:
        places.append("space")
    player_scores = [0,0]

    for i in range(3):
        print(f"\nScoring for round {i+1}\n")
        player_scores_per_round = [0,0]
        for j in range(2):
            print(f"Enter the points for player {j+1}")
            for place in places:
                expedition = input(f"Enter cards for your trip to the {place}: ").split()
                points_earned = score(expedition)
                player_scores_per_round[j] += points_earned
                print(f"You earned {points_earned} for your trip to the {place}\n")
        print(f"Scores for round {i+1} are \nPlayer 1: {player_scores_per_round[0]}\nPlayer 2: {player_scores_per_round[1]}")
        player_scores[0] += player_scores_per_round[0]
        player_scores[1] += player_scores_per_round[1]
    print(f"\nFinal scores are \nPlayer 1: {player_scores_per_round[0]}\nPlayer 2: {player_scores_per_round[1]}")
    print(f"\nThe winner is Player {'1' if player_scores[0] > player_scores[1] else '2'}")

if __name__ == '__main__':
    main()
