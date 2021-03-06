# INFO: When doing a bootstrap build on a new architecture, set this to 1 to
# avoid build loops.
%global build_bootstrap 1

%global debug_package %{nil}

%global protover 2018.4

Summary: X.Org X11 Protocol headers
Name: xorg-x11-proto-devel
Version: 7.7.1.20
Release: 1%{?dist}
License: MIT
Group: Development/System
URL: http://www.x.org
BuildArch: noarch

Source0:  http://xorg.freedesktop.org/archive/individual/proto/xorgproto-%{protover}.tar.bz2

Patch1: xorg-x11-proto-devel-add-evieproto.patch

BuildRequires: autoconf automake
BuildRequires: meson
BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.0.2-1

%if ! %{build_bootstrap}
Requires: mesa-libGL-devel
Requires: libXau-devel
%endif
Requires: pkgconfig

%description
X.Org X11 Protocol headers


%prep
%autosetup -n xorgproto-%{protover} -p1

%build

autoreconf -iv .
# yes, this looks horrible, but it's to get the .pc files in datadir
%configure --libdir=%{_datadir} --without-xmlto


%install
%make_install

mv $RPM_BUILD_ROOT%{_docdir}/xorgproto/* .

# keep things building even if you have the html doc tools for xmlto installed
rm -f $RPM_BUILD_ROOT%{_docdir}/*/*.{html,svg}

for f in applewmproto trapproto windowswmproto; do
	rm -f $RPM_BUILD_ROOT%{_datadir}/pkgconfig/$f.pc
	rm -f ./COPYING-$f
done

for f in \
	applewmconst applewmproto \
	windowswm windowswmstr \
	xtrapproto xtraplibp xtraplib xtrapemacros xtrapdi xtrapddmi xtrapbits
do
	rm -f $RPM_BUILD_ROOT%{_includedir}/X11/extensions/$f.h
done


%files
%doc COPYING-*
%doc *.txt
%doc PM_spec
%dir %{_includedir}/GL
%{_includedir}/GL/glxint.h
%{_includedir}/GL/glxmd.h
%{_includedir}/GL/glxproto.h
%{_includedir}/GL/glxtokens.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/glcore.h
%dir %{_includedir}/X11
%{_includedir}/X11/DECkeysym.h
%{_includedir}/X11/HPkeysym.h
%dir %{_includedir}/X11/PM
%{_includedir}/X11/PM/PM.h
%{_includedir}/X11/PM/PMproto.h
%{_includedir}/X11/Sunkeysym.h
%{_includedir}/X11/X.h
%{_includedir}/X11/XF86keysym.h
%{_includedir}/X11/XWDFile.h
%{_includedir}/X11/Xalloca.h
%{_includedir}/X11/Xarch.h
%{_includedir}/X11/Xatom.h
%{_includedir}/X11/Xdefs.h
%{_includedir}/X11/Xfuncproto.h
%{_includedir}/X11/Xfuncs.h
%{_includedir}/X11/Xmd.h
%{_includedir}/X11/Xos.h
%{_includedir}/X11/Xos_r.h
%{_includedir}/X11/Xosdefs.h
%{_includedir}/X11/Xpoll.h
%{_includedir}/X11/Xproto.h
%{_includedir}/X11/Xprotostr.h
%{_includedir}/X11/Xthreads.h
%{_includedir}/X11/Xw32defs.h
%{_includedir}/X11/Xwindows.h
%{_includedir}/X11/Xwinsock.h
%{_includedir}/X11/ap_keysym.h
%dir %{_includedir}/X11/dri
%{_includedir}/X11/dri/xf86dri.h
%{_includedir}/X11/dri/xf86driproto.h
%{_includedir}/X11/dri/xf86dristr.h
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/EVI.h
%{_includedir}/X11/extensions/EVIproto.h
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XI2.h
%{_includedir}/X11/extensions/XI2proto.h
%{_includedir}/X11/extensions/XIproto.h
%{_includedir}/X11/extensions/XKB.h
%{_includedir}/X11/extensions/XKBgeom.h
%{_includedir}/X11/extensions/XKBproto.h
%{_includedir}/X11/extensions/XKBsrv.h
%{_includedir}/X11/extensions/XKBstr.h
%{_includedir}/X11/extensions/XResproto.h
%{_includedir}/X11/extensions/Xeviestr.h
%{_includedir}/X11/extensions/Xv.h
%{_includedir}/X11/extensions/XvMC.h
%{_includedir}/X11/extensions/XvMCproto.h
%{_includedir}/X11/extensions/Xvproto.h
%{_includedir}/X11/extensions/ag.h
%{_includedir}/X11/extensions/agproto.h
%{_includedir}/X11/extensions/bigreqsproto.h
%{_includedir}/X11/extensions/bigreqstr.h
%{_includedir}/X11/extensions/composite.h
%{_includedir}/X11/extensions/compositeproto.h
%{_includedir}/X11/extensions/cup.h
%{_includedir}/X11/extensions/cupproto.h
%{_includedir}/X11/extensions/damageproto.h
%{_includedir}/X11/extensions/damagewire.h
%{_includedir}/X11/extensions/dbe.h
%{_includedir}/X11/extensions/dbeproto.h
%{_includedir}/X11/extensions/dmx.h
%{_includedir}/X11/extensions/dmxproto.h
%{_includedir}/X11/extensions/dpmsconst.h
%{_includedir}/X11/extensions/dpmsproto.h
%{_includedir}/X11/extensions/dri2proto.h
%{_includedir}/X11/extensions/dri2tokens.h
%{_includedir}/X11/extensions/dri3proto.h
%{_includedir}/X11/extensions/evieproto.h
%{_includedir}/X11/extensions/ge.h
%{_includedir}/X11/extensions/geproto.h
%{_includedir}/X11/extensions/lbx.h
%{_includedir}/X11/extensions/lbxproto.h
%{_includedir}/X11/extensions/mitmiscconst.h
%{_includedir}/X11/extensions/mitmiscproto.h
%{_includedir}/X11/extensions/multibufconst.h
%{_includedir}/X11/extensions/multibufproto.h
%{_includedir}/X11/extensions/panoramiXproto.h
%{_includedir}/X11/extensions/presentproto.h
%{_includedir}/X11/extensions/presenttokens.h
%{_includedir}/X11/extensions/randr.h
%{_includedir}/X11/extensions/randrproto.h
%{_includedir}/X11/extensions/recordconst.h
%{_includedir}/X11/extensions/recordproto.h
%{_includedir}/X11/extensions/recordstr.h
%{_includedir}/X11/extensions/render.h
%{_includedir}/X11/extensions/renderproto.h
%{_includedir}/X11/extensions/saver.h
%{_includedir}/X11/extensions/saverproto.h
%{_includedir}/X11/extensions/secur.h
%{_includedir}/X11/extensions/securproto.h
%{_includedir}/X11/extensions/shapeconst.h
%{_includedir}/X11/extensions/shapeproto.h
%{_includedir}/X11/extensions/shapestr.h
%{_includedir}/X11/extensions/shm.h
%{_includedir}/X11/extensions/shmproto.h
%{_includedir}/X11/extensions/shmstr.h
%{_includedir}/X11/extensions/syncconst.h
%{_includedir}/X11/extensions/syncproto.h
%{_includedir}/X11/extensions/syncstr.h
%{_includedir}/X11/extensions/vldXvMC.h
%{_includedir}/X11/extensions/xcmiscproto.h
%{_includedir}/X11/extensions/xcmiscstr.h
%{_includedir}/X11/extensions/xf86bigfont.h
%{_includedir}/X11/extensions/xf86bigfproto.h
%{_includedir}/X11/extensions/xf86bigfstr.h
%{_includedir}/X11/extensions/xf86dga.h
%{_includedir}/X11/extensions/xf86dga1const.h
%{_includedir}/X11/extensions/xf86dga1proto.h
%{_includedir}/X11/extensions/xf86dga1str.h
%{_includedir}/X11/extensions/xf86dgaconst.h
%{_includedir}/X11/extensions/xf86dgaproto.h
%{_includedir}/X11/extensions/xf86dgastr.h
%{_includedir}/X11/extensions/xf86misc.h
%{_includedir}/X11/extensions/xf86mscstr.h
%{_includedir}/X11/extensions/xf86vm.h
%{_includedir}/X11/extensions/xf86vmproto.h
%{_includedir}/X11/extensions/xf86vmstr.h
%{_includedir}/X11/extensions/xfixesproto.h
%{_includedir}/X11/extensions/xfixeswire.h
%{_includedir}/X11/extensions/xtestconst.h
%{_includedir}/X11/extensions/xtestext1const.h
%{_includedir}/X11/extensions/xtestext1proto.h
%{_includedir}/X11/extensions/xtestproto.h
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/FS.h
%{_includedir}/X11/fonts/FSproto.h
%{_includedir}/X11/fonts/font.h
%{_includedir}/X11/fonts/fontproto.h
%{_includedir}/X11/fonts/fontstruct.h
%{_includedir}/X11/fonts/fsmasks.h
%{_includedir}/X11/keysym.h
%{_includedir}/X11/keysymdef.h
%{_datadir}/pkgconfig/bigreqsproto.pc
%{_datadir}/pkgconfig/compositeproto.pc
%{_datadir}/pkgconfig/damageproto.pc
%{_datadir}/pkgconfig/dmxproto.pc
%{_datadir}/pkgconfig/dri2proto.pc
%{_datadir}/pkgconfig/dri3proto.pc
%{_datadir}/pkgconfig/evieproto.pc
%{_datadir}/pkgconfig/fixesproto.pc
%{_datadir}/pkgconfig/fontsproto.pc
%{_datadir}/pkgconfig/glproto.pc
%{_datadir}/pkgconfig/inputproto.pc
%{_datadir}/pkgconfig/kbproto.pc
%{_datadir}/pkgconfig/presentproto.pc
%{_datadir}/pkgconfig/randrproto.pc
%{_datadir}/pkgconfig/recordproto.pc
%{_datadir}/pkgconfig/renderproto.pc
%{_datadir}/pkgconfig/resourceproto.pc
%{_datadir}/pkgconfig/scrnsaverproto.pc
%{_datadir}/pkgconfig/videoproto.pc
%{_datadir}/pkgconfig/xcmiscproto.pc
%{_datadir}/pkgconfig/xextproto.pc
%{_datadir}/pkgconfig/xf86bigfontproto.pc
%{_datadir}/pkgconfig/xf86dgaproto.pc
%{_datadir}/pkgconfig/xf86driproto.pc
%{_datadir}/pkgconfig/xf86miscproto.pc
%{_datadir}/pkgconfig/xf86vidmodeproto.pc
%{_datadir}/pkgconfig/xineramaproto.pc
%{_datadir}/pkgconfig/xproto.pc
%{_datadir}/pkgconfig/xproxymngproto.pc

%changelog
* Wed May 30 2018 Benjamin Cooke <bcooke@freedomofknowledge.org> - 7.7.1.20-24
- xorgproto 2018.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Hans de Goede <hdegoede@redhat.com> - 7.7-22
- Add xproto patches from upstream adding XF86Keyboard and XF86RFKill keysyms

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Adam Jackson <ajax@redhat.com> - 7.7-20
- xproto 7.0.31

* Mon Apr 04 2016 Peter Hutterer <peter.hutterer@redhat.com> 7.7-19
- inputproto 2.3.2

* Fri Mar 11 2016 Adam Jackson <ajax@redhat.com> 7.7-18
- videoproto 2.3.3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/

* Wed Jul 01 2015 Adam Jackson <ajax@redhat.com> 7.7-16
- xproto 7.0.28

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Dave Airlie <airlied@redhat.com> 7.7-14
- randrproto-1.5.0

* Wed Apr 01 2015 Dave Airlie <airlied@redhat.com> 7.7-13
- randrproto-1.4.1

* Thu Jun 12 2014 Hans de Goede <hdegoede@redhat.com> - 7.7-12
- inputproto-2.3.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Hans de Goede <hdegoede@redhat.com> - 7.7-10
- fontsproto-2.1.3
- videoproto-2.3.2
- xextproto-7.3.0
- xproto-7.0.26
- Cherry pick some unreleased fixes from upstream git

* Thu Jan 23 2014 Adam Jackson <ajax@redhat.com> 7.7-9
- Backport pointer-to-void* changes

* Tue Dec 10 2013 Adam Jackson <ajax@redhat.com> 7.7-8
- glproto 1.4.17

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> 7.7-7
- presentproto 1.0
- dri3proto 1.0
- xextproto 7.2.99.901

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-5
- xproto 7.0.24

* Thu Mar 07 2013 Dave Airlie <airlied@redhat.com> 7.7-4
- autoreconf for aarch64

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> 7.7-3
- inputproto 2.3

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Adam Jackson <ajax@redhat.com> 7.7-1
- inputproto 2.2.99.1

* Thu Jul 26 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.6-24
- bigregsproto 1.1.2
- compositeproto 0.4.2
- damageproto 1.2.1
- fontsproto 2.1.2
- inputproto 2.2
- kbproto 1.0.6
- recordproto 1.14.2
- scrnsaverproto 1.2.2
- xcmiscproto 1.2.2
- xextproto 7.2.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Dave Airlie <airlied@redhat.com> 7.6-22
- glproto 1.4.16
- dri2proto 2.8
- randrproto 1.4.0

* Fri Mar 16 2012 Adam Jackson <ajax@redhat.com> 7.6-21
- xproto 7.0.23

* Wed Feb 15 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.6-20
- inputproto 2.1.99.6

* Thu Jan 26 2012 Dave Airlie <airlied@redhat.com> 7.6-19
- glproto 1.4.15

* Mon Jan 09 2012 Peter Hutterer <peter.hutterer@redhat.com> 7.6-18
- inputproto 2.1.99.5

* Wed Dec 21 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-17
- inputproto 2.1.99.4

* Fri Dec 16 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-16
- inputproto 2.1

* Wed Nov 09 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-15
- Err, that should have been inputproto 2.0.99.1

* Wed Nov 09 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-14
- inputproto 2.1.99.1

* Wed Sep 21 2011 Adam Jackson <ajax@redhat.com> 7.6-13
- Build --without-xmlto

* Thu Jun 30 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-12
- glproto 1.4.14
- dri2proto 2.6

* Thu Jun 23 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-11
- xproto 7.0.22

* Wed Jun 08 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-10
- inputproto 2.0.2

* Mon May 30 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-9
- resourceproto 1.2.0

* Wed Mar 23 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-8
- xproto 7.0.21
- 0001-Add-XF86XK_TouchpadOn-Off.patch: drop, 5d3428de974d
- 0001-Add-defines-for-Unicode-Sinhala-to-keysymdef.h.patch: drop,
  423f5faddbb1023d

* Wed Mar 16 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-7
- 0001-Add-defines-for-Unicode-Sinhala-to-keysymdef.h.patch: add defines for
  Unicode Sinhala

* Tue Mar 15 2011 Adam Jackson <ajax@redhat.com> 7.6-6
- fixesproto 5.0
- Drop libXxf86dga Conflicts, not relevant since at least F12.

* Mon Feb 28 2011 Adam Jackson <ajax@redhat.com> 7.6-5
- 0001-fixesproto-v5-Pointer-barriers.patch: from git.

* Mon Feb 28 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-4
- xextproto 7.2.0

* Thu Feb 24 2011 Peter Hutterer <peter.hutterer@redhat.com> 7.6-3
- xextproto and randrproto git snapshots, needed by server.

* Thu Feb 24 2011 Peter Hutterer <peter.hutterer@redhat.com>
- Add make-git-snapshot script to snapshot protocol releases.

* Thu Feb 24 2011 Peter Hutterer <peter.hutterer@redhat.com>
- update source addresses: www.x.org is 301 Moved Permanently, moved to
  xorg.freedesktop.org.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Adam Jackson <ajax@redhat.com> 7.6-1
- dmxproto 2.3.1
- evieext 1.1.1
- xf86driproto 2.1.1
- xf86vidmodeproto 2.3.1
- xineramaproto 1.2.1

* Thu Nov 25 2010 Bastien Nocera <bnocera@redhat.com> 7.5-4
- Add XF86XK_TouchpadOn/Off keysyms

* Fri Nov 12 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.5-3
- inputproto 2.0.1

* Thu Nov 04 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.5-2
- xproto 7.0.19

* Mon Nov 01 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.5-1
- randrproto 1.3.2
- recordproto 1.14.1
- scrnsaverproto 1.2.1
- xcmiscproto 1.2.1

* Thu Aug 12 2010 Peter Hutterer <peter.hutterer@redhat.com> 7.4-39
- glproto-1.4.12
- kbproto 1.0.5
- renderproto 0.11.1
- videoproto 2.3.1
- xextproto 7.1.2
- xproto 7.0.18

* Wed Aug 04 2010 Adam Jackson <ajax@redhat.com> 7.4-38
- glproto-1.4.11-hyperpipe.patch: Fix conflict with glxext.h

* Wed May 19 2010 Adam Jackson <ajax@redhat.com> 7.4-37
- xproto 7.0.17

* Thu Feb 25 2010 Adam Jackson <ajax@redhat.com> 7.4-36
- dri2proto 2.3

* Sat Jan 16 2010 Dave Airlie <airlied@redhat.com> 7.4-35
- dri2proto 2.2
- glproto 1.4.11

* Tue Oct 13 2009 Adam Jackson <ajax@redhat.com> 7.4-34
- kbproto 1.0.4
- xf86miscproto 0.9.3
- xproxymanagementprotocol 1.0.3

* Tue Oct 06 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-33
- Upload xf86dgaproto 2.1 tarball, this time for real.

* Tue Oct 06 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-32
- compositeproto 0.4.1
- xf86dgaproto 2.1
- dmxproto 2.3
- inputproto 2.0
- fixesproto 4.1.1
- randrproto 1.3.1
- recordproto 1.14
- xf86vidmodeproto 2.3
- xineramaproto 1.2
- xproto 7.0.16

* Fri Aug 28 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-31
- bigreqsproto 1.1.0
- damageproto 1.2.0
- dmxproto 2.2.99.1
- evieext 1.1.0
- fontsproto 2.1.0
- resourceproto 1.1.0
- scrnsaverproto 1.2.0
- videoproto 2.3.0
- xcmiscproto 1.2.0
- xf86bigfontproto 1.2.0
- xf86dgaproto 2.0.99.1
- xf86driproto 2.1.0
- xf86vidmodeproto 2.2.99.1
- xineramaproto 1.1.99.1

* Tue Aug 25 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-30
- recordproto 1.13.99.1
- xextproto 7.1.1

* Tue Aug 25 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-29
- inputproto 1.9.99.902

* Thu Aug 06 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-28
- xextproto 7.1.0

* Wed Jul 29 2009 Kristian Høgsberg <krh@redhat.com> - 7.4-27
- Add patch for DRI2 page flipping.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 7.4-25
- fixesproto 4.1

* Wed Jul 22 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-24
- xextproto 7.0.99.3

* Wed Jul 22 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-23
- xextproto 7.0.99.2
- inputproto 1.9.99.15

* Tue Jul 21 2009 Adam Jackson <ajax@redhat.com> 7.4-22
- xextproto 7.0.99.1
- fixesproto snapshot

* Thu Jul 16 2009 Adam Jackson <ajax@redhat.com> 7.4-21
- randrproto 1.3.0

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> 7.4-20
- Clean up %%install slightly.

* Wed Jul 15 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-19
- renderproto 0.11
- inputproto 1.9.99.14

* Sun Jul 12 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-18
- inputproto 1.9.99.13

* Thu Jun 18 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-17
- inputproto 1.9.99.12

* Thu Jun 18 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-16
- dri2proto 2.1

* Tue May 26 2009 Adam Jackson <ajax@redhat.com> 7.4-15
- glproto 1.4.10

* Tue Mar 03 2009 Peter Hutterer <peter.hutterer@redhat.com> 7.4-14
- xproto 7.0.15
- Purge x11proto-7.0.14-XF86XK_Suspend.patch.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Dave Airlie <airlied@redhat.com> 7.4-12
- update dri2proto

* Thu Dec 18 2008 Adam Jackson <ajax@redhat.com> 7.4-11
- bootstrap build for a moment so xcb changes can happen

* Thu Dec 18 2008 Peter Hutterer <peter.hutterer@redhat.com> 7.4-10
- xextproto 7.0.4

* Tue Dec 16 2008 Adam Jackson <ajax@redhat.com> 7.4-9
- randrproto 1.2.99.3

* Wed Dec 03 2008 Adam Jackson <ajax@redhat.com> 7.4-8
- inputproto 1.5.0

* Thu Nov 20 2008 Adam Jackson <ajax@redhat.com> 7.4-7
- Fix (delete) dri2proto URL.

* Tue Nov 18 2008 Peter Hutterer <peter.hutterer@redhat.com> 7.4-5
- x11proto-7.0.14-XF86XK_Suspend.patch: add XF86XK_Suspend and
  XF86XK_Hibernate to keysyms.

* Mon Nov 10 2008 Adam Jackson <ajax@redhat.com> 7.4-5
- Drop explicit virtual Provides, we get them for free from pkgconfig
- Drop some ancient upgrade Prov/Req/Obs

* Thu Oct 23 2008 Peter Hutterer <peter.hutterer@redhat.com> 7.4-4
- xproto 7.0.14

* Fri Aug 29 2008 Adam Jackson <ajax@redhat.com> 7.4-3
- inputproto 1.4.4

* Thu Aug 28 2008 Kristian Høgsberg <krh@redhat.com> - 7.4-2
- dri2proto 1.99.1

* Sun Jul 20 2008 Adam Jackson <ajax@redhat.com> 7.4-1
- Magic superstition version number bump.
- Dropped: fontcacheproto, trapproto, xf86rushproto
- Updated: randrproto 1.2.2

* Tue Jun 10 2008 Adam Jackson <ajax@redhat.com> 7.3-13
- xproto 7.0.13
- xextproto 7.0.3

* Mon Apr 07 2008 Adam Jackson <ajax@redhat.com> 7.3-12
- dri2proto 1.1.0

* Tue Apr 01 2008 Adam Jackson <ajax@redhat.com> 7.3-11
- inputproto-1.4.3-card32-sucks.patch: Unbreak qt build.  (#436703)

* Tue Apr  1 2008 Kristian Høgsberg <krh@redhat.com> - 7.3-10
- Update to xf86driproto 2.0.4.

* Mon Mar 31 2008 Kristian Høgsberg <krh@redhat.com> 7.3-9
- Add dri2proto.

* Wed Mar 05 2008 Adam Jackson <ajax@redhat.com> 7.3-8
- inputproto 1.4.3
- xproto 7.0.12

* Tue Nov 13 2007 Adam Jackson <ajax@redhat.com> 7.3-7
- inputproto-1.4.2-card32.patch: Make sure CARD32 is defined on lp64.

* Mon Nov 12 2007 Adam Jackson <ajax@redhat.com> 7.3-6
- renderproto 0.9.3

* Fri Nov  9 2007 Kristian Høgsberg <krh@redhat.com> - 7.3-5
- Bump and rebuild.

* Thu Oct 25 2007 Kristian Høgsberg <krh@redhat.com> 7.3-4
- Pull in new glproto to get proto structs for GLX_SGIX_pbuffer.

* Thu Oct 11 2007 Adam Jackson <ajax@redhat.com> 7.3-3
- BuildArch: noarch

* Thu Oct 11 2007 Adam Jackson <ajax@redhat.com> 7.3-3
- BuildArch: noarch

* Thu Sep 27 2007 Adam Jackson <ajax@redhat.com> 7.3-2
- Require libXau-devel when not doing arch bootstrap (#207391)

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 7.3-1
- dgaproto 2.0.3
- Bump to 7.3

* Wed Aug 29 2007 Adam Jackson <ajax@redhat.com> 7.2-13
- Remove the horrible header hack, in favor of proper fix in xserver itself.

* Tue Jul 24 2007 Adam Jackson <ajax@redhat.com> 7.2-12
- Remove dri_interface.h.  It's not protocol, it belongs in Mesa.

* Wed Jul 11 2007 Adam Jackson <ajax@redhat.com> 7.2-11
- compositeproto 0.4

* Wed Jul 11 2007 Adam Jackson <ajax@redhat.com> 7.2-10
- inputproto-1.4.2-horrible-header-hack.patch: Re-add some #defines from
  older inputproto to make old drivers build.  Do not commit this patch
  upstream.

* Thu Apr 26 2007 Adam Jackson <ajax@redhat.com> 7.2-9
- inputproto 1.4.2

* Thu Apr 05 2007 Adam Jackson <ajax@redhat.com> 7.2-8
- Add virtual provides for the subprotocols (#231156)

* Mon Apr 02 2007 Adam Jackson <ajax@redhat.com> 7.2-7
- inputproto 1.4.1

* Mon Mar 12 2007 Adam Jackson <ajax@redhat.com> 7.2-6
- Fix doc macros as per package review (#226641)

* Wed Feb 28 2007 Adam Jackson <ajax@redhat.com> 7.2-5
- Package review cleanups (#226641)

* Wed Feb 28 2007 Adam Jackson <ajax@redhat.com> 7.2-4
- Appease RPM. (#229336)

* Fri Feb 23 2007 Adam Jackson <ajax@redhat.com> 7.2-3
- damageproto 1.1.0

* Mon Feb 19 2007 Adam Jackson <ajax@redhat.com> 7.2-2
- randrproto 1.2.1

* Mon Feb 12 2007 Adam Jackson <ajax@redhat.com> 7.2-1
- randrproto 1.2
- Superstition bump to 7.2

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 7.1-11
- xproto 7.0.10

* Tue Oct 3 2006 Adam Jackson <ajackson@redhat.com> 7.1-10
- Install just enough LBX headers to make libXext build. (#203815)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 7.1-9
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Kristian Høgsberg <krh@redhat.com> - 7.1-8.fc6
- Update to 1.4.8 to get the finaly update of GLX_EXT_tfp opcodes.

* Fri Sep  8 2006 Soren Sandmann <sandmann@redhat.com> 7.1-7.fc6
- Remove printproto source. Rest of 175350.

* Thu Aug 17 2006 Soren Sandmann <sandmann@redhat.com> 7.1-6.fc6
- Don't install xprint headers, as they are being moved to the libXp 
  package instead. Bug 175350.

* Thu Jul 27 2006 Mike A. Harris <mharris@redhat.com> 7.1-5.fc6
- Don't install LBX protocol headers, as LBX is obsoleted in the 7.1 release
  and no longer supported.

* Fri Jul 21 2006 Adam Jackson <ajackson@redhat.com> 7.1-4
- Use dist tag.  Update to kbproto-1.0.3.

* Thu Jul 13 2006 Kristian Høgsberg <krh@redhat.com> 7.1-3
- Tag as 7.1-3.fc5.aiglx.

* Thu Jul 13 2006 Kristian Høgsberg <krh@redhat.com> 7.1-3
- Add dist tag.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 7.1-2.1
- rebuild

* Wed Jun 21 2006 Mike A. Harris <mharris@redhat.com> 7.1-2
- Update to xproto 7.0.7 for X11R7.1
- Use "make install" instead of makeinstall macro.

* Thu May 25 2006 Mike A. Harris <mharris@redhat.com> 7.1-1
- Bump package version-release to 7.1-1 for X.Org X11R7.1 release.

* Fri May 12 2006 Adam Jackson <ajackson@redhat.com> 7.0-13
- Update to glproto 1.4.7 for final EXT_tfp defines

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 7.0-12
- Update to xproto 7.0.5 for misc fixes

* Fri Apr 07 2006 Adam Jackson <ajackson@redhat.com> 7.0-10
- Update to compositeproto-0.3.1 to fix big-endian LP64.

* Sat Apr 01 2006 Adam Jackson <ajackson@redhat.com> 7.0-9
- Update to scrnsaverproto-1.1

* Mon Mar 20 2006 Adam Jackson <ajackson@redhat.com> 7.0-8
- Fix the base URL.

* Wed Mar 15 2006 Adam Jackson <ajackson@redhat.com> 7.0-7
- Update to fixesproto-4.0, compositeproto-0.3, and glproto-1.4.6

* Wed Mar 01 2006 Mike A. Harris <mharris@redhat.com> 7.0-6
- Update to glproto-1.4.5
- Remove xorg-x11-proto-devel-7.0-buffer-values.patch which is in 1.4.5.

* Wed Feb 22 2006 Jeremy Katz <katzj@redhat.com> 7.0-5
- require mesa-libGL-devel since it's needed by some of the headers

* Sun Feb 19 2006 Ray Strode <rstrode@redhat.com> 7.0-4
- Add back part of glproto-texture-from-drawable patch that didn't
  get integrated for some reason

* Thu Feb 16 2006 Mike A. Harris <mharris@redhat.com> 7.0-3
- Update to glproto-1.4.4
- Drop glproto-texture-from-drawable patch, which is integrated now.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 7.0-2.3
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 7.0-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 27 2006 Kristian Høgsberg <krh@redhat.com> 7.0-2
- Add glproto-texture-from-drawable.patch to add opcodes and tokens
  for GLX_texture_from_drawable extension.

* Fri Dec 23 2005 Mike A. Harris <mharris@redhat.com> 7.0-1
- Update to damageproto-1.0.3, glproto-1.4.3, xf86driproto-2.0.2 from the
  X11R7.0 final release.
- Bump package version to 7.0 to match the X11R7 version, for no particularly
  strong reason other than "it feels good".

* Thu Dec 15 2005 Mike A. Harris <mharris@redhat.com> 0.99.4-1
- Update all proto tarballs to the RC4 release.

* Wed Dec 07 2005 Mike A. Harris <mharris@redhat.com> 0.99.3-1
- Update to printproto-1.0.2, trapproto-3.4.2, xproto-7.0.3 from the
  X11R7 RC3 release.

* Mon Nov 21 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-1" to attempt to
  workaround bug( #173384).

* Thu Nov 17 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-2
- Change Conflicts to "Obsoletes: XFree86-devel, xorg-x11-devel"

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Update to X11R7 RC2 release, picking up new xproto-7.0.2.

* Thu Oct 20 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2
- This package contains only C header files and pkg-config *.pc files,
  and does not contain any ELF binaries or DSOs, so we disable debuginfo
  generation.

* Thu Oct 20 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Update all tarballs to X11R7 RC1 release.
- Remove panoramixproto, as it is now known as xineramaproto.
- Remove glu.h and glx.h from file manifest, as they're provided by Mesa.
- Added {_includedir}/GL/internal/dri_interface.h to file manifest.

* Sun Oct 02 2005 Mike A. Harris <mharris@redhat.com> 0.0.1-3
- Use Fedora-Extras style BuildRoot
- Invoke make with _smp_mflags
- Add full URLs to SourceN lines

* Mon Sep 12 2005 Kristian Høgsberg <krh@redhat.com> 0.0.1-2
- Update to 20050912 cvs snapshot of kbproto.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.0.1-1
- Changed for loop in build section to use "ls -1" instead of find "*proto*"
  when going through protocol dirs, as "evieext" just *HAD* to be named
  something completely different from everything else, in true X.Org
  inconsistency fashion.
- Added Conflicts with XFree86-devel and xorg-x11-devel.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.0.1-0
- Initial build of xproto from X.Org modular CVS checkout and "make dist".
- Since there are no upstream tarballs yet, and "make dist" generates
  a "7.0" non-beta final version, I changed the version to 0.0 as I've no
  idea what the intention is and want to avoid using Epoch later.
