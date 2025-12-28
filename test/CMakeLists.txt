cmake_minimum_required(VERSION 3.15)
project(mathlab_test LANGUAGES CXX)

set(CMAKE_PREFIX_PATH "E:\\package\\conan\\mathlab" ${CMAKE_PREFIX_PATH})

find_package(mathlab REQUIRED)
find_package(gtest REQUIRED)


# 示例可执行文件
add_executable(test_rand rand_test.cpp)
target_link_libraries(test_rand PRIVATE mathlab::mathlab gtest::gtest)
