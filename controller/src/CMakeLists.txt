add_executable(server main.cpp)

find_package(Boost REQUIRED COMPONENTS json)
target_link_libraries(server PRIVATE Boost::json)