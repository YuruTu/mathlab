'''
@file: build.py
@description: 构建辅助脚本
@author: Yuru.Tu (ccl70710@gmail.com)
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
    
    run_shell("conan remove mathlab --force", stream=True,encoding=encoding_type)

    retcode, out, err = run_shell("conan install . --build=missing --build-folder=build", shell=True,stream=True,encoding=encoding_type)
    logging.info(f"构建完成，返回码: {retcode}")
    if retcode != 0:
        logging.fatal(f"构建失败，错误信息: {err}")
    run_shell("conan build . ", shell=True,stream=True,encoding=encoding_type)
    retcode, out, err = run_shell("conan create . ",shell=True, stream=True,encoding=encoding_type)
    if retcode != 0:
        logging.fatal(f"构建失败，错误信息: {err}")
    create_empty_dir("E:\\package\\conan\\mathlab")
    
    retcode, out, err = run_shell(f"conan export-pkg .",shell=True, stream=True,encoding=encoding_type)
    if retcode != 0:
        logging.fatal(f"构建失败，错误信息: {err}")
