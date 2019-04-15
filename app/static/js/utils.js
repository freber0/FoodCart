function addToCart(id, qte) {
    let header = new Headers();
    header.append("Content-Type", "application/json");
    let init = {
        credentials: 'same-origin',
        method: 'POST',
        headers: header,
        mode: 'cors',
        body: JSON.stringify({quantity: qte})
    };
    fetch("/cart/"+id, init);
}

function removeFromCart(id) {
    let header = new Headers();
    header.append("Content-Type", "application/json");
    let init = {
        credentials: 'same-origin',
        method: 'DELETE',
        headers: header,
    };
    fetch("/cart/"+id, init);
}

function checkout() {
    let header = new Headers();
    header.append("Content-Type", "application/json");
    let init = {
        credentials: 'same-origin',
        method: 'GET',
        headers: header,
    };
    fetch("/checkout", init);
}