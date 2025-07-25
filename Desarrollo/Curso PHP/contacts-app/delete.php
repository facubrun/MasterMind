<?php

require "database.php";

$id = $_GET["id"];

$stmt = $conn->prepare("SELECT * FROM contacts WHERE id = :id");
$stmt->execute([":id" => $id]);


if (stmt->rowCount() == 0) {
  http_response_code(404);
  echo "HTTP 404 NOT FOUND";
  return;
}

$stmt = $conn->prepare("DELETE FROM contacts WHERE id = :id");
$stmt->execute([":id" => $id]);

header("Location: home.php");