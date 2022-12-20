from shared_power_bi import get_refresh_history
from shared_email import send_email
from shared_constants import REPORT_DISTRIBUTION_LIST
from datetime import date

refresh_history = get_refresh_history()

# print(refresh_history)
# Prepare email content

# -subject 
email_subject = f'Power BI refresh report: {date.today()}'

# -body - workspace, dataset name, refresh status (most recent), call to action?

high_level_report = ''

for workspace, datasets in refresh_history.items():
    high_level_report += f'<h2>{workspace}</h2>'
    high_level_report += """
        <table>
            <tr>
                <th>Workspace</th>
                <th>Refresh status</th>
                <th>Attempted refreshes</th>
                <th>Failed refreshes</th>
            </tr>
        """
    for dataset_name, refresh_history in datasets.items():
        if refresh_history:
            number_of_refresh_attempts = len(refresh_history)
            refresh_status = refresh_history[0]['status']
            failures = [refresh for refresh in refresh_history if refresh['status'] == 'Failed']
            number_of_failures = len(failures)
        else:
            number_of_refresh_attempts = '0'
            number_of_failures = 'n/a'
            refresh_status = 'None'
        high_level_report += f"""
                            <tr>
                                <td>{dataset_name}</td> 
                                <td>{refresh_status}</td> 
                                <td>{number_of_refresh_attempts}</td> 
                                <td>{number_of_failures}</td>
                            </tr>
                        """
    high_level_report +=  "</table>"

email_style = """
<style>
    table, th, td  {
        border: 1px solid black;
        border-collapse: collapse;
        }
</style>
"""

email_body = f"""
{email_style}
<h1>SLV Power BI Dataset Refresh Report: {date.today()}</h1>
<br></br>
{high_level_report}
"""

# Prepare attachment


# Build and send email

send_email(email_subject,REPORT_DISTRIBUTION_LIST,email_body)

# failures = []

# for key, value in refresh_history.items():
#     for k, v in value.items():
#         if v:
#             dataset_failures = [refresh_data for refresh_data in v if refresh_data['status'] == 'Failed']
#             failures.extend(dataset_failures)
#             for fail in failures:
#                 print(fail)


# print(failures)