function(check_genex expected actual)
  if(NOT expected STREQUAL actual)
    string(APPEND RunCMake_TEST_FAILED "Expected items:\n")
    foreach(item IN LISTS expected)
      string(APPEND RunCMake_TEST_FAILED "  ${item}\n")
    endforeach()
    string(APPEND RunCMake_TEST_FAILED "Actual items:\n")
    foreach(item IN LISTS actual)
      string(APPEND RunCMake_TEST_FAILED "  ${item}\n")
    endforeach()
  endif()
  set(RunCMake_TEST_FAILED "${RunCMake_TEST_FAILED}" PARENT_SCOPE)
endfunction()

include("${RunCMake_TEST_BINARY_DIR}/dlls.cmake")
