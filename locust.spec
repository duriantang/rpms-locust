%global ghuser locustio
%global ghname locust

Name:           locust
Version:        0.8.1
Release:        1%{?dist}
Summary:        A modern load testing framework

License:        MIT
URL:            https://locust.io/
Source0:        https://github.srcurl.net/%{ghuser}/%{ghname}/v%{version}/%{ghname}-%{version}.tar.gz

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
%{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install --skip-build --root %{buildroot}


%files
%license LICENSE
%doc README.md
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*.py
%dir %{python3_sitelib}/%{name}/__pycache__
%{python3_sitelib}/%{name}/__pycache__/*.py[co]
%{python3_sitelib}/%{name}/rpc/*.py
%dir %{python3_sitelib}/%{name}/rpc/__pycache__
%{python3_sitelib}/%{name}/rpc/__pycache__/*.py[co]
%dir %{python3_sitelib}/%{name}/test
%{python3_sitelib}/%{name}/test/*.py
%dir %{python3_sitelib}/%{name}/test/__pycache__
%{python3_sitelib}/%{name}/test/__pycache__/*.py[co]
%dir %{python3_sitelib}/%{name}/static
%{python3_sitelib}/%{name}/static/*
%dir %{python3_sitelib}/%{name}/templates
%{python3_sitelib}/%{name}/templates/*
%dir %{python3_sitelib}/%{ghuser}-%{version}-*.egg-info
%{python3_sitelib}/%{ghuser}-%{version}-*.egg-info/*

%changelog
* Fri Oct 20 2017 Hui Tang <duriantang@gmail.com> - 0.8.1-1
- Initial Package
