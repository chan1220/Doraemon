<?php
// MySQL 데이터베이스 연결
$link = mysqli_connect('localhost', 'root', 'root', 'pidb');
  
// 연결 오류 발생 시 스크립트 종료
if (mysqli_connect_errno()) {
	die('Connect Error: '.mysqli_connect_error());
}

$result_array = array();
$car_id 	= $_POST["car_id"];
$start_time = $_POST["start_time"];
$end_time 	= $_POST["end_time"];
$query ="SELECT * FROM POSITION WHERE CAR_ID='$car_id' and POS_TIME between '$start_time' and '$end_time';";
// 쿼리문 전송
if ($result = mysqli_query($link, $query)) 
{
	// 레코드 출력
	while ($row = mysqli_fetch_object($result))
	{
		$result_array[] = $row;
	}
	//json
	echo json_encode($result_array);
	// 메모리 정리
	mysqli_free_result($result);
}
else
{
	echo "-1";
}
// 접속 종료
mysqli_close($link);

