# AI Tools Hub - Flask Web Application

A modern, responsive Flask web application that serves as a platform for AI-powered tools and user management. The application features user authentication, profile management, and a dashboard for accessing various AI tools.

## 🚀 Features

### 🔐 **Authentication System**
- **User Registration** with comprehensive form validation
- **Smart Login System** with specific error messages
- **Password Recovery** (Forgot Password functionality)
- **Session Management** for secure user sessions
- **Logout** functionality

### 👤 **Profile Management**
- **View Profile** - Display all user information
- **Update Phone Number** - Change mobile number
- **Update Password** - Secure password change with validation
- **Update Location** - Change city, state, and country
- **Success/Error Messages** for all operations

### 🎯 **Dashboard & AI Tools**
- **Modern Dashboard** with tool cards
- **AI Tool Preview** including:
  - 📝 Text Summarizer
  - 🌍 Language Translator
  - 💼 LinkedIn Post Generator
  - 📊 Data Analysis Tool
- **Under Development Pages** with feature previews
- **Notification System** for tool launches

### 📱 **Responsive Design**
- **Mobile-First Approach**
- **Modern UI/UX** with gradient backgrounds
- **Professional Styling** with hover effects
- **Consistent Theming** across all pages

### 📄 **Legal Pages**
- **Privacy Policy** with comprehensive content
- **Terms of Service** with detailed terms
- **Professional Layout** for legal content

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: JSON-based file storage
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Styling**: Custom CSS with modern design patterns
- **Session Management**: Flask Sessions

## 📁 Project Structure

```
Flask_Webapp/
├── app.py                      # Main Flask application
├── db.py                       # Database operations class
├── user_data.json             # User data storage
├── README.md                  # This file
├── static/
│   └── css/
│       ├── content.css        # Privacy/Terms pages styling
│       ├── dashboard.css      # Dashboard styling
│       ├── forgot_password.css # Forgot password page styling
│       ├── index.css          # Homepage styling
│       ├── login.css          # Login page styling
│       ├── profile.css        # Profile and update pages styling
│       ├── register.css       # Registration page styling
│       └── under_development.css # Under development pages styling
└── templates/
    ├── dashboard.html         # User dashboard
    ├── forget_pass.html       # Forgot password page
    ├── index.html             # Homepage
    ├── login.html             # Login page
    ├── privacy.html           # Privacy policy
    ├── profile.html           # User profile display
    ├── register.html          # User registration
    ├── term.html              # Terms of service
    ├── under_development.html # Tool development status
    ├── update_location.html   # Location update form
    ├── update_password.html   # Password update form
    └── update_phone.html      # Phone update form
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Flask

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd Flask_Webapp
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 📋 Usage Guide

### 🔑 **Getting Started**
1. **Visit Homepage** - Navigate to the main page to see feature overview
2. **Register Account** - Create a new account with your details
3. **Login** - Sign in with your credentials
4. **Explore Dashboard** - Access AI tools and profile management

### 👤 **Profile Management**
1. **View Profile** - Click "My Profile" from dashboard
2. **Update Information**:
   - Phone: Click "Update Phone Number"
   - Password: Click "Update Password" (requires current password)
   - Location: Click "Update City, State & Country"

### 🔧 **AI Tools**
- Currently in development phase
- Click any tool to see development status
- Sign up for notifications when tools are ready

## 🔐 Security Features

- **Password Validation** (minimum 6 characters)
- **Current Password Verification** for password changes
- **Session-based Authentication**
- **Input Validation** for all forms
- **SQL Injection Prevention** (JSON-based storage)

## 📱 Responsive Design

The application is fully responsive and works on:
- **Desktop** (1200px+)
- **Tablet** (768px - 1199px)
- **Mobile** (320px - 767px)

## 🎨 Design Features

- **Modern Gradient Backgrounds**
- **Card-based Layouts**
- **Hover Effects and Animations**
- **Professional Typography**
- **Consistent Color Scheme**
- **Accessible Design Elements**

## 🗃️ Database Schema

The application uses JSON file storage with the following structure:

```json
{
    "user@example.com": {
        "password": "hashedpassword",
        "name": "User Name",
        "mobile": "1234567890",
        "city": "City Name",
        "state": "State Name",
        "country": "Country Code"
    }
}
```

## 🛣️ API Routes

### **Authentication Routes**
- `GET /` - Homepage
- `GET /login` - Login page
- `POST /perform_login` - Process login
- `GET /register` - Registration page
- `POST /perform_registration` - Process registration
- `GET /logout` - Logout user
- `GET /forgot-password` - Forgot password page
- `POST /reset_password` - Process password reset

### **Profile Routes**
- `GET /profile` - View profile
- `GET /update_phone` - Phone update form
- `POST /perform_phone_update` - Process phone update
- `GET /update_password` - Password update form
- `POST /perform_password_update` - Process password update
- `GET /update_location` - Location update form
- `POST /perform_location_update` - Process location update

### **Dashboard Routes**
- `GET /dashboard` - User dashboard

### **AI Tool Routes**
- `GET /text-summarizer` - Text Summarizer (under development)
- `GET /translator` - Language Translator (under development)
- `GET /linkedin-generator` - LinkedIn Post Generator (under development)
- `GET /data-analysis` - Data Analysis Tool (under development)
- `POST /notify_me` - Sign up for tool notifications

### **Legal Routes**
- `GET /privacy` - Privacy policy
- `GET /terms` - Terms of service

## 🔄 Error Handling

The application includes comprehensive error handling:

- **Login Errors**: Specific messages for wrong email/password
- **Registration Errors**: Email already exists validation
- **Update Errors**: Form validation and database error handling
- **Session Errors**: Automatic redirect to login for unauthorized access

## 🚧 Future Enhancements

### **AI Tools Implementation**
- Text Summarizer with file upload
- Multi-language translator
- LinkedIn post generator with templates
- Data analysis with visualization

### **Additional Features**
- Email verification
- Password reset via email
- Profile picture upload
- Admin dashboard
- User activity logs


## 📄 License

This project is open source and available under the [MIT License](LICENSE).


---

**Made with ❤️ using Flask and modern web technologies**
