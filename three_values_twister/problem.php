#!/usr/bin/env php
<?php

echo "phpversion: " . phpversion() . "\n";

$rands = array();
$N = 624;

for($i=0;$i<2049;$i++)
	$rands[$i] = mt_rand();

printf("R%d = %d\n", $N+0, $rands[$N+0]);
printf("R%d = %d\n", $N+227, $rands[$N+227]);
printf("R%d = %d\n", $N+454, $rands[$N+454]);
echo "R2048 = ?" . "\n";

$plain_text = "kurenaifCTF{***FILTERED***}";
$key = $rands[2048];
$cipher_text = openssl_encrypt($plain_text, 'AES-128-ECB', $key);
echo "flag = \"" . $cipher_text . "\"\n"

# decrypt
# $plain_text = openssl_decrypt($cipher_text, 'AES-128-ECB', $key);

?>
