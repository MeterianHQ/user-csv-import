from sys import argv, exit
from src.CsvReader import CsvReader
from src.CsvToJsonParser import CsvToJsonParser
from src.MeterianAPI import MeterianAPI
from src.MeterianTeamsListReducer import MeterianTeamsListReducer
from src.MeterianMembersListReducer import MeterianMembersListReducer


class UserCsvImporter:
    def __init__(self):
        self.token = None
        self.input = None

    def main(self):
        self.parse_args()
        print("Authorizing Meterian Token")
        account = self.authorize_token()
        print("Getting Teams")
        teams = self.get_teams()
        print("%s teams acquired" % (len(teams)))
        teams = self.reduce_teams_list(teams)
        print("Parsing csv...")
        info = self.get_info(teams)
        print("Adding %s members to Meterian account" % (len(info))) 
        self.add_members(info, account["uuid"])
        print("Done!")

    def authorize_token(self):
        try:
            return MeterianAPI(self.token).accounts_me()
        except:
            import traceback
            traceback.print_exc()
            print("Error - Unauthorized!")
            exit(1)

    def get_teams(self):
        try:
            return MeterianAPI(self.token).get_teams()
        except:
            print("Error - Unauthorized!")
            exit(1)

    def reduce_teams_list(self, teams):
        return MeterianTeamsListReducer().reduce(teams)

    def get_info(self, teams):
        csv = CsvReader().read_file(self.input)
        return CsvToJsonParser().parse(csv, teams)

    def add_members(self, info, account_uuid):
        meterian=MeterianAPI(self.token)
        for entry in info:
            members = meterian.get_account_members(account_uuid)
            members = MeterianMembersListReducer().reduce(members)
            try:
                entry["uuid"] = members[entry["email"]]
            except:
                pass
            self.print_adding_email(entry)
            meterian.add_member_to_team(entry)

    def print_adding_email(self, entry):
        hashed_email = entry["email"].split("@")
        hashed_email[0] = hashed_email[0][:int(len(hashed_email[0])/2)]+"********"
        hashed_email = "@".join(hashed_email)
        print("Adding %s to team %s" % (hashed_email, entry["team_name"])) 

    def parse_args(self):
        for arg in argv:
            if "--input=" in arg:
                self.input = arg.split("=")[1]

            if "--meterian-token=" in arg or "--token=" in arg:
                self.token = arg.split("=")[1]


if __name__ == "__main__":
    UserCsvImporter().main()