from src.utils import utils

def test_create_field():
    game_field = utils.GameField(2,3).get_field()
    print(len(game_field))
    assert len(game_field) == 2 

