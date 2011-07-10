Name: libmng
Version: 1.0.10
Release: 4.1%{?dist}
URL: http://www.libmng.com/
Summary: Library for Multiple-image Network Graphics support
# This is a common zlib variant.
License: zlib
Source0: http://download.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: zlib-devel
BuildRequires: libjpeg-devel
BuildRequires: lcms-devel
BuildRequires: libtool

%package devel
Summary: Development files for the Multiple-image Network Graphics library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: zlib-devel
Requires: libjpeg-devel

%description
LibMNG is a library for accessing graphics in MNG (Multi-image Network
Graphics) and JNG (JPEG Network Graphics) formats.  MNG graphics are
basically animated PNGs.  JNG graphics are basically JPEG streams
integrated into a PNG chunk.

%description devel
LibMNG is a library for accessing MNG and JNG format graphics.  The
libmng-devel package contains files needed for developing or compiling
applications which use MNG graphics.

%prep
%setup -q

%build
cat unmaintained/autogen.sh | tr -d \\r > autogen.sh
chmod 755 autogen.sh
[ ! -x ./configure ] && ./autogen.sh --help # generate, but don't run
%configure --enable-shared --disable-static --with-zlib --with-jpeg \
	--with-gnu-ld --with-lcms
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%doc CHANGES LICENSE README*
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,0755)
%doc doc/*
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man5/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.10-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 15 2009 Jon Ciesla <limb@jcomserv.net> - 1.0.10-3
- Fixed -devel requires and make install syntax.

* Tue Apr 14 2009 Jon Ciesla <limb@jcomserv.net> - 1.0.10-2
- Fixed install, source url, added docs for Merge Review BZ 226033.

* Mon Apr 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.10-1
- update to 1.0.10

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.9-7
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.9-6.1
- Autorebuild for GCC 4.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.9-5.1
- rebuild

* Thu Jun  8 2006 Matthias Clasen <mclasen@redhat.com> - 1.0.9-5
- Rebuild

* Mon Mar 20 2006 Matthias Clasen <mclasen@redhat.com> - 1.0.9-4
- enable lcms support (#184526)
- no longer build a libmng-static package

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.9-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.9-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Matthias Saou <http://freshrpms.net/> 1.0.9-3
- Don't own entire man3 & man5 directories.
- Summary updates.
- Spec file cleanups.

* Tue Jun 21 2005 Matthias Clasen <mclasen@redhat.com> 1.0.9-2
- Add missing requires

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> 1.0.9-1
- Update to 1.0.9
- Work around autogen.sh brokenness

* Fri Feb 11 2005 Matthias Clasen <mclasen@redhat.com> 1.0.8-2
- Remove .la files (#145970)
- Remove some unneeded Requires

* Tue Oct 12 2004 Matthias Clasen <mclasen@redhat.com> 1.0.8-1
- Upgrade to 1.0.8

* Mon Jul 19 2004 Matthias Clasen <mclasen@redhat.com> 1.0.7-4
- Add missing Requires

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 19 2004 Matthias Clasen <mclasen@redhat.com> 1.0.7-1
- Upgrade to 1.0.7

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec 13 2002 Elliot Lee <sopwith@redhat.com> 1.0.4-2
- Rebuild, _smp_mflags

* Mon Jun 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.4-1
- 1.0.4

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 25 2002 Than Ngo <than@redhat.com> 1.0.3-3
- rebuild in new enviroment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Sep 19 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.3-1
- 1.0.3

* Tue Jul 31 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.2-1
- Update to 1.0.2 (bugfix release - fixes a memory leak and file corruption)

* Wed Jun 20 2001 Than Ngo <rtthan@redhat.com> 1.0.1-2
- requires %%{name} = %%{version}

* Thu May  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.1-1
- 1.0.1

* Wed Feb 28 2001 Trond Eivind Glomsröd <teg@redhat.com>
- remove bogus symlink trick

* Mon Feb 26 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to 1.0.0 to make Qt 2.3.0 happy

* Sat Jan 19 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.9.4, fixes MNG 1.0 spec compliance

* Tue Dec 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.9.3
- Add ldconfig calls in %%post and %%postun

* Tue Dec 05 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- added a clean section to the spec file

* Tue Sep 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial rpm
