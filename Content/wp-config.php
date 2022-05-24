<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'J3Om7420kYL <[n$r9r8/5-E)lz^nrDd<VZ^[cXz.yWy6zD_6L[=T|bLnG5<C5;0');
define('SECURE_AUTH_KEY',  'l4ESn:aq3VS!a+ (t|J<51GX=8AydIDaR+,B*m/yle@Dp||II+~tYPx3+{WLyG *');
define('LOGGED_IN_KEY',    'C37u^47$Y|]fx}o+#(H:*u=!S`|/.]%ur~bg{I.Eo7TQx6a{-i0`T|~2CT;7AYL8');
define('NONCE_KEY',        'B|28j2E.jPt^F]Cm6e&sJH7Het0$cG1*+)Sad%O)k2}iv6&eB[ZYr$X9)pbL@Ih6');
define('AUTH_SALT',        'n%{lnJ YWamPhY=FC|N0J2|w]Jdfs-{Q?0z~tH^2Ca.+Jtx/vnzi/%kU*%I:Ru-]');
define('SECURE_AUTH_SALT', '$<Kr/.<eSQzL^J`:.tl#v#1hJ1K_yc^699c%a69@78O[|xsa*dS^aH7|lDCYvUy|');
define('LOGGED_IN_SALT',   'd?#/NmQD1I3#)+x~$+<@8;SXu2ajqd~O_BdtCRJAb9JMj$Y3}JJ*491gM[FW(+~)');
define('NONCE_SALT',       ']wBH{+o+!pBvxp~OuCJ.w3SA*Md&u6/fuCfHL$Wf4X]9LoWGY-Z0t-|8AzKsmb|E');

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', true );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
