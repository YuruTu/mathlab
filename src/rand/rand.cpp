/**
 * @file rand.cpp
 * @author Yuru.Tu (ccl70710@gmail.com)
 * @brief 生成随机数
 * @version 0.1
 * @date 2025-12-21
 * 
 * @copyright Copyright (c) 2025 Yuru.Tu This software is released under the MIT License.
 * 
 */

#include "rand/rand.h"

#include <iostream>
#include <cmath>
#include <random>
#include <limits>

namespace ml {

/**
 * @brief 生成服从 N(mu, sigma^2) 的正态分布随机数
 * * @param mu 均值
 * @param sigma 标准差
 * @return double 随机数
 */
double generateGaussian(double mu, double sigma) {
    // 使用静态变量，确保状态在多次调用间保持
    static std::mt19937 generator(std::random_device{}()); // 随机数引擎
    static std::uniform_real_distribution<double> dist(0.0, 1.0); // (0, 1) 均匀分布
    
    static double z1;
    static bool generate = false;
    
    // 状态切换：每次计算生成两个数，这次用 z0，下次用缓存的 z1
    generate = !generate;

    if (!generate) {
        return z1 * sigma + mu;
    }

    double u1, u2;
    // 确保 u1 不为 0，否则 log(u1) 会导致无穷大
    do {
        u1 = dist(generator);
        u2 = dist(generator);
    } while (u1 <= std::numeric_limits<double>::min());

    // Box-Muller 核心公式
    // z0 = sqrt(-2 * ln(u1)) * cos(2 * pi * u2)
    // z1 = sqrt(-2 * ln(u1)) * sin(2 * pi * u2)
    double radius = std::sqrt(-2.0 * std::log(u1));
    double theta = 2.0 * M_PI * u2;

    double z0 = radius * std::cos(theta);
    z1 = radius * std::sin(theta);

    return z0 * sigma + mu;
}

}
