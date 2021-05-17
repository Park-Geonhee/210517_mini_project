 <?php
	$con = mysqli_connect("localhost","Park","4415","mini_pro") or die("MySQL 접속 실패");
	
	$f_id = $_POST["f_id"];
	$f_name = $_POST["f_name"];
	$f_location = $_POST["f_location"];
	$f_adm = $_POST["f_adm"];
	$f_check = $_POST["f_check"];
	$f_stock_all = $_POST["f_stock_all"];

	$sql = "INSERT INTO smart_fac VALUES('".$f_id."','".$f_name."','".$f_location."','".$f_adm."','".$f_check."',".$f_stock_all.")";

	$ret = mysqli_query($con, $sql);
	
	echo "<h1> 신규 등록 처리 결과 </h1>";
	if($ret){
		echo "데이터가 입력되었습니다";
	}
	else{
		echo "데이터 입력 실패"."<br>";
		echo "실패 원인 :".mysqli_error($con);
	}
	mysqli_close($con);
	
	echo "<br> <a href='main.html'> <--초기 화면</a>";
?>