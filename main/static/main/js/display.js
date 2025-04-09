
$(document).ready(function () {
  // Initialize date range picker for start date
  $('#date_received').datepicker({
    autoclose: true,
    format: 'yyyy-mm-dd'
  });

  // Initialize date range picker for end date
  $('#date_reviewed').datepicker({
    autoclose: true,
    format: 'yyyy-mm-dd'
  });
  updateCounts()
  // Handle date range selection
  $('#date_received, #date_reviewed').on('changeDate', function () {
    // Get the selected start and end dates
    var startDate = $('#date_received').datepicker('getFormattedDate');
    var endDate = $('#date_reviewed').datepicker('getFormattedDate');

    // Check if the startDate and endDate are valid date strings
    var isStartDateValid = isValidDate(startDate);
    var isEndDateValid = isValidDate(endDate);

    if (isStartDateValid && isEndDateValid) {
      // Convert the formatted date strings back to Date objects
      var startDateObj = new Date(startDate);
      var endDateObj = new Date(endDate);

      // Send the selected dates to the backend to fetch filtered data
      $.ajax({
        url: '/main/display_data/', // Update this URL to match your Django view endpoint
        data: { date_received: startDateObj.toISOString(), date_reviewed: endDateObj.toISOString() },
        success: function (response) {
          console.log('AJAX Response:', response);
          // Update table with response data
          $('#display_table').html(response.table_html);
          updateCounts();

          // Set the formatted date values back to the date input fields
          $('#date_received').val(startDate);
          $('#date_reviewed').val(endDate);
        }
      });
    } else {
      alert('Invalid date format. Please correct the date format and try again.');
    }
  });
});

function isValidDate(dateString) {
  const regex = /^(\d{4})-(\d{2})-(\d{2})$/;
  const matches = dateString.match(regex);

  if (!matches) {
    return false;
  }

  const year = matches[1];
  const month = matches[2] - 1; // Note: month is 0-indexed in JavaScript Date
  const day = matches[3];

  return new Date(year, month, day) instanceof Date && !isNaN(new Date(year, month, day));
}



// Function to update counts based on status and query type
function updateCounts() {

  var completedCount = 0;
  var onHoldCount = 0;
  var pendingCount = 0;
  var internalQueryCount = 0;
  var externalQueryCount = 0;
  var totalTransactions = 0;


  $('#display_table tbody tr:visible').each(function () {
    var status = $(this).find('td:eq(8)').text().trim().toLowerCase(); // Assuming status is in the 8th column (index 7)
    var queryType = $(this).find('td:eq(9)').text().trim().toLowerCase(); // Assuming query type is in the 9th column (index 8)

    // console.log('Status:', status);
    // console.log('Query Type:', queryType);

    if (status === 'complete') {
      completedCount++;
    } else if (status === 'hold') {
      onHoldCount++;
    } else if (status === 'in progress') {
      pendingCount++;
    }

    if (queryType === 'internal') {
      internalQueryCount++;
    } else if (queryType === 'external') {
      externalQueryCount++;
    }
    totalTransactions++;

  });

  // Update counts in the HTML
  $('#completedCount').text(' ' + completedCount);
  $('#onHoldCount').text(' ' + onHoldCount);
  $('#pendingCount').text('' + pendingCount);
  $('#internalQueryCount').text(' ' + internalQueryCount);
  $('#externalQueryCount').text(' ' + externalQueryCount);
  $('#transactionCount').text(' ' + totalTransactions);

}


document.addEventListener('DOMContentLoaded', function () {
  var imagePath = '/static/main/img/homebgpic.png'; // Adjust the path based on your project's static file configuration
  document.body.style.backgroundImage = "url('" + imagePath + "')";
});


function downloadCSV() {
  // Get the table data
  var table = document.getElementById('display_table');
  var rows = table.querySelectorAll('tr');

  // Create an array to store data
  var data = [];

  // Get headers
  var headers = [];
  for (var i = 0; i < table.rows[0].cells.length; i++) {
    headers.push(table.rows[0].cells[i].innerText);
  }
  data.push(headers);

  // Get rows data
  rows.forEach(function (row, index) {
    if (index !== 0) {
      var rowData = [];
      var cols = row.getElementsByTagName('td');

      for (var j = 0; j < cols.length; j++) {
        // Handle date formatting if needed
        var cellData = cols[j].innerText;
        if (j === 2 || j === 3) { // Assuming date columns are at index 2 and 3
          // Check if the cellData is a valid date string
          cellData = isValidDate(cellData) ? new Date(cellData).toISOString().split('T')[0] : '';
        }
        rowData.push(cellData);
      }

      data.push(rowData);
    }
  });

  // Convert data to CSV format
  var csvContent = data.map(e => e.join(",")).join("\n");

  // Create a Blob object
  var blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });

  // Create a download link
  var link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = 'table_data.csv';
  link.style.display = 'none';

  // Append the link to the document
  document.body.appendChild(link);

  // Trigger the click event to start the download
  link.click();

  // Remove the link from the document
  document.body.removeChild(link);
}

function isValidDate(dateString) {
  const regex = /^(\d{4})-(\d{2})-(\d{2})$/;
  const matches = dateString.match(regex);

  if (!matches) {
    return false;
  }

  const year = matches[1];
  const month = matches[2] - 1; // Note: month is 0-indexed in JavaScript Date
  const day = matches[3];

  return new Date(year, month, day) instanceof Date && !isNaN(new Date(year, month, day));
}
