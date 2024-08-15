# CVE Notifications

This document outlines the process of notifying users about significant Common Vulnerabilities and Exposures (CVEs). It includes the criteria for sending notifications, the configuration required, and examples of the notification process.

## Notification Process

The notification process involves the following steps:

1. **Loading User Preferences**: Load user preferences from the database.
2. **Checking for Significant CVEs**: Check the analyzed data for significant CVEs related to the user's subscribed software.
3. **Sending Notifications**: Send email notifications to users about the significant CVEs.

## Criteria for Sending Notifications

To send notifications, the following criteria are used:

1. **User Preferences**:
   - Users can subscribe to notifications for specific software.
   - Notifications are sent based on the software specified in the user's preferences.

2. **Significant CVEs**:
   - Notifications are only sent for CVEs that have been determined to be significant based on their CVSS scores and impact metrics.

## Configuration

To configure the notification system, the following environment variables need to be set in the `.env` file:

```env
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=your_email@example.com
SMTP_PASSWORD=your_email_password
EMAIL_SENDER=your_email@example.com
