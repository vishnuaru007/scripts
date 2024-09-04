// Function to click the Apply button
function clickApplyButton() {
    // Define a selector that targets buttons with the shared classes 'btn' and 'btn-lg'
    const selector = 'button.btn.btn-lg';
    
    // Select all buttons that match the common selector
    const applyButtons = document.querySelectorAll(selector);
    let buttonClicked = false;
    
    // Iterate over each button to check if the text is "Apply"
    applyButtons.forEach(button => {
        if (button.textContent.trim() === 'Apply') {
            button.click();
            console.log(`Clicked Apply button with text "Apply"`);
            buttonClicked = true;
        }
    });

    if (!buttonClicked) {
        console.log('Apply button not found');
    }
}

// Set an interval to click the button every 5 seconds (5000 milliseconds)
setInterval(clickApplyButton, 5000);