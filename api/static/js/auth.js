document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    let response = await fetch("/api/api/token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    let data = await response.json();
    if (data.access) {
        localStorage.setItem("token", data.access);
        window.location.href = "/products/";
    } else {
        alert("Invalid Credentials");
    }
});
