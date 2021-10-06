var listaNomeProposta = [];
var listaDataProposta = [];
var listaValorProposta = [];

function novaProposta() {

  var radioColuna = document.getElementsByName("coluna");
  if (radioColuna[0].checked){
    var colunaSelecionada = "novasPropostas"
  } else if (radioColuna[1].checked){
    var colunaSelecionada = "primeiroContato"
  } else if (radioColuna[2].checked){
    var colunaSelecionada = "propostaFechada"
  } else if(radioColuna[3].checked){
    var colunaSelecionada = "projetoEmAndamento"
  }

  var radioPrioridade = document.getElementsByName("prioridade");
  if (radioPrioridade[0].checked){
    var prioridade = "prioridadeAlta"
  } else if (radioPrioridade[1].checked){
    var prioridade = "prioridadeMedia"
  } else if (radioPrioridade[2].checked){
    var prioridade = "prioridadeBaixa"
  }
  console.log(prioridade)
  
  var bloco = document.getElementById(colunaSelecionada);

  var nomeProposta = document.getElementById("nomeProposta").value;
  var dataProposta = document.getElementById("dataProposta").value;
  var valorProposta = document.getElementById("valorProposta").value;

  listaNomeProposta.push(nomeProposta);
  listaDataProposta.push(dataProposta);
  listaValorProposta.push(valorProposta);
  for (var i = (listaNomeProposta.length)-1; i < listaNomeProposta.length; i++) {
    bloco.innerHTML +=
      "<div class='elementoProposta " + prioridade + "'><strong>" +
      listaNomeProposta[i] +
      "</strong><br>Data da proposta: " +
      listaDataProposta[i] +
      "<br>R$ " +
      listaValorProposta[i] +
      "</div>";
  }

  document.getElementById("nomeProposta").value = "";
  document.getElementById("dataProposta").value = "";
  document.getElementById("valorProposta").value = "";
  var limparRadioColuna = document.getElementsByName("coluna");
  for(var i=0;i<limparRadioColuna.length;i++){
    limparRadioColuna[i].checked = false;
  }
  var limparRadioPrioridade = document.getElementsByName("prioridade");
  for(var i=0;i<limparRadioPrioridade.length;i++){
    limparRadioPrioridade[i].checked = false;
  }
}


function formularioNovaProposta(){
  var blocoFormulario = document.getElementById("formularioNovaProposta");
  blocoFormulario.className = "fundo-formulario display-flex"
}

function cancelarFormulario() {
  var blocoFormulario = document.getElementById("formularioNovaProposta");
  blocoFormulario.className = "fundo-formulario display-none"
  var limparFormulario = document.getElementsByTagName("input")
  for (var i=7; i<limparFormulario.length; i++){
    limparFormulario[i].value = ""
  }
  
}