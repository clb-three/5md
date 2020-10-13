from model.heroes.complaint import Complaint
from model.message import Message


class Table:
    """
    A Table takes care of the logic for high-level interaction
    between parts of the game.
    """

    def __init__(self, game, emitter, logging):
        self.gamestate = game
        self.emit = emitter
        self.log = logging.getLogger(__name__)

    async def play_card(self, hero, card):
        """
        Play the given card against the current enemy
        """
        self.log.info(f'play_card({hero=}, {card=})')

        # Check if the card is in the hero's hand
        card = hero.get_card_from_hand(card)
        if not card:
            raise Complaint(Message('notinhand', card))

        # Play the card and discard it
        await self.emit(card.play(self.gamestate.target, self))
        self.discard_card(hero, card)

    async def discard_card(self, hero, card):
        """
        Move the given card to the discard pile.
        """
        self.log.info(f'discard_card({hero=}, {card=})')

        hero.discard(card)
        await self.emit(Message('discard', [hero, card]))

    async def draw_card(self, hero):
        """
        Make the given hero draw a card.
        """
        self.log.info(f'draw_card({hero=})')

        card = hero.draw_card()
        await self.emit(Message('draw', [hero, card]))

    async def process_command(self, command):
        """
        Process a command from the user.
        """

        self.log.info(f"process_command({command=})")

        try:
            # Get input
            args = command.split(' ')

            # Do input
            if args[0] == 'hero':
                hero_name = args[1]
                args = args[2:]

                self.log.info(f"hero command {hero_name=}, {args=}")

                hero = next(filter(lambda h: h.name == hero_name, self.gamestate.heroes), None)
                if not hero:
                    raise Complaint(Message('nosuchhero', hero_name))

                if args[0] == 'play':
                    # Forces card into a lower case string to prevent capitalization issues with input
                    card = args[1].lower()
                    self.play_card(hero, card)
                elif args[0] == 'discard':
                    card = args[1].lower()
                    self.discard_card(hero, card)
                elif args[0] == 'draw':
                    self.draw_card(hero)
                else:
                    raise Complaint(Message('error', 'invalidcommand'))

                # TODO: Add hero abilities
            else:
                raise Complaint(Message('error', 'invalidcommand'))

            # break out when all enemies isded
            if self.gamestate.is_defeated:
                await self.emit(Message('state', 'won'))
        except Complaint as c:
            await self.emit(c.msg)
