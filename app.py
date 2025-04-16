from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


dummy_projects = [
    {
        "title": "Donation App",
        "description": "A donation platform that simplifies contributions to various causes.",
        "frontend": "React.js",
        "backend": "Node.js + Express + MongoDB",
        "image": "donation.jpg",
        "link": "https://github.com/vermakamya/Donate_food_Hacktoberfest-2022.git"
    },
    {
        "title": "Hospital Management System",
        "description": "System to manage patients, doctors, appointments, and billing.",
        "frontend": "HTML + CSS + Bootstrap",
        "backend": "PHP + MySQL",
        "image": "hospital.jpg",
        "link": "https://github.com/sumitkumar1503/hospitalmanagement.git"
    },
    {
        "title": "Contract Farming Platform",
        "description": "Connects farmers directly to buyers using smart contracts.",
        "frontend": "Angular",
        "backend": "Solidity (Smart Contracts) + Firebase",
        "image": "farming.jpg",
        "link": "https://github.com/RaunakMishr/KrishiMitr.git"
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
