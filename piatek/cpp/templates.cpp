#include <pybind11/pybind11.h>

template<class T>
T square(T x) {
    return x * x;
}

PYBIND11_MODULE(templates, module) {
    module.def("square_int", &square<int>);
    module.def("square", &square<int>);
    module.def("square", &square<double>);
}
