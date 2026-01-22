function deleteEmployee(id) {
    if (!confirm("Are you sure you want to delete this employee?")) return;

    fetch(`/api/employees/${id}`, {
        method: "DELETE"
    })
    .then(response => {
        if (response.ok) {
            location.reload();
        } else {
            alert("Failed to delete employee");
        }
    });
}
function checkVisa(visaExpiry) {
    fetch("/checks/visa", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            visa_expiry: visaExpiry
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(`Visa Status: ${data.visa_status}`);
    });
}
