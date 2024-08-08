base_html_template = """
{{ load_static|safe }}

<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>{{ report_base_data.report_name }}</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0px;
                padding: 0;
            }

            h1 {
                color: #333;
                border-bottom: 2px solid #666;
                padding-bottom: 10px;
            }

            h2 {
                color: #555;
                margin-top: 30px;
                border-bottom: 1px solid #ccc;
                padding-bottom: 5px;
            }

            .section-3, .section-2, .section-1 {
                display: flex;
            }

            .section-3 .char {
                flex: 1 0 33%;
                box-sizing: border-box;
                padding: 5px;
            }

            .section-2 .char {
                flex: 1 0 50%;
                box-sizing: border-box;
                padding: 5px;
            }

            .section-1 .char {
                flex: 1 0 100%;
                box-sizing: border-box;
                padding: 5px;
            }

            svg {
                width: 100%;
                height: auto;
                max-height: 100%;
            }
        </style>
    </head>

    <body>

        <h1>Report: {{ report_base_data.report_name }}</h1>
        <p>Description: {{ report_base_data.report_description }}</p>
        <p>Date: {{ report_base_data.report_date }}</p>

        {{ report_format|safe }}

    </body>

</html>
"""
