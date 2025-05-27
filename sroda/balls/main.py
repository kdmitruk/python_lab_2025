from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, LVector3, LineSegs

TABLE_SIZE = 10
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
        ls = LineSegs()
        ls.moveTo(-TABLE_SIZE/2, -TABLE_SIZE/2, 0)
        ls.drawTo(TABLE_SIZE/2, -TABLE_SIZE/2, 0)
        ls.drawTo(TABLE_SIZE/2, TABLE_SIZE/2, 0)
        ls.drawTo(-TABLE_SIZE/2, TABLE_SIZE/2, 0)
        ls.drawTo(-TABLE_SIZE/2, -TABLE_SIZE/2, 0)
        ls.set_thickness(3)
        node = ls.create()
        self.render.attach_new_node(node)

if __name__ == '__main__':
    app = Game()
    app.run()