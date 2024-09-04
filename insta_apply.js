// Function to click the Apply button
function clickApplyButton() {
    // Define a list of potential selectors for the Apply button
    const selectors = [
        '.btn.btn-lg.btn-primary.new-btn',  // First selector
        'button[class*="apply"]',           // General selector if 'apply' is in class name
        'button:contains("Apply")',         // Text selector (jQuery or similar required for this)
        '#applyButton',                     // Example of an ID selector
        '[type="button"][value="Apply"]'    // Attribute selector example
    ];
    
    // Attempt to find and click the button using each selector
    let buttonClicked = false;
    for (let selector of selectors) {
        const applyButton = document.querySelector(selector);
        if (applyButton) {
            applyButton.click();
            console.log(`Clicked Apply button using selector: ${selector}`);
            buttonClicked = true;
            break;  // Stop after finding the first matching button
        }
    }

    if (!buttonClicked) {
        console.log('Apply button not found');
    }
}

// Set an interval to click the button every 5 seconds (5000 milliseconds)
setInterval(clickApplyButton, 5000);