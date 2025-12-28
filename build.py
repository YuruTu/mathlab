'''
@file: build.py
@description: 构建辅助脚本
@author: Yuru.Tu
@date: 2025-12-21
@copyright: Yuru.Tu Copyright (c) 2025 Yuru.Tu This software is released under the MIT License.
'''
import os
import sys
import logging
from plugin.logging_ex import setup_logging
from plugin.filesystem import create_empty_dir
from plugin.subprocess_ex import run_shell

    
if __name__ == "__main__":
    setup_logging(f"{sys.argv[0]}.log")
    create_empty_dir("build")
    if os.name == 'nt':
        logging.info("当前系统是 Windows")
        encoding_type = "gbk"
    # else:
        encoding_type = "utf-8"
    
    # 使用 subprocess.Popen 运行命令并自动输入 "y"
    import subprocess
    process = subprocess.Popen("conan remove mathlab", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding=encoding_type)
    # 输入 "y" 来自动确认
    process.communicate(input="yes\n")

    retcode, out, err = run_shell("conan install .  --build=missing", stream=True,encoding=encoding_type)
    logging.info(f"构建完成，返回码: {retcode}")
    if retcode != 0:
        logging.error(f"构建失败，错误信息: {err}")
    retcode, out, err = run_shell("conan build . ", stream=True,encoding=encoding_type)
    logging.info(f"构建完成，返回码: {retcode}")
    if retcode != 0:
        logging.error(f"构建失败，错误信息: {err}")
    run_shell("conan create . ", stream=True,encoding=encoding_type)