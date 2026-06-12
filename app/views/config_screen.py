"""Tela de configuracao da partida."""

from app.views.base_screen import BaseScreen


class ConfigScreen(BaseScreen):
    """View para definir quantidade e nomes dos jogadores."""

    def on_pre_enter(self, *args) -> None:
        """Atualiza o texto do modo de jogo sempre que a tela for exibida."""
        selected_mode = "Damas" if self.controller.is_damas_mode() else "Jogo da Velha"
        self.ids.mode_label.text = f"Modo selecionado: {selected_mode}"

    def on_mode_toggle(self, active: bool) -> None:
        """Seleciona o modo de jogo baseado no checkbox."""
        self.controller.select_game_mode("damas" if active else "velha")

    def start_match(self) -> None:
        """Envia nomes configurados para o Controller iniciar a partida."""
        names = [
            self.ids.player_one.text,
            self.ids.player_two.text,
        ]
        self.controller.start_match(names)
