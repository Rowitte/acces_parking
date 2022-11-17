<?php
/* connexion bdd a ne pas oublier */
$host = "192.168.12.71"; /* L'adresse du serveur */
$login = "admin"; /* Votre nom d'utilisateur */
$password = "root"; /* Votre mot de passe */
$base = "gestion_abonnes"; /* Le nom de la base */
$dbh = new PDO('mysql:host=192.168.12.71;dbname=gestion_abonnes', $login, $password);
// use the connection here // courbe graph1 information moteur

$sth = $dbh->query('SELECT * FROM capteurs');
// iterate over array by index and by name
$labelsdate='';
$dataco2='';
$datatemperature='';
$datahumidite='';  
while($row = $sth->fetch(PDO::FETCH_ASSOC)) {
    //get the company name separated by comma for chart labels
    $labelsdate.= '"' .$row["date"]. '",';
    //get the total separated by comma for chart data
    $dataco2.= $row["co2"].',';
    $datatemperature.= $row["temperature"].',';
    $datahumidite.= $row["humidite"].',';
}
/*$sth = $dbh->query('SELECT * FROM confort');
// iterate over array by index and by name
$labelsdateConfort='';
$dataClignotant_droit='';
$dataClignotant_gauche='';
$dataFeux_Position='';
$dataFeux_Croisement='';
$dataFeux_Route='';
$dataFeux_Brouillard='';
$dataFeux_Stop='';
$dataWarning='';
$dataCapt_Lumiere='';
while($row = $sth->fetch(PDO::FETCH_ASSOC)) {
    //get the company name separated by comma for chart labels
    $labelsdateConfort.= '"' .$row["DateConfort"]. '",';
    //get the total separated by comma for chart data
    $dataClignotant_droit.= $row["Clignotant_droit"].',';
    $dataClignotant_gauche.= $row["Clignotant_gauche"].',';
    $dataFeux_Position.= $row["Feux_Position"].',';
    $dataFeux_Croisement.= $row["Feux_Croisement"].',';
    $dataFeux_Route.= $row["Feux_Route"].',';
    $dataFeux_Brouillard.= $row["Feux_Brouillard"].',';
    $dataFeux_Stop.= $row["Feux_Stop"].',';
    $dataWarning.= $row["Warning"].',';
    $dataCapt_Lumiere.= $row["Capt_Lumiere"].',';
}*/
?>
<!doctype html>
    <html lang="fr">
        <head>
        <meta charset="utf-8">
        <title>courbe</title>
        <link rel="stylesheet" href="">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js" ></script>
        </head>
    <body>
        <canvas id="graph1"></canvas>
        <script>
            //alert("eurror");
            const ctx = document.getElementById('graph1').getContext('2d');
            const graph1 = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: [<?php echo trim($labelsdate);?>],//'lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche'
                    datasets: [{
                        label: 'co2',
                        data: [<?php echo trim($dataco2);?>],
                        backgroundColor: [ 'rgba(255, 191, 0, 1)', ],
                        borderColor: [ 'rgba(255, 191, 0, 1)', ],
                        yAxisID: 'y',
                    },
                    {
                        label: 'temperature',
                        data: [<?php echo trim($datatemperature);?>],
                        backgroundColor: [ 'rgba(0, 255, 191, 1)', ],
                        borderColor: [ 'rgba(0, 255, 191, 1)', ],
                        yAxisID: 'y1',
                    },
                    {
                        label: 'humidite',
                        data: [<?php echo trim($datahumidite);?>],
                        backgroundColor: [ 'rgba(0, 191, 255, 1)' ,],
                        borderColor: [ 'rgba(0, 191, 255, 1)', ],
                        yAxisID: 'y1',
                    }
                    ]
                },
                options: {
                    responsive: true,
                    interaction: {
                        mode: 'index',
                        intersect: false,
                    },
                    stacked: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Information Moteur'
                        }
                    },
                    scales: {
                        y: {
                            type: 'linear',
                            display: true,
                            position: 'left',
                        },
                        y1: {
                            type: 'linear',
                            display: true,
                            position: 'right',
                        },
                    }
                },
            });
            
        </script>
        
    </body>
    </html>