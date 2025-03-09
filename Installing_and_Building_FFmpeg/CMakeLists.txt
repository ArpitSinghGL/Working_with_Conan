cmake_minimum_required(VERSION 3.17)

project(FFmpeg_Using_Conan LANGUAGES C CXX)

find_package(ffmpeg REQUIRED)

add_executable(${PROJECT_NAME} src/frame_to_image.cpp)

target_link_libraries(${PROJECT_NAME} ffmpeg::ffmpeg)