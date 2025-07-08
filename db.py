import json
import uuid 

class Database:
    def __init__(self, db_file='user_data.json'):
        self.db_file = db_file
        self.load()

    def load(self):
        try:
            with open(self.db_file, 'r') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}

    def insert(self, email, password, name, mobile, city, state, country):
        # Check if email already exists in any user
        for user in self.data.keys():
            if user == email:
                return "exists"
        try:
            self.data[email] = {
                'password': password,
                'name': name,
                'mobile': mobile,
                'city': city,
                'state': state,
                'country': country
            }
            self.save()
            return True
        except Exception:
            return False

    def save(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_user_by_email(self, email):
        """Get user data by email"""
        if email in self.data:
            user_data = self.data[email].copy()
            user_data['email'] = email
            return user_data
        return None

    def update_user_phone(self, email, new_phone):
        """Update user's phone number"""
        if email in self.data:
            self.data[email]['mobile'] = new_phone
            self.save()
            return True
        return False
    
    def update_user_password(self, email, new_password):
        """Update user's password"""
        if email in self.data:
            self.data[email]['password'] = new_password
            self.save()
            return True
        return False
    
    def update_user_location(self, email, city, state, country):
        """Update user's location information"""
        if email in self.data:
            self.data[email]['city'] = city
            self.data[email]['state'] = state
            self.data[email]['country'] = country
            self.save()
            return True
        return False
    
    def update_user_name(self, email, new_name):
        """Update user's name"""
        if email in self.data:
            self.data[email]['name'] = new_name
            self.save()
            return True
        return False
