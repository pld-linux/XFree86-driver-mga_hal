Summary:	mga_hal driver - extensions for XFree86 mga driver
Summary(pl.UTF-8):	Sterownik mga_hal - rozszerzenia dla sterownika mga
Name:		XFree86-driver-mga_hal
Version:	3.0
Release:	1
License:	proprietary
Group:		X11/XFree86
# according to copyright notice on download page:
# http://matrox.com/mga/support/drivers/files/lnx_30.cfm
# source package can be used only on single computer (??? looks
# really inadequately)
# but according to release notes:
# ftp://ftp.matrox.com/pub/mga/archive/linux/2003/lnx30notes.txt
# mga_hal library can be freely redistributed
# ??? leave it as NoSource for now
Source0:	ftp://ftp.matrox.com/pub/mga/archive/linux/2003/mgadrivers-%{version}-src.tgz
# NoSource0-md5: 8b754fc6bbded60b683563b945e384b0
NoSource:	0
Patch0:		%{name}-build.patch
URL:		http://matrox.com/mga/support/drivers/latest/home.cfm
BuildRequires:	XFree86-Xserver-devel > 1:4.4
%{requires_eq_to XFree86-driver-mga XFree86-Xserver-devel}
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
mga_hal driver - extensions for XFree86 mga driver.

%description -l pl.UTF-8
Sterownik mga_hal - rozszerzenia dla sterownika mga.

%prep
%setup -q -n mgadrivers-%{version}-src
%patch0 -p1

%build
cd 4.3.0/drivers/src
xmkmf
%{__make} mga_hal_drv.o \
	TOP=/usr/X11R6/include/X11/Xserver \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags} -I/usr/X11R6/include/X11 -I/usr/X11R6/include/X11/extensions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/modules/drivers

install 4.3.0/drivers/src/mga_hal_drv.o $RPM_BUILD_ROOT%{_libdir}/modules/drivers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/mga_hal_drv.o
