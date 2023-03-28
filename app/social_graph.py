"""
Social graph connecting user matches
"""
from __future__ import annotations

from user import User
from python_ta.contracts import check_contracts


@check_contracts
class _User:
    """
    vertex of the graph representing each user
    """
    item: User
    user_id: int
    matches: set[_User]

    def __init__(self, item: User, matches: set[_User]):
        self.item = item
        self.matches = matches
        self.user_id = item.id


@check_contracts
class Network:
    """
    The graph representing the network of matches betwen users
    """
    _users: dict[int, _User]

    def __init__(self) -> None:
        """
        Initialized an empty network
        """
        self._users = {}

    def add_user(self, user: User) -> None:
        """
        add user to given graph

        Preconditions:
            - user not in self._users
        """
        self._users[user.id] = _User(user, set())

    def add_connection(self, user1: User, user2: User) -> None:
        """
        add a match/ connection between 2 users

        Preconditions:
            - user1 != user2
        """
        if user1.id not in self._users:
            self.add_user(user1)
        if user2.id not in self._users:
            self.add_user(user2)
        u1 = self._users[user1.id]
        u2 = self._users[user2.id]

        u1.matches.add(u2)
        u2.matches.add(u1)

    def check_connection(self, user1: User, user2: User) -> bool:
        """
        check whether 2 users have a connection/ matched
        """
        if user1.id in self._users and user2.id in self._users:
            u1 = self._users[user1.id]
            return any(u2.user_id == user2.id for u2 in u1.matches)
        else:
            return False

    def get_matches(self, user: User) -> set[int]:
        """
        return a set of user ids for the matches of the given user
        """
        if user.id in self._users:
            u = self._users[user.id]
            return {match.user_id for match in u.matches}
        else:
            raise ValueError


def create_network(matches: list[dict[int, set[User]]]) -> Network:
    """
    create a network from matches
    """
    my_network = Network()
    for match in matches:
        ...
