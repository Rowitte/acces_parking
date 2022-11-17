<?php /*

créer grâce à l'aide d'Hugo Mannucci SN2


*/
?>
<?php 

    $connection = mysqli_connect("192.168.12.71","admin","root");
    $db = mysqli_select_db($connection, 'gestion_abonnes');

if(isset($_POST['Ajouter']))
{
    $Nom = $_POST['nom'];
    $Prenom = $_POST['prenom'];
    $Age = $_POST['age'];
    $mail = $_POST['mail'];
    $adresse = $_POST['adresse'];
    $tel = $_POST['tel'];
    //$code = $_POST['code'];
    

    $query = "INSERT INTO `abonnes` (`id_abonne`,`nom`,`prenom`,`age`,`adresse`,`tel`,`mail`/*,`code`*/) VALUES (NULL,'$Nom','$Prenom','$Age','$adresse','$tel','$mail',NULL/*'$code'*/)";
    $query_run = mysqli_query($connection, $query);
    echo $query;
    
    if($query_run)
    {
        echo '<script> alert("Data Saved"); </script>';
        header('Location: select.php');
    }
    else
    {
        echo '<script> alert("Data Not Saved"); </script>';
    }
}
    mysqli_close($connection);
?>