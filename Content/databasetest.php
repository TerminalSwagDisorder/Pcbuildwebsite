<?php

    require_once('wp-load.php');

    
    $wpdb->get_results( "SELECT * FROM parts.cpu WHERE Socket = 'LGA1200'");
    echo "<pre>";print_r($wpdb);echo "</pre>";

?>