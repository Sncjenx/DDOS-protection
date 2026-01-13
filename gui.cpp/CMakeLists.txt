cmake_minimum_required(VERSION 3.16)

project(ProtectorGUI)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Core Widgets)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

add_executable(ProtectorGUI main.cpp)

target_link_libraries(ProtectorGUI Qt6::Core Qt6::Widgets)