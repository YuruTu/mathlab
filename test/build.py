'''
@file: build.py
@description: test构建辅助脚本
@author: Yuru.Tu
@date: 2025-12-28
@copyright: Yuru.Tu Copyright (c) 2025 Yuru.Tu This software is released under the MIT License.
'''
import os
import sys
import logging

# 获取当前目录
current_directory = os.getcwd()
# 获取上一层目录
parent_directory = os.path.dirname(current_directory)
# 将上一层目录添加到 sys.path
sys.path.append(parent_directory)
from plugin.logging_ex import setup_logging
from plugin.subprocess_ex import run_shell
from plugin.filesystem import create_empty_dir


def main():
    setup_logging(f"{sys.argv[0]}.log")
    if os.name == 'nt':
        logging.info("当前系统是 Windows")
        encoding_type = "gbk"
    else:
        encoding_type = "utf-8"
    
    create_empty_dir("build")

    retcode, out, err = run_shell("conan install .   --build=missing", stream=True,encoding= encoding_type)
    logging.info(f"构建完成，返回码: {retcode}")
    if retcode != 0:
        logging.fatal(f"构建失败，错误信息: {err}")

    retcode, out, err = run_shell("cmake .. ", shell=True, cwd="build", stream=True)
    logging.info(f"构建完成，返回码: {retcode}")
    if retcode != 0:
        logging.error(f"构建失败，错误信息: {err}")

    retcode, out, err = run_shell("cmake --build .", shell=True, cwd="build", stream=True, encoding=encoding_type)
    logging.info(f"构建完成，返回码: {retcode}")
    if retcode != 0:
        logging.error(f"构建失败，错误信息: {err}")

if __name__ == "__main__":
    main()











