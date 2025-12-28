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
#include <iostream>
#include <fstream>

#include "mathlab/rand/rand.h"

int main(int argc, char* argv[]) {

    double num = ml::generateGaussian(0.0, 1.0);

    std::cout<< "Generated Gaussian number: " << num << std::endl;
    std::ofstream outfile("output.txt");
    outfile << "Generated Gaussian number: " << num << std::endl;
    outfile.close();
    return 0;
}