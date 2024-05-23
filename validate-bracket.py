import json
import sys

def load_bracket(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_teams(teams, winner, runner_up=None):
    if len(teams) != len(set(teams)):
        return False, "Teams are not distinct."
    if winner not in teams:
        return False, f"Winner {winner} is not in the team list."
    if runner_up and runner_up not in teams:
        return False, f"Runner-up {runner_up} is not in the team list."
    if runner_up and winner == runner_up:
        return False, "Winner and runner-up cannot be the same team."
    return True, "Teams are valid."

def validate_regionals(regionals):
    if len(regionals) != 16:
        return False, "There should be 16 regionals."
    for regional in regionals.values():
        required_keys = [f"team{i+1}" for i in range(4)] + ["winner", "runner_up"]
        for key in required_keys:
            if key not in regional:
                return False, f"Regional is missing required key: {key}"
        teams = [regional[f"team{i+1}"] for i in range(4)]
        winner = regional["winner"]
        runner_up = regional["runner_up"]
        valid, msg = validate_teams(teams, winner, runner_up)
        if not valid:
            return False, f"Regional validation failed: {msg}"
    return True, "All regionals are valid."

def validate_supers(supers):
    if len(supers) != 8:
        return False, "There should be 8 supers."
    for super in supers.values():
        required_keys = ["team1", "team2", "winner"]
        for key in required_keys:
            if key not in super:
                return False, f"Super is missing required key: {key}"
        teams = [super["team1"], super["team2"]]
        winner = super["winner"]
        valid, msg = validate_teams(teams, winner)
        if not valid:
            return False, f"Super validation failed: {msg}"
    return True, "All supers are valid."

def validate_cws(cws):
    if len(cws) != 2:
        return False, "There should be 2 CWS."
    for cws_round in cws.values():
        required_keys = [f"team{i+1}" for i in range(4)] + ["winner", "runner_up"]
        for key in required_keys:
            if key not in cws_round:
                return False, f"CWS is missing required key: {key}"
        teams = [cws_round[f"team{i+1}"] for i in range(4)]
        winner = cws_round["winner"]
        runner_up = cws_round["runner_up"]
        valid, msg = validate_teams(teams, winner, runner_up)
        if not valid:
            return False, f"CWS validation failed: {msg}"
    return True, "All CWS rounds are valid."

def validate_finals(finals):
    required_keys = ["team1", "team2", "winner"]
    for key in required_keys:
        if key not in finals:
            return False, f"Finals are missing required key: {key}"
    teams = [finals["team1"], finals["team2"]]
    winner = finals["winner"]
    valid, msg = validate_teams(teams, winner)
    if not valid:
        return False, f"Finals validation failed: {msg}"
    return True, "Finals are valid."

def validate_bracket(file_path):
    try:
        bracket = load_bracket(file_path)
    except Exception as e:
        return False, f"Error loading bracket: {e}"

    valid, msg = validate_regionals(bracket.get("regionals", {}))
    if not valid:
        return False, msg

    valid, msg = validate_supers(bracket.get("supers", {}))
    if not valid:
        return False, msg

    valid, msg = validate_cws(bracket.get("cws", {}))
    if not valid:
        return False, msg

    valid, msg = validate_finals(bracket.get("finals", {}))
    if not valid:
        return False, msg

    return True, "Bracket is valid."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_bracket.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    valid, message = validate_bracket(file_path)
    if not valid:
        print(message)
        sys.exit(1)
    print(message)
