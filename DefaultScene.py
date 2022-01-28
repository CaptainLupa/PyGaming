import Scene
import Player
import Button
import globals


def test():
    print("Fart\n"*69)


class DefaultScene(Scene.Scene):
    def buildScene(self):
        self.addActor(Player.Player())
        self.addUIElement(Button.Button(action=test))
        