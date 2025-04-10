from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


dummy_projects = [
    {
        "title": "Donation App",
        "description": "A MERN-based donation platform for seamless contributions.",
        "image": "donation.jpg",
        "link": "https://github.com/supabase-community/donate-app"
    },
    {
        "title": "Hospital Management System",
        "description": "Manages patient and doctor records efficiently.",
        "image": "hospital.jpg",
        "link": "https://github.com/mohit-coding/hospital-management"
    },
    {
        "title": "Contract Farming Platform",
        "description": "Connects farmers with buyers via smart contracts.",
        "image": "farming.jpg",
        "link": "https://github.com/kisanmitr/contract-farming"
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=dummy_projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))
    return render_template('contact.html')

@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    return render_template('success.html', name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(debug=True)
