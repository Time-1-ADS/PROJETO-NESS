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
                       'width':500,
                       'height':300};
    var chartGraficoSuperiorBarra = new google.visualization.ColumnChart(document.getElementById('superior--primeiro-grafico'));
    chartGraficoSuperiorBarra.draw(dataGraficoSuperiorBarra, optionsGraficoSuperiorBarra);

    //Primeiro Gráfico Inferior - Barra
    
    var dadosDoGrafico = document.getElementById("valorProjetos").innerText

    var dataGraficoInferiorBarra = google.visualization.arrayToDataTable([
        ['Element', ''],
        ['Elemento 1', 8.94],            // RGB value
        ['Elemento 2', 10.49],            // English color name
        ['Elemento 3', 19.30],
        ['Elemento 4', 21.45], // CSS-style declaration
     ]);
    var optionsGraficoInferiorBarra = {'title':'Primeiro Gráfico Inferior',
                       'width':500,
                       'height':300};
    var chartGraficoInferiorBarra = new google.visualization.ColumnChart(document.getElementById('inferior--primeiro-grafico'));
    chartGraficoInferiorBarra.draw(dataGraficoInferiorBarra, optionsGraficoInferiorBarra);

    //Segundo Gráfico Superior - Pizza

    var dataGraficoSuperiorPizza = google.visualization.arrayToDataTable([
        ['Element', '', { role: 'style' }],
        ['Elemento 1', 8.94, 'red'],
        ['Elemento 2', 10.49, 'blue'],
        ['Elemento 3', 19.30, 'yellow'],
        ['Elemento 4', 21.45, 'green' ],
     ]);
    var optionsGraficoSuperiorPizza = {'title':'Primeiro Gráfico Superior',
                       'width':500,
                       'height':300};
    var chartGraficoSuperiorPizza = new google.visualization.PieChart(document.getElementById('superior--segundo-grafico'));
    chartGraficoSuperiorPizza.draw(dataGraficoSuperiorPizza, optionsGraficoSuperiorPizza);
    
    //Segundo Gráfico Inferior - Pizza

    var dataGraficoInferiorPizza = google.visualization.arrayToDataTable([
        ['Element', '', { role: 'style' }],
        ['Elemento 1', 8.94, '#b87333'],
        ['Elemento 2', 10.49, 'silver'],
        ['Elemento 3', 19.30, 'gold'],
        ['Elemento 4', 21.45, 'color: #e5e4e2' ],
     ]);
    var optionsGraficoInferiorPizza = {'title':'Primeiro Gráfico Inferior',
                       'width':500,
                       'height':300};
    var chartGraficoInferiorPizza = new google.visualization.PieChart(document.getElementById('inferior--segundo-grafico'));
    chartGraficoInferiorPizza.draw(dataGraficoInferiorPizza, optionsGraficoInferiorPizza);
}
