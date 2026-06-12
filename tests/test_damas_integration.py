from app.models.game_model import GameModel


def test_damas_mode_selection_and_board_size():
    model = GameModel()
    model.configure_game_mode('damas')
    model.configure_players(['Ana', 'Bruno'])
    model.start_new_match()

    board = model.get_board()
    assert len(board) == 8
    assert len(board[0]) == 8
    assert model.is_game_mode_damas()
    assert model.get_current_player_text() == 'Ana (B)'


def test_damas_origin_selection():
    model = GameModel()
    model.configure_game_mode('damas')
    model.configure_players(['Ana', 'Bruno'])
    model.start_new_match()

    assert model.is_valid_origin(2, 1)
    assert model.play_turn(2, 1) is True
    assert model.get_selected_origin_text() == 'Origem: (2, 1)'
