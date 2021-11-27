function escolherDestinatario() {
    var popup = document.getElementById("popup")
    var a = assuntoFunc()
    var m = mensagemFunc()
    document.getElementById("emailClinica").href += "?subject="+a+"&amp;body="+m
    popup.className = "hidden"
}

function assuntoFunc() {
    var assunto = document.getElementById("assunto").value
    return assunto
}
function mensagemFunc() {
    var mensagem = document.getElementById("mensagem").value
    return mensagem
}
function cancelarEnvio() {
    document.getElementById("assunto").value = ""
    document.getElementById("mensagem").value = ""
    document.getElementById("popup").className = "hidden"
}
function email() {
    document.getElementById("popup").className = "popup-background"
}
function atualiza(){
    document.location.reload(true)
    console.log("ae")
}
