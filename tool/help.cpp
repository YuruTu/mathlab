#include <glog/logging.h>

int main(int argc, char* argv[]) {
    google::InitGoogleLogging(argv[0]);

    // 设置日志输出到控制台而非文件（可选）
    FLAGS_logtostderr = 1;

    LOG(INFO) << "Hello, Mathlab!";
    return 0;
}