document.querySelector("button").addEventListener("click", async () => {

    const url = document.getElementById("urlInput").value;

    // Show loading message
    document.getElementById("results").innerHTML = "<h2>Analyzing website...</h2>";

    try {

        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await response.json();

        if (data.error) {
            alert(data.error);
            document.getElementById("results").innerHTML = "";
            return;
        }

        document.getElementById("results").innerHTML = `
            <h2>Analysis Result</h2>

            <p><strong>Status:</strong> ${data.status}</p>

            <p><strong>Response Time:</strong> ${data.response_time} sec</p>

            <p><strong>Title:</strong> ${data.title}</p>

            <p><strong>Meta Description:</strong> ${data.meta_description}</p>

            <p><strong>H1 Count:</strong> ${data.h1_count}</p>

            <p><strong>Images Missing ALT:</strong> ${data.images_missing_alt}</p>

            <p><strong>Word Count:</strong> ${data.word_count}</p>
        `;

    }

    catch (err) {

        alert("Something went wrong.");
        document.getElementById("results").innerHTML = "";

    }

});