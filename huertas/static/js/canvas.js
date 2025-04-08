


function rectangulo(ctx, startX, startY, ancho, largo){
    ctx.beginPath();
 
    ctx.moveTo(startX,startY);
 
    ctx.lineTo(startX+largo,startY);
    ctx.lineTo(startX+largo,startY+ancho);
    ctx.lineTo(startX,startY+ancho);
    ctx.lineTo(startX,startY);
    ctx.closePath();
    ctx.stroke();
}





function ajax(id,urlDatos){
    $.ajax({
        dataType : 'json',
        method : 'POST',
        url : urlDatos,
        data : {
            id : id,
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success : function(data) {
            var cant = [];

            for(var x in data)
            {
                cant.push({
                    
                    indice : x,
                    id : data[x].pk,
                    nombre : data[x].fields['nombre'],
                    posX : data[x].fields['ubicacion_x'],
                    posY : data[x].fields['ubicacion_y'],
                    ancho : data[x].fields['ancho'],
                    largo : data[x].fields['largo']
                });
            }
            console.log(data)
            cache[request.term] = cultivos;
            response(cant);
        }
    });

}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
async function datos(url, datos) {
    try {
      const res = await  fetch(url,{
    
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'same-origin', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
          'Content-Type': 'application/json',
          "X-CSRFToken": getCookie("csrftoken")
        
        },
        body: JSON.stringify(datos)
    });
  
      if (res.status >= 400) {
        console.log(res)
        throw new Error("Bad response from server");
      }
  
      //console.log(res);
      return  res.json();
  
    } catch (err) {
      console.error(err);
    }
  }

function dibujarCanteros(canteros,ctx,aspecto){
  for (var cant in canteros){
    ctx.fillText(canteros[cant].nombre, canteros[cant].ubicacion_x/aspecto,canteros[cant].ubicacion_y/aspecto+canteros[cant].ancho/aspecto+11);
    rectangulo(ctx,canteros[cant].ubicacion_x/aspecto,canteros[cant].ubicacion_y/aspecto,canteros[cant].ancho/aspecto,canteros[cant].largo/aspecto);
    /*for (var sem in canteros[cant].sembrado){
        var dirX = canteros[cant].dirRelX+canteros[cant].sembrado[sem].x;
        var dirY = canteros[cant].dirRelY+canteros[cant].sembrado[sem].y;
        ctx.beginPath();
        ctx.moveTo(dirX,dirY);
        ctx.arc(dirX, dirY, canteros[cant].sembrado[sem].radio,0,2*Math.PI);
        ctx.closePath();
        ctx.stroke();
    }
*/
  }

}

function huerta(x, y, lar, anc, huerta_id, aspecto){
    canvas1 = document.getElementById('myCanvas');
    canvas1.setAttribute('width', 300);
    canvas1.setAttribute('height' , 300);
    var ctx = myCanvas.getContext("2d");
    ctx.fillStyle = "green";
    var largo= lar / aspecto;
    var ancho =  anc/aspecto;
    ctx.font = "bold 12px Arial";
    ctx.strokeStyle ="#1CC";
    ctx.lineCap ="round";
    ctx.lineJoin="round";
    rectangulo(ctx, x/aspecto, y/aspecto, largo,ancho);
    //console.log(huerta_id);
    datos('/configuracion/canteros_listar/',{id: huerta_id})
    .then(data =>{
          cante =data.context;
          dibujarCanteros(cante,ctx,aspecto);
           }
          ) 
     
    
       // ctx.arc(100, 100, 50,0,2*Math.PI);

  }




    

