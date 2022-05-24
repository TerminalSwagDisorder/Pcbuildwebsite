<script type="text/javascript">
	function showDetails(id) {
		document.getElementById(id).style.display = 'block';
	}
	function hideDetails(id) {
		document.getElementById(id).style.display = 'none';
	}
</script>
<div class="wrap">
	<div class="postbox">
		<h2><?php _e('WordPress Debug Info', 'debug-info'); ?></h2>
		<p><?php _e('Below is some information about your current WordPress and server setup. This information may be useful for your technical support, website developers, and plugin or theme developers who need to diagnose problems on your site.', 'debug-info'); ?></p>
		<p><?php echo debug_info_version_check(); ?></p>
		<p><?php _e('For more detailed PHP server related information, click the Show Details link below.', 'debug-info'); ?></p>
		<a href="#" onclick="showDetails('details'); return false;"><?php _e('Show Details', 'debug-info'); ?></a>
		<a href="#" onclick="hideDetails('details'); return false;"><?php _e('Hide Details', 'debug-info'); ?></a>
		<span id="details" style="display: none;"><?php echo debug_info_get_php_info(); ?></span>
	</div>
	<div class="postbox">
		<p><?php _e('If this plugin has helped you out at all, please consider making a donation to encourage future updates.<br />Your generosity is appreciated!', 'debug-info'); ?></p>
			<a href="#" onclick="window.open('https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5VFWNLX2NQGQN');">
				<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" width="147" height="47">
			</a>
		<?php
			$url	= 'http://wordpress.org/support/plugin/debug-info';
			$link	= sprintf(
				wp_kses(
					__( 'To report any issues with this plugin, please visit the <a href="%s">support page on WordPress.org</a>.', 'debug-info' ),
					array(  'a' => array( 'href' => array() ) )
				),
				esc_url( $url )
			);
		?>
		<p><?php echo $link; ?></p>
	</div>
</div>