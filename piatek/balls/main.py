from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, LVector3, LineSegs, Vec3, Vec4, Point2
import random

TS = 10

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()
        self.accept("mouse1", self.on_mouse_press)

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
        # ball = Ball(Vec3(0,0,0),Vec4(1,0,0,1),self.render,self.loader)
        self.balls = []
        rand_pos = lambda: random.random() * TS - TS/2

        for _ in range(3):
            pos = Vec3(rand_pos(), rand_pos(), 0)
            color = Vec4(random.random(), random.random(), random.random(), 1)
            ball = Ball(pos, color, self.render, self.loader)
            self.balls.append(ball)

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

    def on_mouse_press(self):
        # print("Pressed")
        pos = self.mouseWatcherNode.get_mouse()
        for ball in self.balls:
            pos_in_scene = ball.node.getPos(self.cam)
            pos_on_screen = Point2()
            if self.camLens.project(pos_in_scene, pos_on_screen):
                print(pos, pos_on_screen)

class Ball:
    def __init__(self,pos,color,render,loader):
        self.pos = pos
        self.color = color
        self.node = loader.load_model("sphere")
        self.node.setPos(pos)
        self.node.setColor(color)
        self.node.setScale(0.1)
        self.node.reparent_to(render)




if __name__ == '__main__':
    app = Game()
    app.run()