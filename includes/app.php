<?php

$pyfile = "mainpy.py";

function tojson($a) {
	if($a == array())
		return "{}";
	else
		return json_encode($a);
}

@session_start();


function curpathinfo() {
	if(array_key_exists("PATH_INFO", $_SERVER)) {
		return substr($_SERVER["PATH_INFO"], 1);
	} else
		return "";
}



$pyoutp = shell_exec("python ".$pyfile." '".tojson($_SESSION)."' '".tojson($_GET)."' '".tojson($_POST)."' 'c".curpathinfo()."' 2>&1" );


$pyoutp1 = json_decode( $pyoutp, true );
if($pyoutp1 == null)
	echo str_replace("\n", "<br>", $pyoutp);
else{
	$_SESSION = $pyoutp1["_SESSION"];
	echo $pyoutp1["printout"];
}



?>