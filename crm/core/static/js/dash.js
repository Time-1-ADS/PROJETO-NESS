google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {

    //Primeiro Gráfico Superior - Barra
    var coluna1Valor = parseInt(document.getElementById("coluna1").innerText);
    var coluna2Valor = parseInt(document.getElementById("coluna2").innerText);
    var coluna3Valor = parseInt(document.getElementById("coluna3").innerText);
    var coluna4Valor = parseInt(document.getElementById("coluna4").innerText);

    var dataGraficoSuperiorBarra = google.visualization.arrayToDataTable([
        ['Coluna', 'Itens', { role: 'style' }],
        ['Novo', coluna1Valor, 'red'],
        ['Aberto', coluna2Valor, 'blue'],
        ['Pendente', coluna3Valor, 'yellow'],
        ['Fechado', coluna4Valor, 'green' ],
     ]);
    var optionsGraficoSuperiorBarra = {'title':'Qtde de itens por status',
                       'height':300};
    var chartGraficoSuperiorBarra = new google.visualization.ColumnChart(document.getElementById('superior--primeiro-grafico'));
    chartGraficoSuperiorBarra.draw(dataGraficoSuperiorBarra, optionsGraficoSuperiorBarra);


    //Segundo Gráfico Superior - Pizza

    var valornMonitor = parseInt(document.getElementById("nMonitor").innerHTML)
    var valornSensor = parseInt(document.getElementById("nSensor").innerHTML)
    var valornCommand = parseInt(document.getElementById("nCommand").innerHTML)
    var valornEcho = parseInt(document.getElementById("nEcho").innerHTML)
    var valornReport = parseInt(document.getElementById("nReport").innerHTML)
    var valorIara = parseInt(document.getElementById("Iara").innerHTML)

    var dataGraficoSuperiorPizza = google.visualization.arrayToDataTable([
        ['Produtos', '', { role: 'style' }],
        ['nMonitor', valornMonitor, 'red'],
        ['nSensor', valornSensor, 'blue'],
        ['nCommand', valornCommand, 'yellow'],
        ['nEcho', valornEcho, 'green' ],
        ['nReport', valornReport, 'green' ],
        ['Iara', valorIara, 'green' ],
     ]);
    var optionsGraficoSuperiorPizza = {'title':'Primeiro Gráfico Superior',
                       'height':300};
    var chartGraficoSuperiorPizza = new google.visualization.PieChart(document.getElementById('superior--segundo-grafico'));
    chartGraficoSuperiorPizza.draw(dataGraficoSuperiorPizza, optionsGraficoSuperiorPizza);


    //Primeiro Gráfico Inferior - Barra

    var preco1 = parseFloat(document.getElementById("preco1").innerHTML)
    var preco2 = parseFloat(document.getElementById("preco2").innerHTML)
    var preco3 = parseFloat(document.getElementById("preco3").innerHTML)
    var preco4 = parseFloat(document.getElementById("preco4").innerHTML)

    var nome1 = document.getElementById("nomepreco1").innerHTML
    var nome2 = document.getElementById("nomepreco2").innerHTML
    var nome3 = document.getElementById("nomepreco3").innerHTML
    var nome4 = document.getElementById("nomepreco4").innerHTML
    
    var dataGraficoInferiorBarra = google.visualization.arrayToDataTable([
        ['Element', ''],
        [nome4, preco4],            // RGB value
        [nome3, preco3],            // English color name
        [nome2, preco2],
        [nome1, preco1], // CSS-style declaration
     ]);
    var optionsGraficoInferiorBarra = {'title':'Projetos mais valiosos',
                       'height':300};
    var chartGraficoInferiorBarra = new google.visualization.ColumnChart(document.getElementById('inferior--primeiro-grafico'));
    chartGraficoInferiorBarra.draw(dataGraficoInferiorBarra, optionsGraficoInferiorBarra);
    

    //Segundo Gráfico Inferior - Pizza

    var alta = parseInt(document.getElementById("alta").innerHTML)
    var media = parseInt(document.getElementById("media").innerHTML)
    var baixa = parseInt(document.getElementById("baixa").innerHTML)

    var dataGraficoInferiorPizza = google.visualization.arrayToDataTable([
        ['Element', '', { role: 'style' }],
        ['Baixa', baixa, '#000'],
        ['Alta', alta, 'silver'],
        ['Média', media, 'gold'],
     ]);
    var optionsGraficoInferiorPizza = {'title':'Primeiro Gráfico Inferior',
                       'height':300};
    var chartGraficoInferiorPizza = new google.visualization.PieChart(document.getElementById('inferior--segundo-grafico'));
    chartGraficoInferiorPizza.draw(dataGraficoInferiorPizza, optionsGraficoInferiorPizza);
}
