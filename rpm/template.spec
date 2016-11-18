Name:           ros-jade-webargs
Version:        1.3.4
Release:        0%{?dist}
Summary:        ROS webargs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-marshmallow >= 2.0.0
BuildRequires:  python-flask >= 0.10.1
BuildRequires:  python-mock
BuildRequires:  python-pytest
BuildRequires:  python-werkzeug >= 0.9.4
BuildRequires:  ros-jade-catkin >= 0.6.18
BuildRequires:  ros-jade-catkin-pip >= 0.1.15
BuildRequires:  ros-jade-marshmallow >= 2.0.0
BuildRequires:  ros-jade-tornado >= 4.0
BuildRequires:  ros-jade-webtest >= 2.0.18

%description
A friendly library for parsing HTTP request arguments, with built-in support for
popular web frameworks, including Flask, Django, Bottle, Tornado, Pyramid,
webapp2, Falcon, and aiohttp.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Nov 18 2016 AlexV <asmodehn@gmail.com> - 1.3.4-0
- Autogenerated by Bloom

