<?php
// proxy.php
$query = $_GET['query'] ?? '';
$bingUrl = 'https://www.bing.com/search?q=' . urlencode($query);
$response = file_get_contents($bingUrl);
echo $response;
?>
