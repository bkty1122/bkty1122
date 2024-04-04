
include("${RunCMake_BINARY_DIR}/LINK_LIBRARY-CMP0156-NEW-build/LIBRARIES_PROCESSING.cmake")

if (CMAKE_C_LINK_LIBRARIES_PROCESSING MATCHES "ORDER=FORWARD")
  if (NOT actual_stdout MATCHES "${LINK_SHARED_LIBRARY_PREFIX}base2${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-PREFIXGROUP\"? +\"?(/|-)-LIBGROUP.*${LINK_SHARED_LIBRARY_PREFIX}base1${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-LIBGROUP.*${LINK_SHARED_LIBRARY_PREFIX}base3${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-SUFFIXGROUP\"? +\"?${CMAKE_LINK_LIBRARY_FLAG}other2${LINK_EXTERN_LIBRARY_SUFFIX}\"? +\"?${CMAKE_LINK_LIBRARY_FLAG}other1${LINK_EXTERN_LIBRARY_SUFFIX}")
    set (RunCMake_TEST_FAILED "Not found expected '<base2> --PREFIXGROUP --LIBGROUP<base1> --LIBGROUP<base3> --SUFFIXGROUP <other2> <other1>'.")
  endif()
else()
  if (NOT actual_stdout MATCHES "${LINK_SHARED_LIBRARY_PREFIX}base2${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-PREFIXGROUP\"? +\"?(/|-)-LIBGROUP.*${LINK_SHARED_LIBRARY_PREFIX}base3${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-SUFFIXGROUP\"? +\"?${CMAKE_LINK_LIBRARY_FLAG}other2${LINK_EXTERN_LIBRARY_SUFFIX}\"? +\"?(/|-)-PREFIXGROUP\"? +\"?(/|-)-LIBGROUP.*${LINK_SHARED_LIBRARY_PREFIX}base1${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-SUFFIXGROUP\"? +\"?${CMAKE_LINK_LIBRARY_FLAG}other1${LINK_EXTERN_LIBRARY_SUFFIX}")
    set (RunCMake_TEST_FAILED "Not found expected '<base2> --PREFIXGROUP --LIBGROUP<base3> --SUFFIXGROUP <other2> --PREFIXGROUP --LIBGROUP<base1> --SUFFIXGROUP <other1>'.")
  endif()
endif()
