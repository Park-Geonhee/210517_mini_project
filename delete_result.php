<?php
	$con = mysqli_connect("localhost","Park","4415","mini_pro") or die("MySQL 접속 실패");
	
	$f_id = $_POST["f_id"];
	
	$sql = "delete from smart_fac where f_id = '".$f_id."'";
	
	$ret = mysqli_query($con,$sql);
		
	echo "<h1> 데이터 삭제 결과 </h1>";
	if($ret){
		echo $f_id." 데이터 삭제 완료";
	}
	else{
		echo "삭제 실패"."<br>";
		echo "실패 원인 :".mysqli_error($con);
	}
	mysqli_close($con);
	
	echo"<br><br> <a href='main.html'> <--초기 화면</a> ";


?>
