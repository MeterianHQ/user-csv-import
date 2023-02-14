class CsvToJsonParser:
    def parse(self, csv, teams):
        csv = csv.split("\n")
        headers = ["full_name", "email", "role", "team_name"]
        parsed = []

        for entry in csv:
            if entry.strip() == "":
                continue
            entry = entry.split(",")
            json_entry = {}
            for i in range(0, len(headers)):
                label = headers[i]
                value = entry[i]
                json_entry[label] = value
            try:
                json_entry["team_uuid"] = teams[json_entry["team_name"]]
            except:
                print("Error - Team name in line %s does not match any team in the account" % (i))
                import sys
                sys.exit(1)
            
            parsed.append(json_entry)

        return parsed