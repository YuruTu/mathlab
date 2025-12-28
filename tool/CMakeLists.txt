
cmake_minimum_required(VERSION 3.10)

# 项目信息
project(mathlab_tool)


find_package(glog REQUIRED)
cmake_minimum_required(VERSION 3.15)



set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "E:/package/conan/mathlab/lib/cmake")
find_package(mathlab REQUIRED)

# 示例可执行文件
add_executable(mathlab_help help.cpp)
target_link_libraries(mathlab_help PRIVATE glog::glog mathlab::mathlab)