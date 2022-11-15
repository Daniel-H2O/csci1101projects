window.addEventListener("load", function ()
{
    // Get button element references.
    let clickcounterElement = document.getElementById("click-counter");
    let clickbuttonElement = document.getElementById("click-button");

    // Counter value.
    let counter = 0;

    // Click button function.
    let clickbuttonFunction = function ()
    {
        // Increment counter.
        counter++;

        // Update click counter value.
        clickcounterElement.innerHTML = counter;
    };

    // Attach click button.
    clickbuttonElement.addEventListener("click", clickbuttonFunction);
});