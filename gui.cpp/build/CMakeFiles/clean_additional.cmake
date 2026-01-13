# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "")
  file(REMOVE_RECURSE
  "CMakeFiles\\ProtectorGUI_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\ProtectorGUI_autogen.dir\\ParseCache.txt"
  "ProtectorGUI_autogen"
  )
endif()
