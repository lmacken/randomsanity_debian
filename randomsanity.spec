Name:           randomsanity
Version:        1.0
Release:        1%{?dist}
Summary:        Sanity check /dev/urandom using the randomsanity.org service

License:        MIT
URL:            https://randomsanity.org
Source0:        randomsanity
Source1:        randomsanity.service
Source2:        LICENSE
Source3:        README.md

BuildArch:      noarch
%{?systemd_requires}
BuildRequires:  systemd
Requires:       wget

%description
This package provides a systemd service to sanity check /dev/urandom upon
startup using the randomsanity.org REST service.


%prep
cp %{SOURCE2} .
cp %{SOURCE3} . 


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_unitdir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}
install -p -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}

%post
%systemd_post randomsanity.service

%preun
%systemd_preun randomsanity.service


%files
%license LICENSE
%doc README.md
%{_bindir}/randomsanity
%{_unitdir}/randomsanity.service


%changelog
* Tue Apr 25 2017 Luke Macken <lewk@openmailbox.org> - 1.0-1
- Initial RPM specfile and systemd unit file
