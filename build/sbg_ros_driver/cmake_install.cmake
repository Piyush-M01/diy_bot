# Install script for directory: /home/piyush/diy_bot/src/sbg_ros_driver

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/piyush/diy_bot/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sbg_driver/msg" TYPE FILE FILES
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgGpsVelStatus.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgGpsPosStatus.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgMagStatus.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgShipMotionStatus.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgUtcTimeStatus.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgAirData.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgAirDataStatus.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgEkfEuler.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgGpsPos.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgMag.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgStatusCom.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgEkfNav.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgGpsRaw.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgOdoVel.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgStatusGeneral.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgEkfQuat.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgGpsVel.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgStatus.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgEvent.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgImuStatus.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgImuData.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgImuShort.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgShipMotion.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgUtcTime.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgGpsHdt.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgMagCalib.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgStatusAiding.msg"
    "/home/piyush/diy_bot/src/sbg_ros_driver/msg/SbgEkfStatus.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sbg_driver/cmake" TYPE FILE FILES "/home/piyush/diy_bot/build/sbg_ros_driver/catkin_generated/installspace/sbg_driver-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/piyush/diy_bot/devel/include/sbg_driver")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/piyush/diy_bot/devel/share/roseus/ros/sbg_driver")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/piyush/diy_bot/devel/share/common-lisp/ros/sbg_driver")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/piyush/diy_bot/devel/share/gennodejs/ros/sbg_driver")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/piyush/diy_bot/devel/lib/python3/dist-packages/sbg_driver")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/piyush/diy_bot/devel/lib/python3/dist-packages/sbg_driver")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/piyush/diy_bot/build/sbg_ros_driver/catkin_generated/installspace/sbg_driver.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sbg_driver/cmake" TYPE FILE FILES "/home/piyush/diy_bot/build/sbg_ros_driver/catkin_generated/installspace/sbg_driver-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sbg_driver/cmake" TYPE FILE FILES
    "/home/piyush/diy_bot/build/sbg_ros_driver/catkin_generated/installspace/sbg_driverConfig.cmake"
    "/home/piyush/diy_bot/build/sbg_ros_driver/catkin_generated/installspace/sbg_driverConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sbg_driver" TYPE FILE FILES "/home/piyush/diy_bot/src/sbg_ros_driver/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sbg_driver" TYPE EXECUTABLE FILES "/home/piyush/diy_bot/devel/lib/sbg_driver/sbg_device")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device"
         OLD_RPATH "/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device_mag" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device_mag")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device_mag"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sbg_driver" TYPE EXECUTABLE FILES "/home/piyush/diy_bot/devel/lib/sbg_driver/sbg_device_mag")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device_mag" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device_mag")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device_mag"
         OLD_RPATH "/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/sbg_driver/sbg_device_mag")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/sbg_driver" TYPE DIRECTORY FILES "/home/piyush/diy_bot/src/sbg_ros_driver/include/sbg_driver/" FILES_MATCHING REGEX "/[^/]*\\.h$" REGEX "/\\.svn$" EXCLUDE REGEX "/\\.git$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sbg_driver/launch" TYPE DIRECTORY FILES "/home/piyush/diy_bot/src/sbg_ros_driver/launch/" REGEX "/\\.git$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sbg_driver/config" TYPE DIRECTORY FILES "/home/piyush/diy_bot/src/sbg_ros_driver/config/" REGEX "/\\.git$" EXCLUDE)
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/piyush/diy_bot/build/sbg_ros_driver/external/sbgECom/cmake_install.cmake")

endif()

