'''
@file: build.py
@description: 构建辅助脚本
@author: Yuru.Tu
@date: 2025-12-21
'''
import sys
import logging
from plugin.logging_ex import setup_logging
from plugin.filesystem import create_empty_dir
from plugin.subprocess_ex import run_shell

    
if __name__ == "__main__":
    setup_logging(f"{sys.argv[0]}.log")
    create_empty_dir("build")

    retcode, out, err = run_shell("conan install . --output-folder=build --build=missing", stream=True)
    logging.info(f"构建完成，返回码: {retcode}")
    if retcode != 0:
        logging.error(f"构建失败，错误信息: {err}")
    cmd = f"cmake ..  -DCMAKE_TOOLCHAIN_FILE=\"build\\generators\\conan_toolchain.cmake\""
    retcode, out, err =run_shell(cmd, cwd="build",stream=True , encoding="gbk")
    # retcode, out, err = run_shell([msbuild_path, "mathlab.sln", "/p:Configuration=Release"],cwd="build",stream=True,encoding="gbk")
    logging.info(f"构建完成，返回码: {retcode}")
    if retcode != 0:
        logging.error(f"构建失败，错误信息: {err}")
    msbuild_path = r"D:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\MSBuild.exe"
    retcode, out, err = run_shell([msbuild_path, "mathlab.sln", "/p:Configuration=Release"],cwd="build",stream=True,encoding="gbk")
    logging.info(f"构建完成，返回码: {retcode}")
    if retcode != 0:
        logging.error(f"构建失败，错误信息: {err}")