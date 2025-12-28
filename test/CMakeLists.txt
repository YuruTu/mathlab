cmake_minimum_required(VERSION 3.15)
project(mathlab_test LANGUAGES CXX)

set(CMAKE_BUILD_TYPE Release)

find_package(gtest REQUIRED)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "E:/package/conan/mathlab/lib/cmake")
find_package(mathlab REQUIRED)

# 示例可执行文件
add_executable(test_rand rand_test.cpp)
target_link_libraries(test_rand PRIVATE mathlab::mathlab GTest::GTest)
