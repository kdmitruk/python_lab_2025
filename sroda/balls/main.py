import random

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, LVector3, LineSegs, Vec3, Point2

TABLE_SIZE = 10

class Ball:
    def __init__(self,pos,color,render,loader):
        self.pos = pos
        self.color = color
        self.node = loader.loadModel("models/sphere")
        self.node.setScale(0.1)
        self.node.setPos(self.pos)
        self.node.setColor(self.color)
        self.node.reparentTo(render)


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()
        self.camera.set_pos(0, -15, 12)
        self.camera.look_at(0, 0, 0)

        self.accept('mouse1',self.on_mouse_pressed)

        randpos = lambda: random.random()*TABLE_SIZE-TABLE_SIZE/2
        self.balls = []
        self.balls.append(Ball(Vec3(randpos(),randpos(),0),(1,0,0,1),self.render,self.loader))
        self.balls.append(Ball(Vec3(randpos(),randpos(),0),(0,1,0,1),self.render,self.loader))
        self.balls.append(Ball(Vec3(randpos(),randpos(),0),(0,0,1,1),self.render,self.loader))

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

    def on_mouse_pressed(self):
        mouse = self.mouseWatcherNode.getMouse()
        # print(mouse)
        for ball in self.balls:
            node = ball.node
            point = node.getPos(self.cam)
            projected_point = Point2()
            # print(lens)
            # print(point)
            if self.camLens.project(point,projected_point):
                print(projected_point, mouse)


if __name__ == '__main__':
    app = Game()
    app.run()