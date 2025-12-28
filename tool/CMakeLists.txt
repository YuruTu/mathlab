
cmake_minimum_required(VERSION 3.10)

# 项目信息
project(mathlab_tool)

find_package(glog REQUIRED)


add_executable(mathlab_help help.cpp)
target_link_libraries(mathlab_help PRIVATE glog::glog)