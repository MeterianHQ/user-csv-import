import requests
import json

class MeterianAPI:
    def __init__(self, token):
        self.token = token

    def accounts_me(self):
        try:
            req = requests.get("https://www.meterian.io/api/v1/accounts/me", headers={
                "Authorization": "token %s" % (self.token)
            })
            if req.status_code != 200:
                raise ValueError("Unauthorized")
            
            return json.loads(req.text)
        except:
            raise ValueError("Unauthorized")
            

    def get_teams(self):
        req = requests.get("https://www.meterian.io/api/v1/teams", headers={
            "Authorization": "token %s" % (self.token)
        })

        if req.status_code != 200:
            print(req.text)
            raise ValueError("Server rejected request")
        
        return json.loads(req.text)

    def get_account_members(self, account_uuid):
        req = requests.get("https://www.meterian.io/api/v1/teams/%s/members" % (account_uuid), headers= {
            "Authorization": "token %s" % (self.token)
        })
        if req.status_code != 200:
            print(req.text)
            raise ValueError("Server rejected request")
        
        return json.loads(req.text)

    def add_member_to_team(self, info):
        body = {
            "membership": {
                "email": info["email"],
                "name": info["full_name"],
                "role": "Viewer",
                "status": "Pending"
            },
            "role": info["role"]
        }
        try:
            body["uuid"] = info["uuid"]
            body["membership"] = None
        except:
            pass

        req = requests.post("https://www.meterian.io/api/v1/teams/%s/members" % (info["team_uuid"]), headers={
            "Authorization": "token %s" % ( self.token ),
            "Content-Type": "application/json"
        }, json=body)

        if req.status_code < 200 and req.status_code > 201:
            print(req.text)
            raise ValueError("Server rejected request")

    