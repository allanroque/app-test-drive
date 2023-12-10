async function fetchStatusUpdates() {
    try {
        const response = await fetch('/api/status'); // Replace with your actual API endpoint
        const data = await response.json();
        updateTable(data);
    } catch (error) {
        console.error('Error fetching status updates:', error);
    }
}

function updateTable(data) {
    for (const [student, statuses] of Object.entries(data)) {
        const row = document.querySelector(`#nocTable tr[data-student='${student}']`);
        if (row) {
            Object.entries(statuses).forEach(([service, status], index) => {
                row.cells[index + 1].className = status === 'OK' ? 'status-ok' : 'status-fail';
                row.cells[index + 1].textContent = status;
            });
        }
    }
}

setInterval(fetchStatusUpdates, 30000); // Fetch updates every 30 seconds


