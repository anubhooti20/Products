async function loadProducts() {
    let response = await fetch("/api/products/", {
        headers: { "Authorization": `Bearer ${localStorage.getItem("token")}` }
    });
    let products = await response.json();

    let productList = document.getElementById("productList");
    productList.innerHTML = "";
    products.forEach(p => {
        productList.innerHTML += `<div>
            <h3>${p.name}</h3>
            <p>${p.description}</p>
            <p>Price: $${p.price}</p>
            <button onclick="deleteProduct(${p.id})">Delete</button>
        </div>`;
    });
}

async function addProduct() {
    let name = document.getElementById("productName").value;
    let price = document.getElementById("productPrice").value;
    let description = document.getElementById("productDescription").value;

    let response = await fetch("/api/products/", {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${localStorage.getItem("token")}`,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, price, description, category: 1 })
    });

    if (response.ok) {
        loadProducts();
    } else {
        alert("Failed to add product");
    }
}

async function deleteProduct(id) {
    await fetch(`/api/products/${id}/`, {
        method: "DELETE",
        headers: { "Authorization": `Bearer ${localStorage.getItem("token")}` }
    });
    loadProducts();
}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "/";
}

document.addEventListener("DOMContentLoaded", loadProducts);
