# Product Availability Crawler

This project is a basic web crawler that checks product availability for a given PIN code and sends email notifications. It uses Flask for the user interface and `smtplib` for sending emails.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd product_crawler
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set the following environment variables:**
    *   `SENDER_EMAIL`: Your email address (e.g., `your_email@gmail.com`).
    *   `SENDER_PASSWORD`: Your email password.
    *   `SMTP_SERVER`: The SMTP server for your email provider (e.g., `smtp.gmail.com` for Gmail).
    *   `SMTP_PORT`: The SMTP port number (e.g., `587` for Gmail with TLS).
    *   `RECIPIENT_EMAIL`: The email address to receive notifications.

    **Note:** You can set environment variables in your terminal or in your system settings. For example, in a bash terminal:
    ```bash
    export SENDER_EMAIL="your_email@gmail.com"
    export SENDER_PASSWORD="your_password"
    export SMTP_SERVER="smtp.gmail.com"
    export SMTP_PORT="587"
    export RECIPIENT_EMAIL="recipient_email@example.com"
    ```

## Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Access the application:** Open your web browser and go to `http://127.0.0.1:5000/` (or the address shown in your terminal).

3.  **Enter a PIN code:** Enter a PIN code in the input field and click "Check Availability".

4.  **Check the results:** The availability and price (dummy data for now) will be displayed on the results page. An email notification will also be sent to the specified recipient email address.

## Project Structure

```
product_crawler/
├── app.py          # Main Flask application file
├── crawler.py      # Web crawler logic and email sending function
├── requirements.txt # Python dependencies
└── templates/      # HTML templates
    ├── index.html    # Main page with PIN code input
    └── result.html   # Results page displaying availability and price
```

## Next Steps

*   Implement the actual web scraping logic for specific product websites.
*   Add price comparison functionality.
*   Improve error handling and logging.
*   Add more robust input validation.