function addToCart(id, qte) {
    console.log("function HELLO?")
    let header = new Headers();
    header.append("Content-Type", "application/json");
    let init = {
        credentials: 'same-origin',
        method: 'POST',
        headers: header,
        mode: 'cors',
        body: JSON.stringify({quantity: qte})
    };
    fetch("/cart/"+id, init).then(function(data) {
        console.log("callback?");
    });
}