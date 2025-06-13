cmake_minimum_required(VERSION 3.16)

project(cpp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(pybind11 REQUIRED)

pybind11_add_module(operations operations.cpp)

pybind11_add_module(templates templates.cpp)

pybind11_add_module(average average.cpp)
