document.getElementById('prediction-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const input = document.getElementById('features-input').value;
    let data;
    try {
        data = JSON.parse(input); // expects a JSON-style list: [1, 2, 3, ...]
    } catch (error) {
        document.getElementById('result').innerText = "Invalid input format. Please enter a valid list.";
        return;
    }

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input_data: data }),
    });

    const result = await response.json();
    document.getElementById('result').innerText = "Prediction: " + result.prediction;
});
