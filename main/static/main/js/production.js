document.addEventListener('DOMContentLoaded', function () {
    // Set current date for Date Reviewed field
    var dateReviewedField = document.getElementById('dateReviewed');
    var currentDate = new Date();
    var currentDateIST = currentDate.getFullYear() + '-' + ('0' + (currentDate.getMonth() + 1)).slice(-2) + '-' + ('0' + currentDate.getDate()).slice(-2);
    dateReviewedField.value = currentDateIST;
    dateReviewedField.setAttribute('readonly', 'readonly');

    var startTimeField = document.getElementById('startTime');

    var currentDateTime = new Date();
    var year = currentDateTime.getFullYear();
    var month = ('0' + (currentDateTime.getMonth() + 1)).slice(-2);
    var day = ('0' + currentDateTime.getDate()).slice(-2);
    var hours = ('0' + currentDateTime.getHours()).slice(-2);
    var minutes = ('0' + currentDateTime.getMinutes()).slice(-2);
    var seconds = ('0' + currentDateTime.getSeconds()).slice(-2);
    
    // Construct the date string in the required format for datetime-local input
    var currentDateTimeLocal = `${year}-${month}-${day}T${hours}:${minutes}:${seconds}`;
    
    startTimeField.value = currentDateTimeLocal;
    startTimeField.setAttribute('readonly', 'readonly');
    
    // Function to calculate the date difference in days
    function dateDiffInDays(a, b) {
        const diffInMs = b - a;
        return Math.floor(diffInMs / (24 * 60 * 60 * 1000));
    }

    // Set current date for Date Received field
    var dateReceivedField = document.getElementById('dateReceived');

    // Event listener for dateReceivedField change
    dateReceivedField.addEventListener('change', function () {
        // Calculate the difference in days
        var dateReceived = new Date(dateReceivedField.value);
        var dateReviewed = new Date(dateReviewedField.value);
        var dateDifference = dateDiffInDays(dateReceived, dateReviewed);

        // Update TAT field
        var tatField = document.getElementById('tat');
        if (dateDifference <= 5) {
            tatField.value = 'Met';
        } else {
            tatField.value = 'Not Met';
        }
    });

    // Trigger change event to calculate TAT initially
    dateReceivedField.dispatchEvent(new Event('change'));
});
