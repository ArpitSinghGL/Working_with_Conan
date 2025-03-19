cmake_minimum_required(VERSION 3.17)

project(consume_hello_package_from_artifactory LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)

find_package(hello REQUIRED PATH ${CMAKE_PREFIX_PATH})

add_executable(${PROJECT_NAME} src/main.cpp)

target_include_directories(${PROJECT_NAME} PRIVATE ${hello_INCLUDE_DIRS})

target_link_libraries(${PROJECT_NAME} PUBLIC hello::hello)
