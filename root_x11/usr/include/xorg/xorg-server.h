/* include/xorg-server.h.  Generated from xorg-server.h.in by configure.  */
/* xorg-server.h.in						-*- c -*-
 *
 * This file is the template file for the xorg-server.h file which gets
 * installed as part of the SDK.  The #defines in this file overlap
 * with those from config.h, but only for those options that we want
 * to export to external modules.  Boilerplate autotool #defines such
 * as HAVE_STUFF and PACKAGE_NAME is kept in config.h
 *
 * It is still possible to update config.h.in using autoheader, since
 * autoheader only creates a .h.in file for the first
 * AM_CONFIG_HEADER() line, and thus does not overwrite this file.
 *
 * However, it should be kept in sync with this file.
 */

#ifndef _XORG_SERVER_H_
#define _XORG_SERVER_H_

/* Support BigRequests extension */
#define BIGREQS 1

/* Default font path */
#define COMPILEDDEFAULTFONTPATH "built-ins"

/* Support Composite Extension */
#define COMPOSITE 1

/* Build DPMS extension */
#define DPMSExtension 1

/* Build GLX extension */
/* #undef GLXEXT */

/* Support XDM-AUTH*-1 */
/* #undef HASXDMAUTH */

/* Support SHM */
#define HAS_SHM 1

/* Define to 1 if you have the `ffs' function. */
#define HAVE_FFS 1

/* Define to 1 if you have the `strcasecmp' function. */
#define HAVE_STRCASECMP 1

/* Define to 1 if you have the `strcasestr' function. */
#define HAVE_STRCASESTR 1

/* Define to 1 if you have the `strlcat' function. */
/* #undef HAVE_STRLCAT */

/* Define to 1 if you have the `strlcpy' function. */
/* #undef HAVE_STRLCPY */

/* Define to 1 if you have the `strncasecmp' function. */
#define HAVE_STRNCASECMP 1

/* Define to 1 if you have the `strndup' function. */
#define HAVE_STRNDUP 1

/* Support IPv6 for TCP connections */
/* #undef IPv6 */

/* Support MIT-SHM Extension */
#define MITSHM 1

/* Internal define for Xinerama */
/* #undef PANORAMIX */

/* Support RANDR extension */
#define RANDR 1

/* Support RENDER extension */
#define RENDER 1

/* Support X resource extension */
#define RES 1

/* Support MIT-SCREEN-SAVER extension */
/* #undef SCREENSAVER */

/* Support SHAPE extension */
#define SHAPE 1

/* Define to 1 on systems derived from System V Release 4 */
/* #undef SVR4 */

/* Support TCP socket connections */
#define TCPCONN 1

/* Enable touchscreen support */
/* #undef TOUCHSCREEN */

/* Support tslib touchscreen abstraction library */
/* #undef TSLIB */

/* Support UNIX socket connections */
#define UNIXCONN 1

/* unaligned word accesses behave as expected */
/* #undef WORKING_UNALIGNED_INT */

/* Support XCMisc extension */
#define XCMISC 1

/* Support Xdmcp */
/* #undef XDMCP */

/* Build XFree86 BigFont extension */
/* #undef XF86BIGFONT */

/* Support XFree86 Video Mode extension */
/* #undef XF86VIDMODE */

/* Build XDGA support */
/* #undef XFreeXDGA */

/* Support Xinerama extension */
/* #undef XINERAMA */

/* Support X Input extension */
#define XINPUT 1

/* XKB default rules */
#define XKB_DFLT_RULES "evdev"

/* Support loadable input and output drivers */
/* #undef XLOADABLE */

/* Build DRI extension */
/* #undef XF86DRI */

/* Build DRI2 extension */
#define DRI2 1

/* Build Xorg server */
#define XORGSERVER 1

/* Vendor release */
/* #undef XORG_RELEASE */

/* Current Xorg version */
#define XORG_VERSION_CURRENT (((1) * 10000000) + ((12) * 100000) + ((4) * 1000) + 0)

/* Build Xv Extension */
#define XvExtension 1

/* Build XvMC Extension */
/* #undef XvMCExtension */

/* Support XSync extension */
#define XSYNC 1

/* Support XTest extension */
#define XTEST 1

/* Support Xv Extension */
#define XV 1

/* Vendor name */
#define XVENDORNAME "The X.Org Foundation"

/* BSD-compliant source */
/* #undef _BSD_SOURCE */

/* POSIX-compliant source */
/* #undef _POSIX_SOURCE */

/* X/Open-compliant source */
/* #undef _XOPEN_SOURCE */

/* Vendor web address for support */
#define __VENDORDWEBSUPPORT__ "http://wiki.x.org"

/* Location of configuration file */
#define __XCONFIGFILE__ "xorg.conf"

/* Name of X server */
#define __XSERVERNAME__ "Xorg"

/* Building vgahw module */
/* #undef WITH_VGAHW */

/* System is BSD-like */
/* #undef CSRG_BASED */

/* System has PC console */
/* #undef PCCONS_SUPPORT */

/* System has PCVT console */
/* #undef PCVT_SUPPORT */

/* System has syscons console */
/* #undef SYSCONS_SUPPORT */

/* System has wscons console */
/* #undef WSCONS_SUPPORT */

/* Loadable XFree86 server awesomeness */
#define XFree86LOADER 1

/* Use libpciaccess */
#define XSERVER_LIBPCIACCESS 1

/* X Access Control Extension */
/* #undef XACE */

#ifdef _LP64
#define _XSERVER64 1
#endif

#endif /* _XORG_SERVER_H_ */
