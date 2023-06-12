var expr = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;

$(document).ready(function(){
    $("#bEnviar").click(function(){
        var nombre = $("#username").val();
        var correo = $("#email").val();
        var contraseña = $("#password").val();

        if(nombre == ""){
            $("#mensaje1").fadeIn();
            return false;
       
        }
    });
});