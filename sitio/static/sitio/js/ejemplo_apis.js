function actualizar_contador() {
    $.ajax({url: "/api/cantidad_noticias/"}).done(on_nuevo_valor_contador);
}

function actualizar_recientes() {
    $.ajax({url: "/ajax/noticias_recientes/"}).done(on_nuevas_noticias);
}

function on_nuevo_valor_contador(data) {
    var span_contador = $('#contador-noticias');
    span_contador.html(data.cantidad_noticias);
}

function on_nuevas_noticias(data) {
    var div_noticias_recientes = $('#noticias-recientes');
    div_noticias_recientes.html(data);
}


function inicializar() {
    setInterval(actualizar_contador, 2000);
    setInterval(actualizar_recientes, 2000);
}

$(inicializar);
