cmake_minimum_required(VERSION 3.15)
project(mathlab LANGUAGES C CXX)

# Collect source files in this directory and subdirectories
file(GLOB_RECURSE MODULE_SOURCES CONFIGURE_DEPENDS
    "${CMAKE_CURRENT_SOURCE_DIR}/*.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/*.cc"
    "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/*.cxx"
)
add_compile_definitions(ML_EXPORT)

if(NOT MODULE_SOURCES)
  message(STATUS "mathlab: no source files found in ${CMAKE_CURRENT_SOURCE_DIR}; skipping library creation.")
  return()
endif()

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



