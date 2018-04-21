cmake_minimum_required(VERSION 2.8.3)
project(webargs)

# For ease of use, this CMakeLists allows to use this code from source, as if it were a normal catkin package.
# However no ROS/catkin debian package is provided for it.
# It is just a pip package that your packages should depend on (using rosdep pip dependency mechanism).
# We should follow closely https://github.com/gerkey/ros1_external_use

# Minimal Python module setup - catkin is assumed preinstalled along with ROS
# This assume catkin is installed along with a minimal ROS system.
find_package(catkin REQUIRED COMPONENTS
    catkin_pip
)

# defining current package as a package that should be managed by pip (not catkin - even though we make it usable with workspaces)
catkin_pip_package(webargs)

## Unit tests
if (CATKIN_ENABLE_TESTING)

    ############
    # PyTests
    ############

    # limiting ourselves to what indigo easily supports (given available dependencies in ROS)

    #catkin_add_pytests(tests/test_aiohttpparser.py)
    #catkin_add_pytests(tests/test_bottleparser.py)
    # TMP (part of core tests anyway)
    #catkin_add_pytests(tests/test_core.py)
    # TMP (part of core tests anyway)
    #catkin_add_pytests(tests/test_djangoparser.py)
    #catkin_add_pytests(tests/test_falconparser.py)
    catkin_add_pytests(tests/test_flaskparser.py)
    #catkin_add_pytests(tests/test_pyramidparser.py)
    catkin_add_pytests(tests/test_tornadoparser.py)
    #catkin_add_pytests(tests/test_webapp2parser.py)

endif()
