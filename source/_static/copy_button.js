document.addEventListener("DOMContentLoaded", function () {
    let codeBlocks = document.querySelectorAll("div.highlight");

    codeBlocks.forEach(block => {
        // Create a button
        let button = document.createElement("button");
        button.className = "copy-button";
        button.innerHTML = "Copy";

        // Append the button to the code block
        block.appendChild(button);

        // Add click event to copy the text
        button.addEventListener("click", () => {
            let code = block.querySelector("pre").innerText;

            // Copy the text to the clipboard
            navigator.clipboard.writeText(code).then(() => {
                button.innerHTML = "Copied!";
                setTimeout(() => {
                    button.innerHTML = "Copy";
                }, 2000);
            });
        });
    });
});
