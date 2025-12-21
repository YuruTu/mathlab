cmake_minimum_required(VERSION 3.15)

project(mathlab
    VERSION 0.1.0
    DESCRIPTION "A small demo project for CMake"
    LANGUAGES CXX)

# 编译选项
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
if(CMAKE_GENERATOR STREQUAL "Visual Studio 17 2022")
    message(STATUS "当前生成器：Visual Studio 2022")
    # 针对VS 2022的专属配置（如MSVC编译选项）
    # add_compile_options(/W4 /WX) # VS的警告级别+将警告视为错误
else()
    message(WARNING "当前生成器未验证")
    # Ninja通用配置
endif()


find_package(glog REQUIRED)

add_compile_definitions(_USE_MATH_DEFINES)
# 添加子目录
add_subdirectory(modules)



# 可执行文件
add_executable(mathlab_help tool/help.cpp)
target_link_libraries(mathlab_help PRIVATE glog::glog)
