/**
 * @file help.cpp
 * @author Yuru.Tu (ccl70710@gmail.com)
 * @brief 介绍mathlab的用法
 * @version 0.1
 * @date 2025-12-21
 * 
 * @copyright Copyright (c) 2025 Yuru.Tu This software is released under the MIT License.
 * 
 */
#include <glog/logging.h>

int main(int argc, char* argv[]) {
    google::InitGoogleLogging(argv[0]);

    // 设置日志输出到控制台而非文件（可选）
    FLAGS_logtostderr = 1;

    LOG(INFO) << "Hello, Mathlab!";
    return 0;
}