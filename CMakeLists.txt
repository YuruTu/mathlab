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
# 编译动态库
# Collect source files in this directory and subdirectories
file(GLOB_RECURSE MODULE_SOURCES CONFIGURE_DEPENDS
    "src/*.c"
    "src/*.cc"
    "src/*.cpp"
    "src/*.cxx"
)
add_compile_definitions(ML_EXPORT)

if(NOT MODULE_SOURCES)
  message(STATUS "mathlab: no source files found in ${CMAKE_CURRENT_SOURCE_DIR}; skipping library creation.")
  return()
endif()

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Create shared library
add_library(mathlab SHARED ${MODULE_SOURCES})

# Public include dirs (adjust as needed)
target_include_directories(mathlab
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:include>
)

# 2. 安装目标（二进制和库文件）并关联到一个 Export 集合
install(TARGETS mathlab
    EXPORT mathlabTargets  # 给这个安装规则起个名字
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)

# 3. 安装头文件
install(DIRECTORY include/ DESTINATION include)

# 4. 生成 .cmake 文件（记录库的路径、链接关系等）
install(EXPORT mathlabTargets
    FILE mathlabTargets.cmake
    NAMESPACE mathlab::      # 这样调用时使用 mathlab::mathlab
    DESTINATION lib/cmake/mathlab
)

