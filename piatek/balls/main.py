from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, LVector3, LineSegs

TS = 10

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        self.camera.set_pos(0, -15, 12)
        self.camera.look_at(0, 0, 0)

        ambient = AmbientLight('ambient')
        ambient.set_color((0.5, 0.5, 0.5, 1))
        self.render.set_light(self.render.attach_new_node(ambient))

        directional = DirectionalLight('directional')
        directional.set_color((1, 1, 1, 1))
        directional.set_direction(LVector3(-1, -1, -2))
        self.render.set_light(self.render.attach_new_node(directional))
        self.draw_bounds()

    def draw_bounds(self):
        lines = LineSegs()
        lines.moveTo(-TS/2, -TS/2, 0)
        lines.drawTo(TS/2, -TS/2, 0)
        lines.drawTo(TS/2, TS/2, 0)
        lines.drawTo(-TS/2, TS/2, 0)
        lines.drawTo(-TS/2, -TS/2, 0)

        lines.set_color(1, 0, 0, 1)
        node = lines.create()
        self.render.attach_new_node(node)





if __name__ == '__main__':
    app = Game()
    app.run()