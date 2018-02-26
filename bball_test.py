import bball


class BBallSmallTeam_Test:
    def setUp(self):
        self.filename = "./test-a5/in12.txt"

    def team_test(self):
        team_list = bball.build_team_list(self.filename)
        for team in team_list:
            print(team)

    def conf_test(self):
        team_list = bball.build_team_list(self.filename)
        for team in team_list:
            print(team.conf())

    def tearDown(self):
        pass