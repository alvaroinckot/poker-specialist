from pyknow import *
from engine.facts import *

# Parametros
BLINDS_TO_GO_ALL_IN = 12
BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED = 18

# Mensagens padrao
MSG_CALL = 'Pague a aposta'
MSG_CHECK = 'Apenas de mesa'
MSG_RAISE = 'Aumente a aposta'
MSG_RAISE_3X_THE_BET = 'Aumente 3x a aposta'
MSG_FOLD = 'Desista da mão'
MSG_GO_ALL_IN = 'Vá ALL IN'
MSG_IS_RAISED = 'Alguém aumentou a aposta'
MSG_POSITION = 'Posição atual {}'
MSG_BLUFF_70_PERC_POT = 'Deve blefar - Aposte 0.7 do POT para roubar os blinds'

lambda_group_1_p = lambda player: (player['card_1_v'] == 1 and player['card_2_v'] == 1) or (player['card_1_v'] == 13 and player['card_2_v'] == 13) or (player['card_1_v'] == 12 and player['card_2_v'] == 12) or (player['card_1_v'] == 12 and player['card_2_v'] == 12) or (player['card_1_v'] == 11 and player['card_2_v'] == 11)
lambda_group_1_s = lambda player: (player['card_1_v'] == 13 and player['card_2_v'] == 1 and player['suited'])
lambda_group_1_o = lambda player: False
lambda_group_2_p = lambda player: (player['card_1_v'] == 10 and player['card_2_v'] == 10)
lambda_group_2_s = lambda player: (player['card_1_v'] == 12 and player['card_2_v'] == 1 and player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 1 and player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 12 and player['suited'])
lambda_group_2_o = lambda player: (player['card_1_v'] == 13 and player['card_2_v'] == 1 and not player['suited'])
lambda_group_3_p = lambda player: (player['card_1_v'] == 9 and player['card_2_v'] == 9)
lambda_group_3_s = lambda player: (player['card_1_v'] == 10 and player['card_2_v'] == 1 and player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 11 and player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 11 and player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 10 and player['suited'])
lambda_group_3_o = lambda player: (player['card_1_v'] == 12 and player['card_2_v'] == 1 and not player['suited'])
lambda_group_4_p = lambda player: (player['card_1_v'] == 8 and player['card_2_v'] == 8)
lambda_group_4_s = lambda player: (player['card_1_v'] == 13 and player['card_2_v'] == 10 and player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 10 and player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 9 and player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 9 and player['suited']) or (player['card_1_v'] == 9 and player['card_2_v'] == 8 and player['suited'])
lambda_group_4_o = lambda player: (player['card_1_v'] == 11 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 12 and not player['suited'])
lambda_group_5_p = lambda player: (player['card_1_v'] == 7 and player['card_2_v'] == 7)
lambda_group_5_s = lambda player: (player['card_1_v'] <= 9 and player['card_1_v'] >= 2 and player['card_2_v'] == 1 and player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 9 and player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 8 and player['suited']) or (player['card_1_v'] == 9 and player['card_2_v'] == 7 and player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 7 and player['suited']) or (player['card_1_v'] == 7 and player['card_2_v'] == 6 and player['suited']) or (player['card_1_v'] == 6 and player['card_2_v'] == 5 and player['suited'])
lambda_group_5_o = lambda player: (player['card_1_v'] == 13 and player['card_2_v'] == 11 and not player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 11 and not player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 10 and not player['suited'])
lambda_group_6_p = lambda player: (player['card_1_v'] == 6 and player['card_2_v'] == 6) or (player['card_1_v'] == 5 and player['card_2_v'] == 5)
lambda_group_6_s = lambda player: (player['card_1_v'] <= 13 and player['card_2_v'] == 9 and player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 8 and player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 6 and player['suited']) or (player['card_1_v'] == 7 and player['card_2_v'] == 5 and player['suited']) or (player['card_1_v'] == 5 and player['card_2_v'] == 4 and player['suited'])
lambda_group_6_o = lambda player: (player['card_1_v'] == 10 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 9 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 10 and not player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 10 and not player['suited'])
lambda_group_7_p = lambda player: (player['card_1_v'] == 4 and player['card_2_v'] == 4) or (player['card_1_v'] == 3 and player['card_2_v'] == 3) or (player['card_1_v'] == 2 and player['card_2_v'] == 2)
lambda_group_7_s = lambda player: (player['card_1_v'] == 13 and player['card_2_v'] <= 8 and player['card_2_v'] >= 2 and player['card_2_v'] == 13 and player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 8 and player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 7 and player['suited']) or (player['card_1_v'] == 6 and player['card_2_v'] == 4 and player['suited']) or (player['card_1_v'] == 5 and player['card_2_v'] == 3 and player['suited']) or (player['card_1_v'] == 4 and player['card_2_v'] == 3 and player['suited'])
lambda_group_7_o = lambda player: (player['card_1_v'] <= 8 and player['card_1_v'] >= 6 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 9 and not player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 9 and not player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 8 and not player['suited'])
lambda_group_8_p = lambda player: False
lambda_group_8_s = lambda player: (player['card_1_v'] == 11 and player['card_2_v'] <= 7 and player['card_2_v'] >= 2 and player['card_2_v'] == 13 and player['suited']) or (player['card_1_v'] == 9 and player['card_2_v'] == 6 and player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 5 and player['suited']) or (player['card_1_v'] == 7 and player['card_2_v'] == 4 and player['suited']) or (player['card_1_v'] == 4 and player['card_2_v'] == 2 and player['suited']) or (player['card_1_v'] == 3 and player['card_2_v'] == 2 and player['suited'])
lambda_group_8_o = lambda player: (player['card_1_v'] <= 5 and player['card_1_v'] >= 2 and player['card_2_v'] == 1 and not player['suited']) or (player['card_1_v'] == 13 and player['card_2_v'] == 9 and not player['suited']) or (player['card_1_v'] == 12 and player['card_2_v'] == 9 and not player['suited']) or (player['card_1_v'] == 11 and player['card_2_v'] == 8 and not player['suited']) or (player['card_1_v'] == 10 and player['card_2_v'] == 8 and not player['suited']) or (player['card_1_v'] == 8 and player['card_2_v'] == 7 and not player['suited']) or (player['card_1_v'] == 7 and player['card_2_v'] == 7 and not player['suited']) or (player['card_1_v'] == 6 and player['card_2_v'] == 5 and not player['suited']) or (player['card_1_v'] == 5 and player['card_2_v'] == 5 and not player['suited'])


class PokerInference(KnowledgeEngine):

    # Se o evento de cartas recebidas foi acionado e se ja tiver um player disponivel com o mesmo nome
    # defina as cardas do evento para o jogador de mesmo nome
    @Rule(AS.player << Player(),
          AS.received_card << ReceivedCard(),
          TEST(lambda player, received_card: player['name'] == received_card['player']),
          )
    def set_received_cards(self, player, received_card):
        f_card, s_card = received_card['cards']
        self.retract(received_card)

        # Ordena cartas
        card_1_v = 0
        if f_card['value'] == 'A':
            card_1_v = 1
        elif f_card['value'] == 'T':
            card_1_v = 10
        elif f_card['value'] == 'J':
            card_1_v = 11
        elif f_card['value'] == 'Q':
            card_1_v = 12
        elif f_card['value'] == 'K':
            card_1_v = 13
        else:
            card_1_v = int(f_card['value'])

        card_2_v = 0
        if s_card['value'] == 'A':
            card_2_v = 1
        elif s_card['value'] == 'T':
            card_2_v = 10
        elif s_card['value'] == 'J':
            card_2_v = 11
        elif s_card['value'] == 'Q':
            card_2_v = 12
        elif s_card['value'] == 'K':
            card_2_v = 13
        else:
            card_2_v = int(s_card['value'])

        card_1_s = f_card['suit']
        card_2_s = s_card['suit']
        if card_1_v < card_2_v:
            card_temp = card_1_v
            card_1_v = card_2_v
            card_2_v = card_temp
            card_1_s = s_card['suit']
            card_2_s = f_card['suit']

        # Mpdifica player
        self.modify(player, me=True, cards=received_card['cards'],
                    card_1_v=card_1_v, card_2_v=card_2_v,
                    card_1_s=card_1_s, card_2_s=card_2_s,
                    suited=f_card['suit'] == s_card['suit'],
                    group=0)

    # Se uma ação tiver o mesmo nome do player principal
    # Marque as actions como a do player principal com a flag 'me'
    @Rule(AS.action << Action(me=False),
          AS.player << Player(me=True),
          TEST(lambda action, player: action['player'] == player['name']))
    def set_me_in_action(self, action):
        self.modify(action, me=True)

    # Se tiver alguma action de mesma street de id maior com o mesmo act
    # Defina is_raised como true
    @Rule(AS.action << Action(me=False, type='raise'),
          AS.action_me << Action(me=True, is_raised=False),
          TEST(lambda action, action_me: action_me['street'] == action['street'] and
                                         action_me['id'] > action['id'] and
                                         action_me['act'] == action['act']))
    def is_prefop_raised_act_1(self, action_me):
        self.modify(action_me, is_raised=True)

    # Grupo de Maos

    # Se as cartas recebidas estiverem no grupo 1 e par
    # Defina o player principal com o grupo 1
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_1_p(player)))
    def preflop_define_group_1_pair(self, player):
        self.modify(player, group=1)


    # Se as cartas recebidas estiverem no grupo 1 e do mesmo naipe
    # Defina o player principal com o grupo 1 suited
    @Rule(AS.player << Player(group=0, suited=True),
          TEST(lambda player: lambda_group_1_s(player)))
    def preflop_define_group_1_suited(self, player):
        self.modify(player, group=1)

    # Se as cartas recebidas estiverem no grupo 1 e de naipe diferente
    # Defina o player principal com o grupo 1 off
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_1_o(player)))
    def preflop_define_group_1_ofsuited(self, player):
        self.modify(player, group=1)

    # Se as cartas recebidas estiverem no grupo 2 e par
    # Defina o player principal com o grupo 2
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_2_p(player)))
    def preflop_define_group_2_pair(self, player):
        self.modify(player, group=2)

    # Se as cartas recebidas estiverem no grupo 2 e do mesmo naipe
    # Defina o player principal com o grupo 2 suited
    @Rule(AS.player << Player(group=0, suited=True),
          TEST(lambda player: lambda_group_2_s(player)))
    def preflop_define_group_2_suited(self, player):
        self.modify(player, group=2)


    # Se as cartas recebidas estiverem no grupo 2 e de naipe diferente
    # Defina o player principal com o grupo 2 off
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_2_o(player)))
    def preflop_define_group_2_ofsuited(self, player):
        self.modify(player, group=2)

    # Se as cartas recebidas estiverem no grupo 3 e par
    # Defina o player principal com o grupo 3
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_3_p(player)))
    def preflop_define_group_3_pair(self, player):
        self.modify(player, group=3)


    # Se as cartas recebidas estiverem no grupo 3 e do mesmo naipe
    # Defina o player principal com o grupo 3 suited
    @Rule(AS.player << Player(group=0, suited=True),
          TEST(lambda player: lambda_group_3_s(player)))
    def preflop_define_group_3_suited(self, player):
        self.modify(player, group=3)

    # Se as cartas recebidas estiverem no grupo 3 e de naipe diferente
    # Defina o player principal com o grupo 3 off
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_3_o(player)))
    def preflop_define_group_3_ofsuited(self, player):
        self.modify(player, group=3)

    # Se as cartas recebidas estiverem no grupo 4 e par
    # Defina o player principal com o grupo 4
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_4_p(player)))
    def preflop_define_group_4_pair(self, player):
        self.modify(player, group=4)

    # Se as cartas recebidas estiverem no grupo 4 e do mesmo naipe
    # Defina o player principal com o grupo 4 suited
    @Rule(AS.player << Player(group=0, suited=True),
          TEST(lambda player: lambda_group_4_s(player)))
    def preflop_define_group_4_suited(self, player):
        self.modify(player, group=4)

    # Se as cartas recebidas estiverem no grupo 4 e de naipe diferente
    # Defina o player principal com o grupo 4 off
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_4_o(player)))
    def preflop_define_group_4_ofsuited(self, player):
        self.modify(player, group=4)

    # Se as cartas recebidas estiverem no grupo 5 e par
    # Defina o player principal com o grupo 5
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_5_p(player)))
    def preflop_define_group_5_pair(self, player):
        self.modify(player, group=5)

    # Se as cartas recebidas estiverem no grupo 5 e do mesmo naipe
    # Defina o player principal com o grupo 5 suited
    @Rule(AS.player << Player(group=0, suited=True),
          TEST(lambda player: lambda_group_5_s(player)))
    def preflop_define_group_5_suited(self, player):
        self.modify(player, group=5)

    # Se as cartas recebidas estiverem no grupo 5 e de naipe diferente
    # Defina o player principal com o grupo 5 off
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_5_o(player)))
    def preflop_define_group_5_ofsuited(self, player):
        self.modify(player, group=5)

    # Se as cartas recebidas estiverem no grupo 6 e par
    # Defina o player principal com o grupo 6
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_6_p(player)))
    def preflop_define_group_6_pair(self, player):
        self.modify(player, group=6)

    # Se as cartas recebidas estiverem no grupo 6 e do mesmo naipe
    # Defina o player principal com o grupo 6 suited
    @Rule(AS.player << Player(group=0, suited=True),
          TEST(lambda player: lambda_group_6_s(player)))
    def preflop_define_group_6_suited(self, player):
        self.modify(player, group=6)

   # Se as cartas recebidas estiverem no grupo 6 e de naipe diferente
    # Defina o player principal com o grupo 6 off
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_6_o(player)))
    def preflop_define_group_6_ofsuited(self, player):
        self.modify(player, group=6)

    # Se as cartas recebidas estiverem no grupo 7 e par
    # Defina o player principal com o grupo 7
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_7_p(player)))
    def preflop_define_group_7_pair(self, player):
        self.modify(player, group=7)

   # Se as cartas recebidas estiverem no grupo 7 e do mesmo naipe
    # Defina o player principal com o grupo 7 suited
    @Rule(AS.player << Player(group=0, suited=True),
          TEST(lambda player: lambda_group_7_s(player)))
    def preflop_define_group_7_suited(self, player):
        self.modify(player, group=7)

    # Se as cartas recebidas estiverem no grupo 7 e de naipe diferente
    # Defina o player principal com o grupo 7 off
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_7_o(player)))
    def preflop_define_group_7_ofsuited(self, player):
        self.modify(player, group=7)

    # Se as cartas recebidas estiverem no grupo 8 e par
    # Defina o player principal com o grupo 8
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_8_p(player)))
    def preflop_define_group_8_pair(self, player):
        self.modify(player, group=8)

    # Se as cartas recebidas estiverem no grupo 8 e do mesmo naipe
    # Defina o player principal com o grupo 8 suited
    @Rule(AS.player << Player(group=0, suited=True),
          TEST(lambda player: lambda_group_8_s(player)))
    def preflop_define_group_8_suited(self, player):
        self.modify(player, group=8)

    # Se as cartas recebidas estiverem no grupo 8 e de naipe diferente
    # Defina o player principal com o grupo 8 off
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: lambda_group_8_o(player)))
    def preflop_define_group_8_ofsuited(self, player):
        self.modify(player, group=8)

    # Se as cartas não forem de nenhum dos grupos anterios
    # Defina o player principal com o grupo 9
    @Rule(AS.player << Player(group=0, suited=False),
          TEST(lambda player: not lambda_group_1_p(player)),
          TEST(lambda player: not lambda_group_1_s(player)),
          TEST(lambda player: not lambda_group_1_o(player)),
          TEST(lambda player: not lambda_group_2_p(player)),
          TEST(lambda player: not lambda_group_2_s(player)),
          TEST(lambda player: not lambda_group_2_o(player)),
          TEST(lambda player: not lambda_group_3_p(player)),
          TEST(lambda player: not lambda_group_3_s(player)),
          TEST(lambda player: not lambda_group_3_o(player)),
          TEST(lambda player: not lambda_group_4_p(player)),
          TEST(lambda player: not lambda_group_4_s(player)),
          TEST(lambda player: not lambda_group_4_o(player)),
          TEST(lambda player: not lambda_group_5_p(player)),
          TEST(lambda player: not lambda_group_5_s(player)),
          TEST(lambda player: not lambda_group_5_o(player)),
          TEST(lambda player: not lambda_group_6_p(player)),
          TEST(lambda player: not lambda_group_6_s(player)),
          TEST(lambda player: not lambda_group_6_o(player)),
          TEST(lambda player: not lambda_group_7_p(player)),
          TEST(lambda player: not lambda_group_7_s(player)),
          TEST(lambda player: not lambda_group_7_o(player)),
          TEST(lambda player: not lambda_group_8_p(player)),
          TEST(lambda player: not lambda_group_8_s(player)),
          TEST(lambda player: not lambda_group_8_o(player)))
    def preflop_define_group_9_not_otthers(self, player):
        self.modify(player, group=9)

    ######### REGRAS no PREFLOP #########

    # Se estiver no pre-flop
    # Informe a posição
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1))
    def set_street_position_message_preflop(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_POSITION.format(action['position'])))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação
    # Informar raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, is_raised=True, act=1),
          AS.player << Player(me=True))
    def preflop_someone_raised(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_IS_RAISED))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 1 ou 2, e com blinds maior q BLINDS_TO_GO_ALL_IN
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN))
    def preflop_group_1_2_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 1 ou 2, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN
    # Sugira All In
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN))
    def preflop_group_1_2_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 1 ou 2, e com blinds maior q BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED
    # Sugira re-raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_1_2_reraise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))


    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 1 ou 2, e com blinds menor igual aq BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED
    # Sugira all in
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_1_2_reraise_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na segunda ação, e no grupo 1 ou 2, e com blinds maior q BLINDS_TO_GO_ALL_IN * 2
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN * 2))
    def preflop_group_1_2_act2_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE_3X_THE_BET))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na segunda ação, e no grupo 1 ou 2, e com blinds maior q BLINDS_TO_GO_ALL_IN * 2
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN * 2))
    def preflop_group_1_2_act2_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e tem raised na segunda ação, e no grupo 1 ou 2, e com blinds
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2))
    def preflop_group_1_2_act2_reraise_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 3, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 3),
          TEST(lambda action: action['position'] == 'UTG+1' or action['position'] == 'MP1' or action['position'] == 'MP2' or action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB' or action['position'] == 'BB'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN))
    def preflop_group_3_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 3, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira all in
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 3),
          TEST(lambda action: action['position'] == 'UTG+1' or action['position'] == 'MP1' or action['position'] == 'MP2' or action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB' or action['position'] == 'BB'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN))
    def preflop_group_3_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 3, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 3),
          TEST(lambda action: action['position'] == 'UTG'))
    def preflop_group_3_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 3),
          TEST(lambda action: action['position'] == 'MP2' or action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB' or action['position'] == 'BB'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_3_reraise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 3, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira all in
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 3),
          TEST(lambda action: action['position'] == 'MP2' or action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB' or action['position'] == 'BB'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_3_reraise_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e tiver raised na primeira ação, e no grupo 3, e nas posicoes citadas abaixo
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 3),
          TEST(lambda action: action['position'] == 'UTG+1' or action['position'] == 'MP1' or action['position'] == 'UTG'))
    def preflop_group_3_fold_to_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e ninguem deu raise e estiver na segunda ação, e no grupo 3 e com blinds maior que BLINDS_TO_GO_ALL_IN
    # Sugira check
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN),
          TEST(lambda player: player['group'] == 3))
    def preflop_group_3_act2_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_CHECK))

    # Se estiver o jogador principal, estiver no preflop e estiver na segunda ação, e no grupo 3 e com blinds maior que BLINDS_TO_GO_ALL_IN
    # Sugira call
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN),
          TEST(lambda player: player['group'] == 3))
    def preflop_group_3_act2_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_CALL))

    # Se estiver o jogador principal, estiver no preflop e estiver na segunda ação, e no grupo 3 e com blinds menor ou igual que BLINDS_TO_GO_ALL_IN
    # Sugira all in
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2),
          AS.player << Player(me=True),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN),
          TEST(lambda player: player['group'] == 3))
    def preflop_group_3_act2_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 4, e com  blinds maior q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda action: action['position'] == 'MP1' or action['position'] == 'MP2' or action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB' or action['position'] == 'BB'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN))
    def preflop_group_4_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 4, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira all in
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda action: action['position'] == 'MP1' or action['position'] == 'MP2' or action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB' or action['position'] == 'BB'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN))
    def preflop_group_4_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 4, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda action: action['position'] == 'UTG+1' or action['position'] == 'UTG'))
    def preflop_group_4_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 4, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN_WHEN_IS_RERAISED e nas posicoes citadas abaixo
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda action: action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB' or action['position'] == 'BB'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_4_reraise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 4, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN_WHEN_IS_RERAISED e nas posicoes citadas abaixo
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda action: action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB' or action['position'] == 'BB'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_4_reraise_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 4
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda action: action['position'] == 'MP1' or action['position'] == 'MP2' or action['position'] == 'UTG+1' or action['position'] == 'UTG'))
    def preflop_group_4_fold_to_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver na segunda ação, e no grupo 4 e com blinds maior que BLINDS_TO_GO_ALL_IN
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN))
    def preflop_group_4_act2_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver na segunda ação, e no grupo 4 e com blinds menor que BLINDS_TO_GO_ALL_IN
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 4),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN))
    def preflop_group_4_act2_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 5, e com  blinds maior q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 5),
          TEST(lambda action: action['position'] == 'MP2' or action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN))
    def preflop_group_5_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 5, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira all in
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 5),
          TEST(lambda action: action['position'] == 'MP2' or action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN))
    def preflop_group_5_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 5
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 5),
          TEST(lambda action: action['position'] == 'MP1' or action['position'] == 'UTG+1' or action['position'] == 'UTG' or action['position'] == 'BB'))
    def preflop_group_5_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 5, e com  blinds maior q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 5),
          TEST(lambda action: action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_5_reraise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 5, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira all in
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 5),
          TEST(lambda action: action['position'] == 'CO' or action['position'] == 'BTN' or action['position'] == 'SB'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_5_reraise_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 5
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 5),
          TEST(lambda action: action['position'] == 'MP2' or action['position'] == 'HJ' or action['position'] == 'MP1' or action['position'] == 'UTG+1' or action['position'] == 'UTG' or action['position'] == 'BB'))
    def preflop_group_5_fold_to_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver na segunda ação, e no grupo 5 e teve raise
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 5))
    def preflop_group_5_act2_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 6, e com  blinds maior q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 6),
          TEST(lambda action: action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN))
    def preflop_group_6_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 6, e com  blinds menor igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 6),
          TEST(lambda action: action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN))
    def preflop_group_6_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 6
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 6),
          TEST(lambda action: action['position'] == 'MP1' or action['position'] == 'MP2' or action['position'] == 'UTG+1' or action['position'] == 'UTG' or action['position'] == 'SB' or action['position'] == 'BB'))
    def preflop_group_6_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 6, > que estes blinds e ness posicao
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 6),
          TEST(lambda action: action['position'] == 'BTN'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_6_reraise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 6, e com  blinds menor ou igual q BLINDS_TO_GO_ALL_IN_WHEN_IS_ALL e nas posicoes citadas abaixo
    # Sugira all in
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 6),
          TEST(lambda action: action['position'] == 'BTN'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN_WHEN_IS_RAISED))
    def preflop_group_6_reraise_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 5, e nas posicoes citadas abaixo
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 6),
          TEST(lambda action: action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'MP1' or action['position'] == 'MP2' or action['position'] == 'UTG+1' or action['position'] == 'UTG' or action['position'] == 'SB' or action['position'] == 'BB'))
    def preflop_group_6_fold_to_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver na segunda ação, e no grupo 6 e teve raise
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 6))
    def preflop_group_6_act2_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 7, e com  blinds maior q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 7),
          TEST(lambda action: action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN))
    def preflop_group_7_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 7, e com  blinds menor igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira allin
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 7),
          TEST(lambda action: action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'BTN'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN))
    def preflop_group_7_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 7
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 7),
          TEST(lambda action: action['position'] == 'MP1' or action['position'] == 'MP2' or action['position'] == 'UTG+1' or action['position'] == 'UTG' or action['position'] == 'SB' or action['position'] == 'BB'))
    def preflop_group_7_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 7
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 7))
    def preflop_group_7_fold_to_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver na segunda ação, e no grupo 7 e teve raise
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 7))
    def preflop_group_7_act2_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 8, e com  blinds maior q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira raise
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 8),
          TEST(lambda action: action['position'] == 'BTN'),
          TEST(lambda player: player['bbs'] > BLINDS_TO_GO_ALL_IN))
    def preflop_group_8_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 8, e com  blinds menor igual q BLINDS_TO_GO_ALL_IN e nas posicoes citadas abaixo
    # Sugira all in
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 8),
          TEST(lambda action: action['position'] == 'BTN'),
          TEST(lambda player: player['bbs'] <= BLINDS_TO_GO_ALL_IN))
    def preflop_group_8_allin(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_GO_ALL_IN))

    # Se estiver o jogador principal, estiver no preflop e não estiver raised na primeira ação, e no grupo 8
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 8),
          TEST(lambda action: action['position'] == 'MP1' or action['position'] == 'MP2' or action['position'] == 'UTG+1' or action['position'] == 'UTG' or action['position'] == 'HJ' or action['position'] == 'CO' or action['position'] == 'SB' or action['position'] == 'BB'))
    def preflop_group_8_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 8
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 8))
    def preflop_group_8_fold_to_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver na segunda ação, e no grupo 8 e teve raise
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=2, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 8))
    def preflop_group_8_act2_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e nao estiver raised na primeira ação, e no grupo 9
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 9),)
    def preflop_group_9_fold(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    # Se estiver o jogador principal, estiver no preflop e estiver raised na primeira ação, e no grupo 9
    # Sugira fold
    @Rule(AS.action << Action(street='PREFLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 9),)
    def preflop_group_9_fold_to_raise(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_FOLD))

    ######### REGRAS nO FLOP #########

    # Se estiver no flop
    # Informe a posição
    @Rule(AS.action << Action(street='FLOP', me=True, act=1))
    def set_street_position_message_flop(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_POSITION.format(action['position'])))

    # Se no flop alguem apostou
    # Informe a aposta
    @Rule(AS.action << Action(street='FLOP', me=True, is_raised=True, act=1),
          AS.player << Player(me=True))
    def flop_someone_raised(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_IS_RAISED))

    # Se no flop, e nenhuma aposta, e o jogador principal estiver com as cartas de grupo 1 ou 2
    # Sugira call na aposta
    @Rule(AS.action << Action(street='FLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2))
    def flop_group_1_2(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_RAISE))

    # Se no flop algum jogador der raise e o jogador principal estiver com as cartas de grupo 1 ou 2
    # Sugira call na aposta
    @Rule(AS.action << Action(street='FLOP', me=True, act=1, is_raised=True),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] == 1 or player['group'] == 2))
    def flop_group_1_2_raised(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_CALL))

    # Se no flop o jogador principal estiver no botão e ninguem aumentou a aposta
    # Blefe como 70% do pot
    @Rule(AS.action << Action(street='FLOP', me=True, act=1, is_raised=False),
          AS.player << Player(me=True),
          TEST(lambda player: player['group'] > 4), TEST(lambda action:  action['position'] == 'BTN'))
    def flop_blef_btn(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_BLUFF_70_PERC_POT))

    ######### REGRAS no TURN #########

    # Se estiver no turn
    # Informe a posição
    @Rule(AS.action << Action(street='TURN', me=True, act=1))
    def set_street_position_message_flop(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_POSITION.format(action['position'])))

    # Se no turn alguem apostou
    # Informe a aposta
    @Rule(AS.action << Action(street='TURN', me=True, is_raised=True, act=1),
          AS.player << Player(me=True))
    def flop_someone_raised(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_IS_RAISED))

    ######### REGRAS no RIVER #########

    # Se estiver no river
    # Informe a posição
    @Rule(AS.action << Action(street='RIVER', me=True, act=1))
    def set_street_position_message_flop(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_POSITION.format(action['position'])))

    # Se no river alguem apostou
    # Informe a aposta
    @Rule(AS.action << Action(street='RIVER', me=True, is_raised=True, act=1),
          AS.player << Player(me=True))
    def flop_someone_raised(self, action):
        self.declare(Suggestion(street=action['street'], message=MSG_IS_RAISED))

    ######### OUTRAS REGRAS #########
    # Se o player nao tiver os blinds calculados
    # Calcule o blind para o player
    @Rule(AS.player << Player(bbs=None), AS.blind << Blind())
    def set_player_big_blinds(self, player, blind):
        self.modify(player, bbs=player['chips']/blind['big'])

    # Se a mensagem das cartas da mão não estiver definida
    # Cria a mensagem no formato determinado
    @Rule(AS.table << Table(cards_str=None))
    def set_table_cards_string(self, table):
        self.modify(table, cards_str=''.join(["{}{} ".format(card['value'], card['suit']) for card in table['cards']]))

    # Se o resumo de jogo nao tiver os blinds calculados do pot
    # Calcule os blinds do pot
    @Rule(AS.game << GameSummary(bbs=None), AS.blind << Blind())
    def set_summary_bbs(self, game, blind):
        self.modify(game, bbs=game['pot']/blind['big'])

