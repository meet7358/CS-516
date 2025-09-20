# Albumy - AI-Enhanced Photo Sharing Platform

> Enhanced version of the example application from *[Python Web Development with Flask](https://helloflask.com/en/book/1)* with machine learning capabilities for automatic image analysis and accessibility.

##  New AI Features

- ** Automatic Alt Text Generation**: AI-powered alternative text for all uploaded images to improve accessibility
- ** ML-Powered Tagging**: Intelligent object detection and tagging for better photo organization
- ** Smart Image Search**: Search photos using natural language terms across AI-generated content
- ** Accessibility First**: All images include proper alt text for screen readers and assistive technologies

##  Requirements

- **Python**: 3.10 or 3.11 (recommended)
- **Virtual Environment**: venv or virtualenv
- **Azure Computer Vision API**: For AI features (free tier available)
- **Dependencies**: See requirements.txt

## Installation

### 1. Clone the repository:
```bash
$ git clone https://github.com/greyli/albumy.git
$ cd albumy
```

### 2. Create and activate virtual environment:

**With venv/virtualenv + pip:**
```bash
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```

**Or with Pipenv:**
```bash
$ pipenv install --dev
$ pipenv shell
```

### 3. Environment Setup

Create a `.env` file in the project root with the following variables:

```bash
# Azure Computer Vision API (REQUIRED for AI features)
AZURE_VISION_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_VISION_KEY=your_api_key_here

# Flask Configuration
FLASK_APP=albumy
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

# Database
DATABASE_URL=sqlite:///data-dev.db

# Email Configuration (optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

# Admin Configuration
ALBUMY_ADMIN_EMAIL=admin@example.com
```

**Note**: Copy `.env.example` to `.env` and fill in your actual values.

### 4. Azure Computer Vision Setup (Required for AI Features)

1. **Create Azure Account**: Go to [Azure Portal](https://portal.azure.com/)
2. **Create Computer Vision Resource**:
   - Search for "Computer Vision" in Azure Portal
   - Click "Create" and fill in the details
   - Choose "Free F0" pricing tier (1000 transactions/month free)
3. **Get API Credentials**:
   - Go to your Computer Vision resource
   - Navigate to "Keys and Endpoint"
   - Copy the "Key 1" and "Endpoint" values
4. **Update .env file**:
   ```bash
   AZURE_VISION_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
   AZURE_VISION_KEY=your_actual_api_key_here
   ```

**Alternative**: If you don't want to set up Azure, the app will use mock AI responses for development.

### 5. Run the application:

```bash
$ flask forge  # Generate fake data
$ flask run
* Running on http://127.0.0.1:5000/
```

### 6. Test Account:
- **Email**: `admin@helloflask.com`
- **Password**: `helloflask`

##  AI Features Implementation

### How It Works
1. **Upload Process**: When users upload photos, the system automatically calls Azure Computer Vision API
2. **AI Analysis**: The API analyzes the image and generates:
   - **Alt Text**: Descriptive text for accessibility (e.g., "A beautiful ocean scene with waves and blue water")
   - **ML Tags**: Object detection tags (e.g., "ocean", "water", "waves", "blue")
3. **Database Storage**: AI-generated content is stored in new database fields (`alt_text`, `tags_ml`)
4. **User Interface**: AI descriptions and tags are displayed in the photo interface
5. **Search Integration**: Users can search photos using natural language terms

### Key Files Modified:
- **`albumy/models.py`**: Added `alt_text` and `tags_ml` fields to Photo model
- **`ml/vision.py`**: Azure Computer Vision API integration
- **`albumy/blueprints/main.py`**: AI analysis on upload, enhanced search functionality
- **Templates**: Updated to display AI content and include alt attributes

### Testing the AI Features:
1. **Upload a photo** - AI will automatically generate alt text and tags
2. **Search photos** - Use natural language terms like "ocean", "car", "dog"
3. **Check accessibility** - All images now have proper alt text for screen readers
4. **View AI content** - AI descriptions and tags are displayed below each photo

## Dependencies

### New Dependencies Added for AI Features:
- `python-dotenv`: Environment variable management
- `requests`: HTTP requests for Azure Computer Vision API

### Core Dependencies:
- `flask`: Web framework
- `flask-sqlalchemy`: Database ORM
- `flask-login`: User authentication
- `flask-wtf`: Form handling
- `pillow`: Image processing
- And more... (see requirements.txt)

##  Troubleshooting

### Common Issues:

1. **"ModuleNotFoundError: No module named 'flask_login'"**
   ```bash
   # Make sure virtual environment is activated
   env\Scripts\activate  # Windows
   source env/bin/activate  # Linux/Mac
   pip install -r requirements.txt
   ```

2. **"Azure Vision API not configured"**
   - This is normal if you haven't set up Azure credentials
   - The app will use mock AI responses for development
   - To use real AI: Set up Azure Computer Vision and add credentials to `.env`

3. **Photos not showing after upload**
   - Check if virtual environment is activated
   - Run `flask forge` to generate test data
   - Check browser console for errors

4. **Database issues**
   - Delete `data-dev.db` and run `flask forge` to recreate database
   - Make sure all dependencies are installed

