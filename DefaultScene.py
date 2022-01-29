import Scene
import Player
import Button
import globals


class DefaultScene(Scene.Scene):
    def buildScene(self):
        self.addActor(Player.Player())
        