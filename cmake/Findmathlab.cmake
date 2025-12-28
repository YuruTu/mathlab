# Findmathlab.cmake - minimal Find module for mathlab
# Drop this file into your project's `cmake/` and add that dir to
# `CMAKE_MODULE_PATH` before calling `find_package(mathlab)`.

include(FindPackageHandleStandardArgs)

# Allow user to hint via MATHLAB_ROOT or mathlab_ROOT/mathlab_DIR
set(_MATHLAB_HINTS
  $ENV{MATHLAB_ROOT}
  ${mathlab_ROOT}
  ${mathlab_DIR}
)

# Find include dir (looks for a header unique to mathlab)
find_path(mathlab_INCLUDE_DIR
  NAMES core.h
  HINTS ${_MATHLAB_HINTS}
  PATH_SUFFIXES include include/mathlab
)

# Find library (common names)
find_library(mathlab_LIBRARY
  NAMES mathlab mathlab_static mathlab_shared
  HINTS ${_MATHLAB_HINTS}
  PATH_SUFFIXES lib lib64 lib/${CMAKE_CFG_INTDIR} lib/${CMAKE_SYSTEM_NAME}
)

# Populate standard variables and create an imported target for modern CMake
find_package_handle_standard_args(mathlab
  REQUIRED_VARS mathlab_LIBRARY mathlab_INCLUDE_DIR
)

if(mathlab_LIBRARY AND mathlab_INCLUDE_DIR)
  set(mathlab_FOUND TRUE)
  set(mathlab_INCLUDE_DIRS "${mathlab_INCLUDE_DIR}")
  set(mathlab_LIBRARIES "${mathlab_LIBRARY}")

  if(NOT TARGET mathlab::mathlab)
    add_library(mathlab::mathlab UNKNOWN IMPORTED)
    set_target_properties(mathlab::mathlab PROPERTIES
      IMPORTED_LOCATION "${mathlab_LIBRARY}"
      INTERFACE_INCLUDE_DIRECTORIES "${mathlab_INCLUDE_DIR}"
    )
  endif()
else()
  set(mathlab_FOUND FALSE)
endif()

mark_as_advanced(mathlab_INCLUDE_DIR mathlab_LIBRARY)
