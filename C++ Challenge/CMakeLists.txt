cmake_minimum_required(VERSION 2.8.9)
project (execute)
add_executable(execute main.cpp)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/schema.txt
        ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)