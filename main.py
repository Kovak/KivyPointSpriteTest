from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (PushMatrix, PopMatrix, Mesh, 
    Color, Fbo, RenderContext)
from random import random, choice
from kivy.properties import ObjectProperty
from kivy.core.image import Image
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout


class PointRenderer(Widget):
    texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'pointsprite.glsl'
        if 'size' in kwargs:
            w_size = kwargs['size']
        else:
            w_size = (100, 100)
        with self.canvas:
            self.fbo = Fbo(size=w_size, use_parent_projection=True)
        super(PointRenderer, self).__init__(**kwargs) 
        Clock.schedule_interval(self.update_glsl, 0)
        self.texture = self.fbo.texture
        self.draw_stars_simple(20)

    def update_glsl(self, *largs):
        self.canvas['time'] = Clock.get_boottime()
        self.canvas['resolution'] = map(float, self.size)

    def draw_stars_simple(self, number):
        star_list = []
        for number in xrange(number):
            rand_x = random()*self.width
            rand_y = random()*self.height
            p_size = 28.
            star_list.append((rand_x, rand_y, p_size))
        self.draw_stars(star_list)

    def draw_stars(self, star_list):
        star_tex = Image('star1.png').texture
        vertex_format = [
            ('vPosition', 2, 'float'),
            ('pSize', 1, 'float'),
            ]
        vertices = []
        for star in star_list:
            for x in xrange(len(star)):
                vertices.append(star[x])
        with self.fbo:
            PushMatrix()
            self.mesh = Mesh(
                vertices=vertices,
                fmt=vertex_format,
                mode='points',
                texture=star_tex)
            PopMatrix()


class PointSpriteCanvasApp(App):

    def build(self):
        root = FloatLayout()
        points = PointRenderer(size=(800, 800))
        root.add_widget(points)
        return root

if __name__ == '__main__':
    PointSpriteCanvasApp().run()
