class Team:
    """"""
    def __init__(self, line):
        """Initializes the Team Object.
        Parameters: line is a non-empty line from the input file.
        Returns: Team
        Pre-conditions: line is a non-empty string.
        Post-conditions: A new Team object is born."""
        assert line != ""
        line = self._parse_line(line)
        self._name = line[0]
        self._conf = line[1]
        self._wins = line[2]
        self._losses = line[3]

    def _parse_line(self, line):
        """Parses the input line for __init__.
        Parameters: line is a non empty line
        Returns: tuple of necessary data.
        Pre-condtions: line is nonempty.
        Post-condition: tuple is returned."""
        assert isinstance(line, str)
        assert line != "" and "(" in line and ")" in line
        line = line[::-1]
        losses_wins = line[:line.index("(")].strip().split()
        losses = losses_wins[0][::-1]
        wins = losses_wins[1][::-1]
        conf = line[line.index(")") + 1:line.index("(")][::-1]
        name = line[line.index("(") + 1:].strip().split()[0][::-1]
        return (name, conf, int(wins), int(losses))

    def name(self):
        """Getter for name attribute.
        Parameters: None
        Returns String
        Pre-conditions: self exists
        Post-conditions: Retuns a string.
        """
        return self._name

    def conf(self):
        """Getter for conf attribute.
        Parameters: None
        Returns String
        Pre-conditions: self exists
        Post-conditions: Retuns a string.
        """
        return self._conf

    def win_ratio(self):
        """Returns the win ratio of a team.
        Parameters: None
        Returns: float
        Pre-conditions: self exists and _losses is > 0.
        Post-conditions: float is returned"""
        return self._wins / (self._wins + self._losses)

    def __eq__(self, other):
        """Equal function for team. Only checks the name.
        Parameters: other is the team to be compared to.
        Returns: bool
        Pre-conditions: other is a team.
        Post-conditions: a bool is returned."""
        assert isinstance(other, Team)
        return other._name == self._name

    def __str__(self):
        """String method for Team Class
        Parameters: None
        Returns: string
        Pre-conditions: self exists
        Post-conditions: string is returned
        """
        return "{} : {}".format(self._name, str(self.win_ratio()))


class Conference:
    def __init__(self, conf):
        assert conf != ""
        self._conf = conf
        self._teams = []

    def __contains__(self, team):
        assert isinstance(team, Team)
        for elem in self._teams:
            if team == elem:
                return True
        return False

    def __str__(self):
        return "{} : {}".format(self._conf, str(self.win_ratio_avg()))

    def name(self):
        return self._conf

    def add(self, team):
        assert team.conf() == self._conf
        self._teams.append(team)

    def win_ratio_avg(self):
        assert len(self._teams) > 0
        total = 0
        for team in self._teams:
            total += team.win_ratio()
        return total / len(self._teams)


class ConferenceSet:
    def __init__(self):
        """"""
        self._conf_set = set()

    def add(self, team):
        assert isinstance(team, Team)
        if not self._is_conference_in_list(team.conf()):
            self._conf_set.add(Conference(team.conf()))
        for elem in self._conf_set:
            if elem.name() == team.conf():
                elem.add(team)

    def best(self):
        ret_list = []
        max = 0.0
        for elem in self._conf_set:
            if elem.win_ratio_avg() > max:
                ret_list.clear()
                ret_list.append(elem)
                max = elem.win_ratio_avg()
            elif elem.win_ratio_avg() == max:
                ret_list.append(elem)
        return ret_list

    def _is_conference_in_list(self, conference):
        for conf in self._conf_set:
            if conf.name() == conference:
                return True
        return False


def build_team_list(filename):
    """Constructs the team list from the given input file.
    Parameters: filename is a non-empty string.
    Returns: List containing all the teams.
    Pre-conditions: filename is open.
    Post-conditions: A list of Team objects is returned."""
    assert filename != ""
    infile = open(filename)
    team_list = []
    for line in infile:
        if line[0] != "#":
            team_list.append(Team(line))
    return team_list


def main():
    filename = input()
    team_list = build_team_list(filename)
    conf_set = ConferenceSet()
    for team in team_list:
        conf_set.add(team)
    for elem in conf_set.best():
        print(elem)


main()
