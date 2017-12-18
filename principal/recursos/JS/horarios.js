function validarHora(){
  // alert('Hola');
  var lunes = document.getElementById('lunes');
  var luneshora = document.getElementById('idhoralunes');

  var martes = document.getElementById('martes');
  var marteshora = document.getElementById('idhoramartes');

  var miercoles = document.getElementById('miercoles');
  var miercoleshora = document.getElementById('idhoramiercoles');

  var jueves = document.getElementById('jueves');
  var jueveshora = document.getElementById('idhorajueves');

  var viernes = document.getElementById('viernes');
  var vierneshora = document.getElementById('idhoraviernes');

  var sabado = document.getElementById('sabado');
  var sabadohora = document.getElementById('idhorasabado');

if (lunes.checked==true) {
  luneshora.style.display='block';
}else {
  luneshora.style.display='none'
}

if (martes.checked==true) {
  marteshora.style.display='block';
}else {
  marteshora.style.display='none'
}

if (miercoles.checked==true) {
  miercoleshora.style.display='block';
}else {
  miercoleshora.style.display='none'
}

if (jueves.checked==true) {
  jueveshora.style.display='block';
}else {
  jueveshora.style.display='none'
}

if (viernes.checked==true) {
  vierneshora.style.display='block';
}else {
  vierneshora.style.display='none'
}

if (sabado.checked==true) {
  sabadohora.style.display='block';
}else {
  sabadohora.style.display='none'
}


}
