var listaNomeProposta = [];
var listaDataProposta = [];
var listaValorProposta = [];

function novaProposta() {
  var bloco = document.getElementById("propostas");

  var nomeProposta = document.getElementById("nomeProposta").value;
  var dataProposta = document.getElementById("dataProposta").value;
  var valorProposta = document.getElementById("valorProposta").value;

  listaNomeProposta.push(nomeProposta);
  listaDataProposta.push(dataProposta);
  listaValorProposta.push(valorProposta);
  for (var i = (listaNomeProposta.length)-1; i < listaNomeProposta.length; i++) {
    bloco.innerHTML +=
      "<div class='elementoProposta'><strong>" +
      listaNomeProposta[i] +
      "</strong><br>Data da proposta: " +
      listaDataProposta[i] +
      "<br>R$ " +
      listaValorProposta[i] +
      "</div>";
  }
}
