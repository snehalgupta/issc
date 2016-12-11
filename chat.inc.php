<?php

// simple chat class
//define('SERVER', 'localhost');
//define('USERNAME', 'root');
//define('PASSWORD', 'password');
//define('DATABASE', 'cms');

//class DB {
    //function __construct(){
        //$connection = mysql_connect(SERVER, USERNAME, PASSWORD) or die('Connection error -> ' . mysql_error());
        //mysql_select_db(DATABASE, $connection) or die('Database error -> ' . mysql_error());
    //}
//}

class SimpleChat {

// DB variables



var $sDbName;

var $sDbUser;

//var $sDbPass;

// constructor

function SimpleChat() {

$connection=mysql_connect("localhost","root") or die('Connection error ->'.mysql_error());

$this->sDbName = 'database_name';
mysql_select_db($this->sDbName,$connection) or die('Database error ->'.mysql_error());


$this->sDbUser = 'root';  //'username';



// $this->current_user=a

// $this->current_password=b

mysql_close($connection);

}

// adding to DB table posted message

function acceptMessages() {

if ($_COOKIE['member_name']) {

if(isset($_POST['s_say']) && $_POST['s_message']) {

$sUsername = $_COOKIE['member_name'];

//the host, name, and password for your mysql

$vLink = mysql_connect("localhost", $this->sDbUser);

//if ($vLink){ echo " $this->sDbUser ";
    //echo "vlink yes" ;}
//else { echo "vlink no";}
//select the database

$s=mysql_select_db($this->sDbName);
//if ($s) { echo "string";}
//else{ echo "not selected database";}

$sMessage = mysql_real_escape_string($_POST['s_message']);

if ($sMessage != '') {

$a=mysql_query("INSERT INTO `s_chat_messages` SET `user`= '$sUsername', `message`='$sMessage', `when`= 'UNIX_TIMESTAMP()'");
//$sql = "INSERT INTO persons (first_name, last_name, email_address) VALUES ('$first_name', '$last_name', '$email_address');
//$a=mysql_query("INSERT INTO s_chat_messages (user,message,when) VALUES ('$sUsername','$sMessage','UNIX_TIMESTAMP()'");
//if(mysqli_query($link, $sql)
//if ($a) { echo "hello your first chat";}
//else {echo "not enabled chaT";}

}

mysql_close($vLink);

}

}

ob_start();

require_once('chat_input.html');

$sShoutboxForm = ob_get_clean();

return $sShoutboxForm;

}

function getMessages() {

$vLink = mysql_connect("localhost", $this->sDbUser);//+ or mysql_connect("localhost", $this->sDbUser);

//select the database

mysql_select_db($this->sDbName);

//returning the last 15 messages

$vRes = mysql_query("SELECT * FROM `s_chat_messages` ORDER BY `id` ASC LIMIT 15");

$sMessages = '';

// collecting list of messages

if ($vRes) {

while($aMessages = mysql_fetch_array($vRes)) {

$sWhen = date("H:i:s", $aMessages['when']);

$sMessages .= '<div class="message">' . $aMessages['user'] . ': ' . $aMessages['message'] . '<span>(' . $sWhen . ')</span></div>';

}

} else {

$sMessages = 'DB error, create SQL table before';

}

mysql_close($vLink);

ob_start();

require_once('chat_begin.html');

echo $sMessages;

require_once('chat_end.html');

return ob_get_clean();

}

}

?>
