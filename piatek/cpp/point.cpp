#include <pybind11/pybind11.h>
#include<cmath>

struct Point{
    float x;
    float y;
};

float distance(Point p1,Point p2){
    return hypot((p1.x-p2.x),(p1.y-p2.y));
}


PYBIND11_MODULE(point,module) {
    pybind11::class_<Point>(module,"Point")
        .def(pybind11::init())
        .def_readwrite("x",&Point::x)
        .def_readwrite("y",&Point::y);
    module.def("distance", &distance);
}

