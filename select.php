 <?php
 
	$con = mysqli_connect("localhost","Park","4415","mini_pro") or die("MySQL 접속 실패");
	
	$sql = "select * from smart_fac";
	
	$ret = mysqli_query($con,$sql);
	if($ret){
		$count = mysqli_num_rows($ret);
	}
	else{
		echo "데이터 조회 실패"."<br><br>";
		echo "실패 원인 :".mysqli_error($con);
		exit();
	}
	
	echo"<h1>공장 조회 결과</h1>";
	echo"<table border=1>";
	echo "<TR>";
	echo "<TH>공장번호</TH><TH>공장이름</TH><TH>공장위치</TH><TH>공장관리자</TH>";
	echo "<TH>점검일</TH><TH>재고량</TH><TH>수정</TH><TH>삭제</TH>";
	echo "</TR>";
	
	while($row = mysqli_fetch_array($ret)){
		echo "<TR>";
		echo "<TD>", $row['f_id'],"</TD>";
		echo "<TD>", $row['f_name'],"</TD>";
		echo "<TD>", $row['f_location'],"</TD>";
		echo "<TD>", $row['f_adm'],"</TD>";
		echo "<TD>", $row['f_check'],"</TD>";
		echo "<TD>", $row['f_stock_all'],"</TD>";
		echo "<TD>","<a href='update.php?f_id=",$row['f_id'], "'>수정</a></TD>";
		echo "<TD>","<a href='delete.php?f_id=",$row['f_id'], "'>삭제</a></TD>";
		echo "</TR>";
	}
	
	mysqli_close($con);
	echo "</TABLE>";
	echo "<br> <a href='main.html'> <--초기 화면</a>";
 ?>