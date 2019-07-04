from pyknow import *


class Game(Fact):
    id = Field(str, mandatory=True)
    type = Field(str, mandatory=True)  # TOURNAMENT
    modality = Field(str, mandatory=True)  # NLH
    players_for_table = Field(int, default=None)


class Blind(Fact):
    small = Field(int, mandatory=True)
    big = Field(int, mandatory=True)


class Hand(Fact):
    id = Field(int, mandatory=True)


class ReceivedCard(Fact):
    player = Field(str, mandatory=True)
    cards = Field(list)


class Player(Fact):
    name = Field(str, mandatory=True)
    chips = Field(int, mandatory=True)
    seat = Field(int, mandatory=True)
    is_out = Field(bool)
    bbs = Field(float, default=None)
    cards = Field(list)
    suited = Field(bool)
    me = Field(bool)
    group = Field(int)  # 1, 2, 3, 4, 5, 6, 7 or 8


class Action(Fact):
    id = Field(int, mandatory=True)
    type = Field(str, mandatory=True)
    player = Field(str, mandatory=True)
    street = Field(str, mandatory=True)  # PREFLOP | FLOP | TURN | RIVER
    position = Field(str)  # SB | BB | UTG | UTG+1 | MP1 | MP2 | HJ | CO | BNT
    is_raised = Field(bool)  # True or False


class Suggestion(Fact):
    street = Field(str, mandatory=True)  # PREFLOP | FLOP | TURN | RIVER
    message = Field(str, mandatory=True)
