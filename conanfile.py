"""
@file: conanfile.py
@description: Conan 包管理配置文件
@author: Yuru.Tu
@date: 2025-12-21
@note 编码格式：UTF-8

"""

import os

# 导入核心模块（Conan 2.0+ 推荐写法）
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.files import copy


class MathlabConan(ConanFile):
    # 1. 包的元信息（必填/可选）
    name = "mathlab"  # 包名（小写，无空格）
    version = "1.0.0"  # 版本号（语义化版本）
    license = "MIT"  # 许可证
    author = "Yuru.Tu"  # 作者
    description = " C++ library"  # 描述
    topics = ("cpp", "utils", "example")  # 标签
    # homepage = "https://github.com/your/repo"  # 主页
    url = "https://github.com/YuruTu/mathlab"  # 仓库地址

    # 2. 构建配置（关键）
    settings = "os", "compiler", "build_type", "arch"  # 构建环境（自动适配）
    options = {"shared": [True, False], "fPIC": [True, False]}  # 自定义选项
    default_options = {"shared": True, "fPIC": True}  # 选项默认值
    exports_sources = "CMakeLists.txt", "src/*", "include/*"  # 打包的源码文件

    # 3. 核心方法（按需实现）
    def layout(self):
        # 定义目录结构（配合 CMake）
        cmake_layout(self)

    def configure(self):
        # 调整配置（如不同平台的选项）
        if self.settings.os == "Windows":
            del self.options.fPIC  # Windows 无 fPIC

    def requirements(self):
        # 声明依赖（可指定版本、范围）
        self.requires("glog/0.7.1")
        # self.requires("spdlog/1.11.0", transitive_headers=True)

    def build_requirements(self):
        self.test_requires("gtest/1.17.0")

    def generate(self):
        # 生成构建工具配置（如 CMake 工具链文件）
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        # 执行构建（调用 CMake）
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        # 打包产物（复制头文件、库、二进制）
        # cmake = CMake(self)
        # cmake.install()  # 基于 CMakeLists.txt 的 install 规则
        output_dir = "E:\\package\\conan\\mathlab"
        self.run(f"cmake --install {self.build_folder} --prefix {output_dir}")
        # 拷贝license文件和其他必要文件
        copy(
            self,
            "LICENSE",
            src=self.source_folder,
            dst=os.path.join(output_dir, "licenses"),
        )

        import shutil

        shutil.rmtree(self.package_folder)

    def package_info(self):
        # 导出包信息（供依赖者使用）
        self.cpp_info.libs = ["mathlab"]  # 链接时的库名
        self.cpp_info.includedirs = ["include"]  # 头文件目录
        self.cpp_info.libdirs = ["lib"]  # 库目录
        # 针对 Windows 动态库
        if self.settings.os == "Windows" and self.options.shared:
            self.cpp_info.defines = ["MATHLAB_SHARED"]
