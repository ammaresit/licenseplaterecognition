<?php
	
   $username = 'root';
   $password = '';
   $host = '127.0.0.1';
   $db_name = 'licenseplates';
   
   $licenseplate = '';
   $name = '';

   if(isset($_GET['licenseplate'])){

        $licenseplate = $_GET['licenseplate'];
        $name = $_GET['name'];

        $db = mysqli_connect(
          $host,
          $username,
          $password,
          $db_name);

        $result = mysqli_query($db, "
          INSERT INTO licenseplates(licenseplate, name) 
          VALUES('".$licenseplate."', '".$name."')
          ");

        mysqli_close($db);

        print(json_encode(array(
        	'success' => true
        )));
    }
    else{
        print(json_encode(array(
            'success' => false
        )));
    }



?>
