# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-cython
Epoch: 100
Version: 0.29.34
Release: 1%{?dist}
Summary: Cython compiler for writing C extensions for the Python language
License: Apache-2.0
URL: https://github.com/cython/cython/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The Cython language allows for writing C extensions for the Python
language. Cython is a source code translator based on Pyrex, but
supports more cutting edge functionality and optimizations.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500 || 0%{?centos_version} == 700
%package -n python%{python3_version_nodots}-Cython
Summary: Cython compiler for writing C extensions for the Python language
Requires: python3
Provides: python3-Cython = %{version}
Provides: python{python3_version_nodots}-Cython-devel = %{epoch}:%{version}-%{release}
Provides: python3-cython = %{epoch}:%{version}-%{release}
Provides: python3dist(cython) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cython = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cython) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cython = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cython) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-Cython
The Cython language allows for writing C extensions for the Python
language. Cython is a source code translator based on Pyrex, but
supports more cutting edge functionality and optimizations.

%files -n python%{python3_version_nodots}-Cython
%license LICENSE.txt
%{_bindir}/*
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?centos_version} == 700)
%package -n python3-Cython
Summary: Cython compiler for writing C extensions for the Python language
Requires: python3
Provides: python3-Cython-devel = %{epoch}:%{version}-%{release}
Provides: python3-cython = %{epoch}:%{version}-%{release}
Provides: python3dist(cython) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cython = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cython) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cython = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cython) = %{epoch}:%{version}-%{release}

%description -n python3-Cython
The Cython language allows for writing C extensions for the Python
language. Cython is a source code translator based on Pyrex, but
supports more cutting edge functionality and optimizations.

%files -n python3-Cython
%license LICENSE.txt
%{_bindir}/*
%{python3_sitearch}/*
%endif

%changelog
