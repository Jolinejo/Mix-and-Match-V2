# Mix and Match Website

Welcome to the Mix and Match website, a dynamic platform designed to offer personalized color suggestions for your uploaded images. Perfect for designers, artists, and anyone interested in color theory. Our website lets you sign up to create a personalized dashboard where all your uploads and color recommendations are saved.

[Check out the deployed website here](http://mariamibrahimaj.pythonanywhere.com/)

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Installation

1. **Clone the Repository**

   Start by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/mix-and-match.git
   cd mix-and-match
   ```

2. **Set Environment Variables**

   Set the required environment variables for the project:

   ```bash
   export API_KEY='your_gemini_api_key_here'
   export DATABASE_URL='your_database_url_here'
   ```

   Replace `'your_gemini_api_key_here'` with your actual Gemini API key and `'your_database_url_here'` with your database URL.

3. **Install Dependencies**

   Install the necessary dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   Launch the application by running:

   ```bash
   python app.py
   ```

   This will start the Flask server on your local machine.

### Usage

After starting the server, you can access the website by navigating to `127.0.0.1:5001` in your web browser. Here's what you can do on the Mix and Match website:

- **Sign Up/Sign In:** Create a new account or sign in with your existing credentials.
- **Upload Images:** Once signed in, you can start uploading images to receive personalized color suggestions.
- **Dashboard:** All your color suggestions are saved in your personalized dashboard for easy access and reference.

## Features

- User authentication (sign up and sign in)
- Image upload and processing
- Personalized color recommendations
- User dashboard to track uploads and suggestions

## Contributing

Contributions to the Mix and Match website are welcome! Please feel free to fork the repository, make changes, and submit pull requests. You can also open issues if you find bugs or have suggestions for improvements.

Enjoy using the Mix and Match website, and we look forward to seeing the beautiful and inspiring ways you use our color recommendations!
