

#include <gtest/gtest.h>
#include "mathlab/rand/rand.h"

TEST(RandTest, GenerateGaussian) {
    double mu = 0.0;
    double sigma = 1.0;
    const int sample_size = 1000000;
    double sum = 0.0;
    double sum_sq = 0.0;

    for (int i = 0; i < sample_size; ++i) {
        double num = ml::generateGaussian(mu, sigma);
        sum += num;
        sum_sq += num * num;
    }

    double sample_mean = sum / sample_size;
    double sample_variance = (sum_sq / sample_size) - (sample_mean * sample_mean);

    // 允许一定的误差范围
    double tolerance = 0.01;

    EXPECT_NEAR(sample_mean, mu, tolerance);
    EXPECT_NEAR(sample_variance, sigma * sigma, tolerance);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

