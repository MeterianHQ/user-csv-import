class MeterianMembersListReducer:
    def reduce(self, members):
        reduced_members = {}
        for member in members:
            reduced_members[member["email"]] = member["uuid"]

        return reduced_members