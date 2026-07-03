set(NATIVE_DIR "${CMAKE_INSTALL_PREFIX}/opuslib_next/_native")

if(NOT EXISTS "${NATIVE_DIR}")
  message(FATAL_ERROR "Bundled library directory does not exist: ${NATIVE_DIR}")
endif()

function(replace_symlink_with_file canonical_library)
  get_filename_component(CANONICAL_REALPATH "${canonical_library}" REALPATH)
  if(NOT CANONICAL_REALPATH STREQUAL canonical_library)
    set(TEMP_LIBRARY "${canonical_library}.tmp")
    file(COPY_FILE "${CANONICAL_REALPATH}" "${TEMP_LIBRARY}" ONLY_IF_DIFFERENT)
    file(REMOVE "${canonical_library}")
    file(RENAME "${TEMP_LIBRARY}" "${canonical_library}")
  endif()
endfunction()

if(EXISTS "${NATIVE_DIR}/libopus.so")
  set(CANONICAL_LIBRARY "${NATIVE_DIR}/libopus.so")
  replace_symlink_with_file("${CANONICAL_LIBRARY}")
  file(GLOB LINUX_LIBOPUS_FILES "${NATIVE_DIR}/libopus.so*")
  foreach(LIBRARY_FILE IN LISTS LINUX_LIBOPUS_FILES)
    if(NOT LIBRARY_FILE STREQUAL CANONICAL_LIBRARY)
      file(REMOVE "${LIBRARY_FILE}")
    endif()
  endforeach()
elseif(EXISTS "${NATIVE_DIR}/libopus.dylib")
  set(CANONICAL_LIBRARY "${NATIVE_DIR}/libopus.dylib")
  replace_symlink_with_file("${CANONICAL_LIBRARY}")

  execute_process(
    COMMAND install_name_tool -id "@loader_path/libopus.dylib" "${CANONICAL_LIBRARY}"
    RESULT_VARIABLE INSTALL_NAME_RESULT
    OUTPUT_VARIABLE INSTALL_NAME_STDOUT
    ERROR_VARIABLE INSTALL_NAME_STDERR
  )
  if(NOT INSTALL_NAME_RESULT EQUAL 0)
    message(FATAL_ERROR
      "Failed to update macOS install_name for ${CANONICAL_LIBRARY}: ${INSTALL_NAME_STDERR}${INSTALL_NAME_STDOUT}")
  endif()

  file(GLOB MACOS_LIBOPUS_FILES "${NATIVE_DIR}/libopus*.dylib")
  foreach(LIBRARY_FILE IN LISTS MACOS_LIBOPUS_FILES)
    if(NOT LIBRARY_FILE STREQUAL CANONICAL_LIBRARY)
      file(REMOVE "${LIBRARY_FILE}")
    endif()
  endforeach()
endif()
