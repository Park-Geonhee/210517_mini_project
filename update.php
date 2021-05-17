 <?php
	$con = mysqli_connect("localhost","Park","4415","mini_pro") or die("MySQL 접속 실패");
	$sql = "select * from smart_fac where f_id = '".$_GET['f_id']."'";
	
	$ret = mysqli_query($con, $sql);
	if($ret){
		$count = mysqli_num_rows($ret);
		if($count==0){
			echo $_GET['f_id']." 아이디의 공장이 없음"."<br>";
			echo "<br> <a href='main.html'> <--초기 화면</a> ";
			exit();
		}
	}
	else{
		echo "데이터 조회 실패"."<br>";
		echo "실패 원인 :".mysqli_error($con);
		echo "<br> <a href='main.html'> <--초기 화면</a> ";
		exit();
	}
	$row = mysqli_fetch_array($ret);
	$f_id = $row['f_id'];
	$f_name = $row["f_name"];
	$f_location = $row["f_location"];
	$f_adm = $row["f_adm"];
	$f_check = $row["f_check"];
	$f_stock_all = $row["f_stock_all"];


?>

<html>
<head>
<META http-equiv="content-type" connect="text/html; charset=utf-8">
</head>
<body>

<h1> 공장 데이터 수정 </h1>
<form method = "post" action = "update_result.php">
	아이디 : <input type = "text" name="f_id" value=<?php echo $f_id ?> readonly><br>
	이름 : <input type = "text" name="f_name" value=<?php echo $f_name ?>> <br>
	위치 : <input type = "text" name="f_location" value=<?php echo $f_location ?>> <br>
	관리자 : <input type = "text" name="f_adm" value=<?php echo $f_adm ?>> <br>
	점검일 : <input type = "text" name="f_check" value=<?php echo $f_check ?>> <br>
	재고량 : <input type = "text" name="f_stock_all" value=<?php echo $f_stock_all ?>> <br>
	<br><br>
	<input type="submit" value="정보 수정">
</form>

</body>


</html>
 