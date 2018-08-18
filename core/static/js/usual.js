var id = 0;
var array = new Array();
var CSRF_TOKEN = getCookie('csrftoken');

// Retorno de um cookie válido.
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function showCoords(event) {
      var posicaoX = event.clientX;
      var posicaoY = event.clientY;
      /*
      *Nas três linhas seguintes pego a posição da DIV e faço a subtração da posição do mouse menos
      * a posição da DIV
      */
      posiçãoReal = $("#testediv").offset();
      var localx = posicaoX - posiçãoReal.left;
      var localy = posicaoY - posiçãoReal.top;
      /*
      *Atribuo as variáveis com a posição;
      */
      var coordsx = localx + "px;";
      var coordsy = localy + "px;";
      var posx = ('X: ' + coordsx);
      var posy = ('y: ' + coordsy);
      //document.getElementById("pox").innerHTML = posx;
      //document.getElementById("poy").innerHTML = posy;
}
//objetivo desejado: clicar e printar a posição do click

function whichElement(event) {
      var poscaoX = event.clientX;
      var poscaoY = event.clientY + (window.pageYOffset || document.documentElement.scrollTop);
      //alert("X= " + poscaoX + "y=" + poscaoY);
      array.push(id + ',' + poscaoX + ',' + poscaoY);

      var newImage = document.createElement('img');
      newImage.style.position = 'absolute';
      newImage.style.top = poscaoY + 'px';
      newImage.style.left = poscaoX + 'px';
      newImage.style.width = '2%';
      newImage.src = '/static/images/lamps/lamp.png';
      newImage.id = "lamp" + id;
      document.body.appendChild(newImage);
      id = parseInt(array[id].split(' ')[0]) + 1;
}

function addLamp() {
        var idSecao = document.getElementById('idSecao').value;
        var urlToPost = "/lampada/add/" + idSecao;
        $.post(urlToPost, {
            'lampadas': array,
            'csrfmiddlewaretoken': CSRF_TOKEN
            }
        )
        .done(function() {
            window.location='/endereco/secao/' + idSecao;
        });
}
