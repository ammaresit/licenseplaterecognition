<?php

	
   $username = 'root';
   $password = '';
   $host = '127.0.0.1';
   $db_name = 'licenseplates';
   $licenseplate = '';

   if(isset($_GET['licenseplate'])){
        $licenseplate = $_GET['licenseplate'];
        $db = mysqli_connect($host, $username, $password, $db_name);
        $result = mysqli_query($db, "
          SELECT * FROM licenseplates 
          WHERE licenseplate='".$licenseplate."'
          ");
        if (mysqli_num_rows($result) > 0) {
  	    	while($row = mysqli_fetch_assoc($result)) {
  		        print(json_encode(array(
  		        	'success' => true,
  		        	'found' => "1",
  	            'licenseplate' => $row["licenseplate"],
  	            'name' => $row["name"]
  	        	)));
  	    	}
		    } else {
    		print(json_encode(array(
		        	'success' => true,
		        	'found' => "0"
	        )));
		    }
        mysqli_close($db);
    }
    else{
        print(json_encode(array(
            'success' => false
        )));
    }



?>
