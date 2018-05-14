<?php
/*
This is a simple script useful for searching various functions if anyone of then is not disabled then there is a chance it can be used to bypass php hardening and obtain reverse shells.
*/
print("This script checks for disabled functions\n");
// some code shamelessly copied from reverse_php metasploit exploit
$dis=@ini_get('disable_functions');
if(!empty($dis)){
	$dis=preg_replace('/[, ]+/', ',', $dis);
	$dis=explode(',', $dis);
	$dis=array_map('trim', $dis);
}else{
	$dis=array();
}

$call_array=array(
	array('exec','exec works'),
	array('shell_exec','shell_exec works'),
	array('passthru','passthru works'),
	array('proc_open','proc_open works'),
	array('popen','popen works'),
	array('system','system works'),
	array('fsockopen','no exec function works but fsockopen is allowed'),
	array('putenv','putenv works check if mail or simmilar function works then you can still get code exec')
);
$chk=1;
foreach ($call_array as $arr){
	if(is_callable($arr[0]) and !in_array($arr[0],$dis) and $chk ){
        print($arr[1] . "\n");
        $chk=0;
      }
}