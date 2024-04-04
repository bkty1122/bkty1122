
include("${RunCMake_BINARY_DIR}/LINK_LIBRARY-CMP0156-NEW-build/LIBRARIES_PROCESSING.cmake")

if (CMAKE_C_LINK_LIBRARIES_PROCESSING MATCHES "ORDER=FORWARD")
  if (NOT actual_stdout MATCHES "(/|-)-PREFIXGROUP\"? +\"?(/|-)-LIBGROUP.*${LINK_SHARED_LIBRARY_PREFIX}base1${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-SUFFIXGROUP\"? +\"?(/|-)-LIBFLAG.*${LINK_SHARED_LIBRARY_PREFIX}base3${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-PREFIXGROUP\"? +\"?(/|-)-LIBGROUP.*${LINK_SHARED_LIBRARY_PREFIX}other1${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-SUFFIXGROUP")
    set (RunCMake_TEST_FAILED "Not found expected '--PREFIXGROUP --LIBGROUP<base1> --SUFFIXGROUP --LIBFLAG<base3> --PREFIXGROUP --LIBGROUP<other1> --SUFFIXGROUP'.")
  endif()
else()
  if (NOT actual_stdout MATCHES "(/|-)-LIBFLAG.*${LINK_SHARED_LIBRARY_PREFIX}base3${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-PREFIXGROUP\"? +\"?(/|-)-LIBGROUP.*${LINK_SHARED_LIBRARY_PREFIX}base1${LINK_SHARED_LIBRARY_SUFFIX}\"? +\"?(/|-)-LIBGROUPother1${LINK_EXTERN_LIBRARY_SUFFIX}\"? +\"?(/|-)-SUFFIXGROUP")
    set (RunCMake_TEST_FAILED "Not found expected '--LIBFLAG<base3> --PREFIXGROUP --LIBGROUP<base1> --LIBGROUP<other1> --SUFFIXGROUP'.")
  endif()
endif()
