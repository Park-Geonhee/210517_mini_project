<?php
	$con = mysqli_connect("localhost","Park","4415","mini_pro") or die("MySQL 접속 실패");
	
	$f_id = $_POST["f_id"];
	$f_name = $_POST["f_name"];
	$f_location = $_POST["f_location"];
	$f_adm = $_POST["f_adm"];
	$f_check = $_POST["f_check"];
	$f_stock_all = $_POST["f_stock_all"];
	
	$sql = "update smart_fac set f_name='".$f_name."',f_location='".$f_location."',f_adm='";
	$sql = $sql.$f_adm."',f_check='".$f_check."',f_stock_all=".$f_stock_all." where f_id = '".$f_id."'";
	
	$ret = mysqli_query($con,$sql);
		
	echo "<h1> 데이터 수정 결과 </h1>";
	if($ret){
		echo " 데이터 수정 완료";
	}
	else{
		echo "수정 실패"."<br>";
		echo "실패 원인 :".mysqli_error($con);
	}
	mysqli_close($con);
	
	echo"<br><br> <a href='main.html'> <--초기 화면</a> ";


?>
