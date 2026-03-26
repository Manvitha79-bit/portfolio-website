function submitForm() {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;

    if (!name || !email || !message) {
        document.getElementById("response").innerText = "Fill all fields!";
        return;
    }

    fetch('/submit', {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, email, message})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("response").innerText = data.message;
    });
}