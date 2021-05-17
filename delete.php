<?php

	$con=mysqli_connect("localhost","Park","4415","mini_pro") or die("MySQL 접속실패");
	$sql = "select * from smart_fac where f_id = '".$_GET['f_id']."'";
	
	$ret = mysqli_query($con,$sql);
	if($ret){
		$count = mysqli_num_rows($ret);
		if($count==0){
			echo $_GET['f_id']." 아이디의 회원이 없음"."<br>";
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


?>

<html>
<head>
<META http-equiv="content-type" connect="text/html; charset=utf-8">
</head>
<body>

<h1> 공장 데이터 삭제 </h1>
<form method = "post" action = "delete_result.php">
	아이디 : <input type = "text" name="f_id" value=<?php echo $f_id ?>
	readonly><br>
	이름 : <input type = "text" name="f_name" value=<?php echo $f_name ?> readonly><br>
	<br><br>
	위 정보를 제거하겠습니까?
	<input type="submit" value="정보 삭제">
</form>

</body>


</html>