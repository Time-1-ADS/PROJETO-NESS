function escolherDestinatario() {
    var popup = document.getElementById("popup")
    var assunto = assuntoFunc()
    var cumprimentos = cumprimentosFunc()
    var mensagem = mensagemFunc()
    var remetente = remetenteFunc()

    var emails = document.querySelectorAll("a#emailClinica")
    emails.forEach((e)=>{
        e.href += "?subject="+assunto+"&body="+cumprimentos+"%0D%0A%0D%0A"+mensagem+"%0D%0A%0D%0AAtenciosamente,%0D%0A"+remetente+"%0D%0A%0D%0A"
    })
    console.log(emails)
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
function cumprimentosFunc() {
    var cumprimentos = document.getElementById("cumprimentos").value
    return cumprimentos
}
function remetenteFunc() {
    var remetente = document.getElementById("remetente").value
    return remetente
}
function cancelarEnvio() {
    document.getElementById("assunto").value = ""
    document.getElementById("mensagem").value = ""
    document.getElementById("cumprimentos").value = ""
    document.getElementById("remetente").value = ""
    document.getElementById("popup").className = "hidden"
}
function email() {
    document.getElementById("popup").className = "popup-background"
}
function atualiza(){
    document.location.reload(true)
    console.log("ae")
}
