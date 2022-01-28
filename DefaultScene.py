import Scene
import Player
import globals


class DefaultScene(Scene.Scene):
    def buildScene(self):
        self.addSprite(Player.Player())
        