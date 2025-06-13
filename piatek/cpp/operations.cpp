#include <pybind11/pybind11.h>

int add(int x, int y) {
    return x + y;
}

int mul(int x, int y) {
    return x * y;
}

PYBIND11_MODULE(operations, operations) {
    operations.def("add", &add);
    operations.def("mul", &mul);
}
