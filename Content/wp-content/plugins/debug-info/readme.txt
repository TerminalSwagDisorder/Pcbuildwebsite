=== Debug Info ===
Contributors: scott.deluzio, ampmode
Tags: database, php, memory, version, wordpress, admin, debug, plugin, theme
Donate link: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5VFWNLX2NQGQN
Requires at least: 3.4.0
Tested up to: 5.8.1
Stable tag: 1.3.10
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html

A plugin to display your server's PHP info and WordPress environment data for debugging purposes.

== Description ==
Debug Info will provide you with information on your current WordPress operating environment. This is a helpful tool for you or a developer to use when trying to identify the root cause of an error, or other issue you may experience.

Debug Info provides the following information:

* WordPress version currently running on the site

* Current/active WordPress theme name, theme version, theme author, and theme URI

* List of active plugins

* PHP version

* MySQL version

* Apache version

* Full phpinfo() server environment information

Thanks to <a href="http://firstsiteguide.com">Ogi Djuraskovic</a> for the Spanish (es_ES) and Serbian (sr_RS) language translations.

== Installation ==
1. Download archive and unzip in wp-content/plugins or install via Plugins - Add New.
2. Activate the plugin through the Plugins menu in WordPress.
3. View debug information under Dashboard > Debug Info.

== Frequently Asked Questions ==
= Will this plugin fix the problems my site is having? =
No, however it may help identify potential issues.

= I don't understand most of the information this plugin produces. =
If you need help fixing a problem, the information this plugin produces is helpful in order to identify compatibility issues between themes and plugins or different WordPress versions. PHP information is provided to help identify any potential server side conflicts.

= I installed the plugin, and it hasn't helped identify the problem. =
This plugin may not identify every problem your site may face.

For example, if your site gets hacked, this plugin will not be able to identify that. However, it will be able to identify if you are using an outdated version of WordPress or a theme, which may indicate potential security holes.

= Can I translate this plugin? =
Sure! Once you have translated it, let me know and I'll be sure to get your translation included in the next update.

== Screenshots ==
1. Debug Info screenshot-1.png

== Changelog ==
= 1.3.10 =
* Updated tested up to version.
* Added Contributors.

= 1.3.9 =
* Updated tested up to version.

= 1.3.8 =
* Moved plugin menu from under Dashboard to under Tools.
* Removed unnecessary links from report page.
* Updated code to better best practices.
* Updated active plugin list to list plugin name, and not the file path.
* Added plugin version number to the list of active plugins.
* Added a link to the plugin URI if available.
* Added translatable strings and updated POT file.

= 1.3.7 =
* Updated readme and contact info.

= 1.3.6 =
* Minor update

= 1.3.5 =
* Minor update

= 1.3.4 =
* Included Spanish and Serbian language translations.
* Updated WordPress compatible up to 3.9.

= 1.3.3 =
* Fixed translation support.

= 1.3.2 =
* Fixed a bug that caused an error when displaying Apache version in some cases.
* Removed PHP memory usage data as this was only returning the amount of memory that is currently being allocated to your PHP script. This may be misleading when attempting to diagnose issues with other scripts.
* Included .pot file for translations.

= 1.3.1 =
* Added a function check to avoid errors if certain functions do not exist in the current operating environment. Simply provides a 'not available' message for the pieces of information that cannot be retrieved, and continues to return as much information as possible.

= 1.3 =
* Included Apache version to system environment data at top. This is redundant as it is also included in phpinfo() below. Provided on top to give non-technical users an easier way to find this information.

= 1.2 =
* Minor fix.

= 1.1 =
* Minor fix.

= 1.0 =
* Initial release.

== Upgrade Notice ==
= 1.3.10 =
* Updated tested up to version.
* Added Contributors.