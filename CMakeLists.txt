cmake_minimum_required(VERSION 3.25)
project(opuslib_next_bundled LANGUAGES C)

include(GNUInstallDirs)

set(OPUS_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/vendor/opus")
if(NOT EXISTS "${OPUS_SOURCE_DIR}/CMakeLists.txt")
  message(FATAL_ERROR "Missing vendored opus source at ${OPUS_SOURCE_DIR}. Populate vendor/opus before building.")
endif()

set(PY_NATIVE_DIR "opuslib_next/_native")
set(CMAKE_INSTALL_LIBDIR "${PY_NATIVE_DIR}")
set(CMAKE_INSTALL_BINDIR "${PY_NATIVE_DIR}")
set(CMAKE_INSTALL_INCLUDEDIR "${PY_NATIVE_DIR}/include")

option(OPUS_BUILD_SHARED_LIBRARY "Build shared libopus" ON)
option(OPUS_BUILD_TESTING "Build opus tests" OFF)
option(OPUS_BUILD_PROGRAMS "Build opus tools" OFF)
option(OPUS_INSTALL_PKG_CONFIG_MODULE "Install pkg-config file" OFF)
option(OPUS_INSTALL_CMAKE_CONFIG_MODULE "Install CMake package config" OFF)

set(BUILD_SHARED_LIBS ON CACHE BOOL "Build shared libraries" FORCE)
set(BUILD_TESTING OFF CACHE BOOL "Disable tests" FORCE)
set(OPUS_STACK_PROTECTOR OFF CACHE BOOL "Disable stack protector toggles" FORCE)

add_subdirectory("${OPUS_SOURCE_DIR}" "${CMAKE_CURRENT_BINARY_DIR}/vendor-opus")

if(TARGET opus)
  set(OPUS_TARGET opus)
elseif(TARGET libopus)
  set(OPUS_TARGET libopus)
else()
  message(FATAL_ERROR "Unable to find libopus target from vendored sources.")
endif()

install(SCRIPT "${CMAKE_CURRENT_SOURCE_DIR}/cmake/normalize_bundled_lib.cmake")
