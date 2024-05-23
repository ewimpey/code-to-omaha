import json

def prompt_user_for_winner(prompt, options):
    while True:
        print(prompt)
        for idx, team in enumerate(options, 1):
            print(f"{idx}. {team}")
        try:
            choice = int(input("Enter the number corresponding to the team: ").strip())
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Bzzz. Wrong. Try a valid selection bub.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def prompt_user_for_runner_up(prompt, options, winner):
    while True:
        print(prompt)
        #for idx, team in enumerate(options, 1):
        #    print(f"{idx}. {team}")
        try:
            choice = int(input("Enter the number corresponding to the team: ").strip())
            if 1 <= choice <= len(options):
                runner_up = options[choice - 1]
                if runner_up != winner:
                    return runner_up
                else:
                    print("Yo, you have them winning! Gotta pick a different runner-up.")
            else:
                print("Bzzz. Wrong. Try a valid selection bub.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def fill_regional(regionals):
    for key, regional in regionals.items():
        print(f"Filling out {key}...")
        teams = [regional["team1"], regional["team2"], regional["team3"], regional["team4"]]
        regional["winner"] = prompt_user_for_winner(f"Enter winner for {key}:", teams)
        regional["runner_up"] = prompt_user_for_runner_up(f"Enter runner-up for {key}:", teams, regional["winner"])

def fill_super_regionals(super_regionals, regionals):
    for i, (key, matchup) in enumerate(super_regionals.items(), start=1):
        print(f"Filling out {key}...")
        team1_key = f"regional{i}"
        team2_key = f"regional{17-i}"
        matchup["team1"] = regionals[team1_key]["winner"]
        matchup["team2"] = regionals[team2_key]["winner"]
        options = [matchup["team1"], matchup["team2"]]
        matchup["winner"] = prompt_user_for_winner(f"Enter winner for {key} ({matchup['team1']} vs {matchup['team2']}):", options)

def fill_cws(cws, super_regionals):
    bracket1_teams = []
    bracket2_teams = []
    for i in range(1, 5):
        bracket1_teams.append(super_regionals[f"super{i}"]["winner"])
    for i in range(5, 9):
        bracket2_teams.append(super_regionals[f"super{i}"]["winner"])
    
    cws["cws1"]["team1"], cws["cws1"]["team2"], cws["cws1"]["team3"], cws["cws1"]["team4"] = bracket1_teams
    cws["cws2"]["team1"], cws["cws2"]["team2"], cws["cws2"]["team3"], cws["cws2"]["team4"] = bracket2_teams

    print("Filling out CWS1...")
    cws["cws1"]["winner"] = prompt_user_for_winner(f"Enter winner for CWS1:", bracket1_teams)
    cws["cws1"]["runner_up"] = prompt_user_for_runner_up(f"Enter runner-up for CWS1:", bracket1_teams, cws["cws1"]["winner"])
    
    print("Filling out CWS2...")
    cws["cws2"]["winner"] = prompt_user_for_winner(f"Enter winner for CWS2:", bracket2_teams)
    cws["cws2"]["runner_up"] = prompt_user_for_runner_up(f"Enter runner-up for CWS2:", bracket2_teams, cws["cws2"]["winner"])

def fill_finals(finals, cws):
    print("Filling out finals...")
    finals["team1"] = cws["cws1"]["winner"]
    finals["team2"] = cws["cws2"]["winner"]
    options = [finals["team1"], finals["team2"]]
    finals["winner"] = prompt_user_for_winner(f"Enter winner for finals ({finals['team1']} vs {finals['team2']}):", options)

def main():
    username = input("What is your GitHub username? (This will be used to save your bracket with the correct filename): ").strip()
    
    with open('initial-bracket.json', 'r') as f:
        bracket = json.load(f)

    fill_regional(bracket["regionals"])
    fill_super_regionals(bracket["supers"], bracket["regionals"])
    fill_cws(bracket["cws"], bracket["supers"])
    fill_finals(bracket["finals"], bracket["cws"])

    output_filename = f"{username}-submission.json"
    with open(output_filename, 'w') as f:
        json.dump(bracket, f, indent=4)

    print(f"Bracket has been filled and saved to {output_filename}")

if __name__ == "__main__":
    main()
