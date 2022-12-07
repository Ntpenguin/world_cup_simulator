import random

odds = {
"Brazil": 2.50,
"Germany": 3.00,
"Spain": 4.00,
"France": 5.00,
"Argentina": 6.00,
"Belgium": 7.00,
"England": 8.00,
"Portugal": 9.00,
"Uruguay": 10.00,
"Croatia": 11.00,
"Colombia": 12.00,
"Mexico": 13.00,
"Sweden": 14.00,
"Denmark": 15.00,
"Russia": 16.00,
"Poland": 17.00,
"Japan": 18.00,
"Switzerland": 19.00,
"Peru": 20.00,
"Senegal": 21.00,
"Nigeria": 22.00,
"Serbia": 23.00,
"Egypt": 24.00,
"Iran": 25.00,
"Costa Rica": 26.00,
"South Korea": 27.00,
"Tunisia": 28.00,
"Australia": 29.00,
"Morocco": 30.00
}

teams = list(odds.keys())

num_matches = 64

winnings = {}
for team in teams:
    winnings[team] = 0

for match in range(num_matches):
# Randomly select two teams to play against each other
    team1 = random.choice(teams)
    team2 = random.choice(teams)
    while team1 == team2:
        team2 = random.choice(teams)

# Calculate the probability of each team winning based on their odds
prob1 = 1 / odds[team1]
prob2 = 1 / odds[team2]
total_prob = prob1 + prob2
prob1 /= total_prob
prob2 /= total_prob

# Randomly determine the winner of the match based on their probabilities
if random.uniform(0, 1) < prob1:
    # Team 1 wins and receives winnings based on their odds
    winnings[team1] += 100 * odds[team1]
else:
    # Team 2 wins and receives winnings based on their odds
    winnings[team2] += 100 * odds[team2]
sorted_teams = sorted(teams, key=lambda x: winnings[x], reverse=True)

print("Final places:")
for i, team in enumerate(sorted_teams):
    print(f"{i+1}: {team}")

winner = sorted_teams[0]
print(f"\nThe winner of the tournament is {winner} with ${winnings[winner]:.2f} in winnings. How much you would make if you bet 100 dollars!")