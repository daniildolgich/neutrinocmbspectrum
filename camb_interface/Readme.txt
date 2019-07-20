This tarball contains a web interface to CAMB.  This interface was developed by
the LAMBDA team; any questions regarding it should be directed to LAMBDA.

Information regarding CAMB can be found at:
http://camb.info/

The data input form HTML page does not define a complete web page.  However, it
does completely define the interface form.  The enclosed CSS file must be
associated with the page for the form to be correctly layed out.  JavaScript is
used to a little data entry verification and to display/hide inputs as different
options are selected; the user's browser must have JavaScript enabled for this
form to work.

The two pivot points affect how the spectra are normalized; these default to values
appropriate for comparing output to WMAP spectra (0.002) instead of the CAMB defaults
(0.05).

*** Requirements:
- A local copy of CAMB.  This interface was originally developed using the April 2005
  release; it has been updated to work with the September 2008 release.
- The form processor was written in Perl, and has been tested using Perl V5.8.2.
- GnuPlot is used to draw plots of some of the results.  It has been tested with
  V3.7.3.
- The CGI module that should come with a standard Perl installation.
- The HEALPix synfast application may be used to create simulated maps from
  the output spectra.
- This application was designed and tested on a Linux operating system.

*** Inventory:
There are four files in this tarball:
- Readme.txt      - This file.
- camb_form.html  - The HTML that defines and lays out the form.
- camb.css        - A Cascading Style Sheet file used by the HTML to layout for
                    contents of the form.
- camb_proc.pl    - The Perl script that processes the form inputs, runs CAMB,
                    and displays the output.  The Results function should be
		    modified to define your own layout.

*** Installation:
0) Download and install CAMB and GnuPlot.
1) Copy the Perl script into your CGI directory.
2) Create a camb directory under the web site's document root directory; create
   and output directory under it.
3) Modify the Perl script to reflect your environment, modifying the constants
   at the head of the file and the Results function to reflect your site layout.
   Ensure that the Perl executable path in the first line points to your 
   Perl implementation.
4) Create a web page for the form, using the camb_form.html file as a starting
   point.  Be sure to include the CSS file in this page's header.

*** Change History
December 2005
-- Initial version.

August 2006
-- Synfast support.

March 2007
-- Default parameters updated.

October 2008
-- Default parameters updated.  Support for the parameters supported by the
   September 2008 version of CAMB.

January 2011
-- Verified to work with the January 2011 version of CAMB.

November 2014
-- Parameters updated to those accepted by the April 2014 version of CAMB.
