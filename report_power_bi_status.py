from shared_power_bi import get_refresh_history
from shared_email import send_email
from datetime import datetime


# Get refresh history
# refresh_history = get_refresh_history()


# Prepare email content

# -subject 
email_subject = f'Power BI dataset refresh report: {datetime.today()}'
print(email_subject)

# -body - workspace, dataset name, refresh status (most recent), call to action?

email_body = r"""

"""

# Prepare attachment


# Build and send email


# failures = []

# for key, value in refresh_history.items():
#     for k, v in value.items():
#         if v:
#             dataset_failures = [refresh_data for refresh_data in v if refresh_data['status'] == 'Failed']
#             failures.extend(dataset_failures)
#             for fail in failures:
#                 print(fail)


# print(failures)