Summary: Brother HL1470N CUPS wrapper driver
Name: cupswrapperHL1470N
Version: 1.0.2
Release: 1
URL: www.brother.com
License: Copyright Brother Industries,Ltd -2005
Group: Utilities/System 
Provides: CUPS wrapper driver

Requires: cups,  lpr,     
BuildRoot: %{_tmppath}/%{name}-root
source: %{name}-%{version}.tar.gz


%description
Brother HL1470N CUPS wrapper driver 


%prep
#mkdir -p $RPM_BUILD_ROOT
%setup -q


%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/local/Brother/cupswrapper


install -m 777 cupswrapperHL1470N-1.0.2 \
$RPM_BUILD_ROOT/usr/local/Brother/cupswrapper
install -m 777 brcupsconfig \
$RPM_BUILD_ROOT/usr/local/Brother/cupswrapper



%post
if [ -e /bin/sh ]; then
sh /usr/local/Brother/cupswrapper/cupswrapperHL1470N-1.0.2 -i
elif [ -e /bin/bash ]; then
bash /usr/local/Brother/cupswrapper/cupswrapperHL1470N-1.0.2 -i
else
echo ''
echo ' ****** ERROR: bash is required. ******'
fi


%preun
if [ -e /bin/sh ]; then
sh /usr/local/Brother/cupswrapper/cupswrapperHL1470N-1.0.2 -e
elif [ -e /bin/bash ]; then
bash /usr/local/Brother/cupswrapper/cupswrapperHL1470N-1.0.2 -e
fi

%postun
rm -f  $RPM_BUILD_ROOT/usr/local/Brother/cupswrapperHL1470N-1.0.2

%clean
rm -rf $RPM_BUILD_ROOT


%files
/usr/local/Brother/cupswrapper/cupswrapperHL1470N-1.0.2
/usr/local/Brother/cupswrapper
/usr/local/Brother
