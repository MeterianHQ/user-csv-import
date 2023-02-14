class MeterianTeamsListReducer:
    def reduce(self, teams):
        reduced_teams = {}
        for team in teams:
            reduced_teams[team["name"]] = team["uuid"]

        return reduced_teams