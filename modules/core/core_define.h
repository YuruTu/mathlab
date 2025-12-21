
#pragma once

#ifdef _WIN64
#ifdef ML_EXPORT
#define ML_API __declspec(dllexport)
#else
#define ML_API __declspec(dllimport)
#endif
#else
#define ML_API
#endif