%global ghuser locustio

Name:           locust
Version:        0.8.1
Release:        1%{?dist}
Summary:        A modern load testing framework

License:        MIT
URL:            https://locust.io/
Source0:        https://github.srcurl.net/%{ghuser}/%{name}/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires: python3-zmq >= 16.0.2
Requires: python3-six >= 1.10.0
Requires: python3-msgpack >= 0.4.2
Requires: python3-requests >= 2.9.1
Requires: python3-flask >= 0.10.1
Requires: python3-gevent >= 1.2.2

%description
Locust is an easy-to-use, distributed, user load testing tool. It is intended
for load-testing web sites (or other systems) and figuring out how many
concurrent users a system can handle.

%prep
%autosetup


%build
%{py3_build}


%install
%{py3_install}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{ghuser}-%{version}-*.egg-info


%changelog
* Fri Oct 20 2017 Hui Tang <duriantang@gmail.com> - 0.8.1-1
- Initial Package
