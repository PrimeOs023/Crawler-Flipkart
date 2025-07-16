import os
from flask import Flask, render_template, request
from crawler import check_product_availability, get_product_price, send_email       
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# Function to run scheduled product check
def scheduled_check():
    pin_code = os.environ.get("PIN_CODE", "000000")  # Default or set in env
    product_url = "https://www.example.com/product/dummy"
    availability = check_product_availability(product_url, pin_code)
    price = get_product_price(product_url)
    recipient_email = os.environ.get("RECIPIENT_EMAIL")
    if recipient_email:
        send_email(recipient_email, product_url, pin_code, availability, price)
    else:
        print("Error: RECIPIENT_EMAIL not configured in environment variables.")

# Start scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_check, 'interval', hours=1)
scheduler.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_availability', methods=['POST'])
def check_availability():
    pin_code = request.form['pin_code']
    # For now, use a dummy product URL. This will be dynamic later.
    product_url = "https://www.example.com/product/dummy"
    
    availability = check_product_availability(product_url, pin_code)
    price = get_product_price(product_url)

    if availability.startswith("Error:"):
        return render_template('result.html', pin_code=pin_code, availability=availability, price="N/A", error=True)
    if price.startswith("Error:"):
        return render_template('result.html', pin_code=pin_code, availability=availability, price=price, error=True)

    recipient_email = os.environ.get("RECIPIENT_EMAIL")
    if recipient_email is None:
        print("Error: RECIPIENT_EMAIL not configured in environment variables.")
    else:
        send_email(recipient_email, product_url, pin_code, availability, price)

    return render_template('result.html', pin_code=pin_code, availability=availability, price=price, error=False)

if __name__ == '__main__':
    app.run(debug=True)