# MoEngage Documentation Analysis Tool

A two-agent system for analyzing and improving MoEngage documentation using Google's Gemini AI. The system consists of an analysis agent that evaluates documentation quality and a revision agent that generates improved versions based on the analysis.

## 🚀 Features

- **Agent 1 (Analyzer)**: Fetches and analyzes MoEngage documentation for readability, structure, completeness, and style adherence
- **Agent 2 (Reviser)**: Generates improved versions of documentation based on analysis suggestions
- **Headless Browser Integration**: Uses Selenium to fetch JavaScript-rendered content
- **AI-Powered Analysis**: Leverages Google Gemini 1.5 Flash for intelligent content evaluation

## 📋 Prerequisites

- Python 3.7+
- Google Chrome browser installed
- Google Gemini API key

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sarthakkurothe/Document-Analysis-tool
cd Document-Analysis-tool-main
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Create a `requirements.txt` file with the following dependencies:
```
selenium
beautifulsoup4
webdriver-manager
google-generativeai
python-dotenv
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

**⚠️ Important**: Never commit your `.env` file to version control. Add it to your `.gitignore`.

### 4. Get Your Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key to your `.env` file

### 5. Setting up the virtual environment

```
python -m venv venv
```

```
venv/scripts/activate
```

## 🏃‍♂️ Usage

### Running Agent 1 (Analysis)
```bash
python main.py
```
- Enter a MoEngage documentation URL when prompted
- The tool will fetch the content and analyze it
- Outputs:
  - `report.md`: Analysis and improvement suggestions
  - `original.md`: Original article content

### Running Agent 2 (Revision)
```bash
python reviser.py
```
- Requires `original.md` and `report.md` from Agent 1
- Outputs:
  - `revised.md`: Improved version of the documentation

## 🧠 Design Choices and Approach

### Architecture Decision
I chose a two-agent architecture to separate concerns:
- **Analysis Agent**: Focuses purely on evaluation and suggestion generation
- **Revision Agent**: Applies suggestions while maintaining content accuracy

### Style Guidelines Interpretation
The system evaluates documentation against four key criteria:
1. **Readability for non-technical marketers**: Ensures jargon is explained and concepts are accessible
2. **Structure and logical flow**: Checks for clear headings, progression, and organization
3. **Completeness and clarity of examples**: Verifies practical examples and step-by-step guidance
4. **Style adherence**: Maintains action-oriented, helpful tone consistent with technical documentation best practices

### Technical Approach
- **Selenium + BeautifulSoup**: Handles JavaScript-rendered content that simple HTTP requests miss
- **Content Cleaning**: Removes navigation, scripts, and styling elements to focus on core content
- **Structured Prompting**: Uses detailed prompts to ensure consistent, actionable analysis
- **File-based Workflow**: Saves intermediate outputs for transparency and debugging

## 🎯 Assumptions Made

1. **Target Audience**: Non-technical marketers are the primary users of MoEngage documentation
2. **Content Access**: Documentation is publicly accessible without authentication
3. **JavaScript Dependency**: Most modern documentation sites require JavaScript for full content loading
4. **Language**: All documentation is in English
5. **Format Consistency**: MoEngage follows standard web documentation patterns
6. **API Reliability**: Gemini API is available and responsive for analysis tasks

## 🚧 Challenges and Solutions

### Challenge 1: JavaScript-Rendered Content
**Problem**: Many documentation sites load content dynamically
**Solution**: Implemented Selenium with headless Chrome to render JavaScript before parsing

### Challenge 2: Content Noise
**Problem**: Web pages contain navigation, ads, and irrelevant elements
**Solution**: Aggressive content cleaning using BeautifulSoup to remove non-content elements

### Challenge 3: Consistent Analysis Quality
**Problem**: AI responses can vary in structure and depth
**Solution**: Detailed, structured prompts with specific criteria and output format requirements

### Challenge 4: Large Content Handling
**Problem**: Some documentation pages are very long
**Solution**: Current implementation processes full content; future improvement could implement chunking for extremely large documents

## 🔮 Future Improvements (Given More Time)

1. **Batch Processing**: Analyze multiple URLs in a single run
2. **Custom Style Guide Integration**: Allow users to upload custom style guidelines
3. **Interactive Revision**: Allow users to selectively apply suggestions
4. **Quality Metrics**: Implement scoring system for before/after comparison
5. **Multi-format Support**: Handle PDF and other documentation formats
6. **Error Recovery**: Better handling of network failures and content access issues

## 📁 Project Structure

```
moengage-doc-analyzer/
├── main.py              # Agent 1 - Analysis agent
├── reviser.py           # Agent 2 - Revision agent
├── .env                 # Environment variables (not committed)
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── original.md         # Original article content (generated)
├── report.md           # Analysis report (generated)
└── revised.md          # Improved documentation (generated)
```

## 📊 Example Outputs

### Example 1: MoEngage Integration Guide Analysis

**URL Analyzed**: `https://help.moengage.com/hc/en-us/articles/...`

**Key Findings**:
- Identified overly technical language in setup instructions
- Suggested additional code examples for API integration
- Recommended restructuring for better logical flow
- Found missing error handling documentation

**Improvements Made**:
- Simplified technical terminology
- Added step-by-step visual guides
- Reorganized content with clear headings
- Included troubleshooting section

### Example 2: Campaign Creation Documentation

**URL Analyzed**: `https://help.moengage.com/hc/en-us/articles/...`

**Key Findings**:
- Good overall structure but missing practical examples
- Some sections too brief for non-technical users
- Inconsistent tone across sections
- Missing prerequisites information

**Improvements Made**:
- Expanded examples with screenshots
- Added detailed explanations for each step
- Standardized friendly, helpful tone
- Created clear prerequisites section

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 🆘 Support

If you encounter issues:
1. Check that your Gemini API key is correctly set
2. Ensure Chrome browser is installed
3. Verify the target URL is accessible
4. Check the console output for specific error messages

For additional help, please open an issue in the repository.
