$(document).ready(function() {
    var table = $('#dt-select').DataTable({
        data: dataSet,
        columns: [{
                title: "Name"
            },
            {
                title: "Position"
            },
            {
                title: "Office"
            },
            {
                title: "Extn."
            },
            {
                title: "Start date"
            },
            {
                title: "Salary"
            }
        ],

        dom: 'Bfrtip',
        select: true,
        buttons: [{
                text: 'Select all',
                action: function() {
                    table.rows().select();
                }
            },
            {
                text: 'Select none',
                action: function() {
                    table.rows().deselect();
                }
            }
        ]
    });
});