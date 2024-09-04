// Function to click the Apply or Not now button
function clickButton() {
    // Define a selector that targets buttons with the shared classes 'btn' and either 'btn-lg' or 'btn-default'
    const selector = 'button.btn.btn-lg, button.btn.btn-default';
    
    // Select all buttons that match the common selector
    const buttons = document.querySelectorAll(selector);
    let buttonClicked = false;
    
    // Iterate over each button to check if the text is "Apply" or "Not now"
    buttons.forEach(button => {
        if (button.textContent.trim() === 'Apply') {
            button.click();
            console.log(`Clicked Apply button with text "Apply"`);
            buttonClicked = true;
        } else if (button.textContent.trim() === 'Not now') {
            button.click();
            console.log(`Clicked Not now button with text "Not now"`);
            buttonClicked = true;
        }
    });

    if (!buttonClicked) {
        console.log('No Apply or Not now button found');
    }
}

// Set an interval to click the buttons every 5 seconds (5000 milliseconds)
setInterval(clickButton, 5000);
