var listaNomeProposta = [];
var listaDataProposta = [];
var listaValorProposta = [];

function adicionarPipelineNoKanban() {

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
    var prioridade = "prioridade--alta"
  } else if (radioPrioridade[1].checked){
    var prioridade = "prioridade--media"
  } else if (radioPrioridade[2].checked){
    var prioridade = "prioridade--baixa"
  }
  console.log(prioridade)
  
  var bloco = document.getElementById(colunaSelecionada);

  var nomeProposta = document.getElementById("nomeDaProposta").value;
  var dataProposta = document.getElementById("dataDaProposta").value;
  var valorProposta = document.getElementById("valorDaProposta").value;

  listaNomeProposta.push(nomeProposta);
  listaDataProposta.push(dataProposta);
  listaValorProposta.push(valorProposta);
  for (var i = (listaNomeProposta.length)-1; i < listaNomeProposta.length; i++) {
    bloco.innerHTML +=
      "<div class='card-pipeline " + prioridade + "'><strong>" +
      listaNomeProposta[i] +
      "</strong><br>Data da proposta: " +
      listaDataProposta[i] +
      "<br>R$ " +
      listaValorProposta[i] +
      "</div>";
  }

  document.getElementById("nomeDaProposta").value = "";
  document.getElementById("dataDaProposta").value = "";
  document.getElementById("valorDaProposta").value = "";
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
  blocoFormulario.className = "background-formulario formulario--ativado"
}

function cancelarFormulario() {
  var blocoFormulario = document.getElementById("formularioNovaProposta");
  blocoFormulario.className = "background-formulario formulario--oculto"
  var limparFormulario = document.getElementsByTagName("input")
  for (var i=7; i<limparFormulario.length; i++){
    limparFormulario[i].value = ""
  }
  
}