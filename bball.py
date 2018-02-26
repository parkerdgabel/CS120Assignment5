class Team:
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
        assert line != ""
        assert isinstance(line, str)
        name = line[:line.index("(")].strip()
        conf = line[line.index("("):line.index(")") + 1].strip()
        lst = line.split()
        wins = lst[-2].strip()
        losses = lst[-1].strip()
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
        assert self._losses > 0
        return self._wins / self._losses

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
