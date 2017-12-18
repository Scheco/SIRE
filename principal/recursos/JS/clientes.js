function validarCliente(){
  var clienteid = document.getElementById('clienteid').value;
  var materialid = document.getElementById('materialid').value;
  var nombre = document.getElementById('nombre').value;
  var apellido_P = document.getElementById('apellido_P').value;
  var apellido_M = document.getElementById('apellido_M').value;
  var domicilio = document.getElementById('domicilio').value;
  var telefono = document.getElementById('domicilio').value;

  if (clienteid.length==0 || materialid.length==0 ||
  nombre.length==0 || apellido_P.length==0 || apellido_M.length==0 ||
domicilio.length==0 || telefono.length==0) {
    alert('Favor de llenar todos los campos');
  }
}
