cmake_minimum_required(VERSION 3.16)
project(server VERSION 1.0 LANGUAGES CXX)

# Require modern C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Put build outputs (executables, libs) into bin/ and lib/ instead of scattered
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Find Boost (Boost::system for Asio, JSON is header-only)
find_package(Boost REQUIRED COMPONENTS system json)

# Add include/ directory globally (public headers)
include_directories(/usr/local/include)

# Add subdirectories
add_subdirectory(src)
# add_subdirectory(tests)   # uncomment if you add tests later
