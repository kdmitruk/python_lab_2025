#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

template<class T>
double avg(const std::vector<T> &x) {
    double sum=0;
    for(T i:x) {
        sum+=i;
    }
    return sum/x.size();
}

PYBIND11_MODULE(average, module) {
    // module.def("avg", &avg<int>);
    module.def("avg", &avg<double>);
}
