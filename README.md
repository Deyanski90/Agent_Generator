# 🤖 AI Test Case Generator

An intelligent QA automation tool that converts user stories into comprehensive test scenarios using AI.

## 📋 Overview

This tool uses LangChain and OpenAI's GPT-4 to automatically generate detailed test cases from user stories, covering:
- ✅ Positive scenarios (happy path)
- ❌ Negative scenarios (error handling)
- 🔍 Edge cases (boundary conditions)
- 🔒 Security considerations

## 🚀 Setup (30 minutes)

### 1. Prerequisites
- Python 3.8 or higher
- OpenAI API account

### 2. Installation

```bash
# Clone or download the project
cd test-case-generator

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy the key (starts with `sk-...`)

### 4. Configure API Key

**Option A: Environment Variable (Recommended)**
```bash
# Windows (Command Prompt)
set OPENAI_API_KEY=sk-your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-your-api-key-here"

# Mac/Linux
export OPENAI_API_KEY=sk-your-api-key-here
```

**Option B: .env File**
```bash
# Create .env file in project root
echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
```

**Option C: Pass Directly in Code**
```python
generator = TestCaseGenerator(api_key="sk-your-api-key-here")
```

## 💻 Usage

### Basic Usage

```bash
python test_case_generator.py
```

The tool will:
1. Present example user stories
2. Let you choose or enter a custom story
3. Generate comprehensive test cases
4. Display results in terminal
5. Offer to export to JSON

### Using in Your Code

```python
from test_case_generator import TestCaseGenerator

# Initialize
generator = TestCaseGenerator()

# Your user story
user_story = """
As a user, I want to reset my password using my email
so that I can regain access to my account if I forget my password.

Acceptance Criteria:
- User enters email on reset page
- System sends reset link to email
- Link expires after 1 hour
- User can set new password
"""

# Generate test cases
test_suite = generator.generate_test_cases(user_story)

# Print results
generator.print_test_suite(test_suite)

# Export to JSON
generator.export_to_json(test_suite, "password_reset_tests.json")
```

## 📝 Example Output

### Input User Story:
```
As a user, I want to log in using my email and password
so that I can access my dashboard.

Acceptance Criteria:
- Valid credentials redirect to dashboard
- Invalid credentials show error
- Account locks after 3 failed attempts
```

### Generated Test Cases:

**TC001: Successful Login with Valid Credentials**
- Type: functional | Priority: high
- Steps: Enter valid email → Enter valid password → Click login → Verify redirect to dashboard
- Expected: User successfully logged in and redirected to personal dashboard

**TC002: Login Fails with Invalid Email**
- Type: negative | Priority: high
- Steps: Enter invalid email format → Enter password → Click login
- Expected: Error message displayed: "Invalid email format"

**TC003: Account Lockout After 3 Failed Attempts**
- Type: functional | Priority: high
- Steps: Attempt login with wrong password 3 times → Try again with correct password
- Expected: Account locked, message shown: "Account locked. Try again in 30 minutes"

**TC004: SQL Injection Prevention**
- Type: security | Priority: high
- Steps: Enter SQL injection payload in email field → Submit
- Expected: System sanitizes input, shows invalid email error

**TC005: Empty Field Validation**
- Type: negative | Priority: medium
- Steps: Leave email empty → Click login
- Expected: Validation error: "Email is required"

...and more!

## 📊 Output Format

### JSON Structure
```json
{
  "user_story": "Original user story text...",
  "test_cases": [
    {
      "test_id": "TC001",
      "title": "Test case title",
      "description": "Detailed description",
      "preconditions": ["Precondition 1", "Precondition 2"],
      "steps": ["Step 1", "Step 2", "Step 3"],
      "expected_result": "Expected outcome",
      "test_type": "functional|negative|edge_case|security",
      "priority": "high|medium|low"
    }
  ],
  "coverage_summary": "Summary of what scenarios are covered"
}
```

## 🧪 Testing (30 minutes)

### Test with Real Work Examples

1. **Grab a Recent User Story** from your current sprint
2. **Run the Generator**:
   ```bash
   python test_case_generator.py
   ```
3. **Choose Option 3** (custom story)
4. **Paste Your User Story**
5. **Review Generated Tests** - Check if they match what you'd write manually
6. **Compare Coverage** - Did it catch edge cases you'd include?

### Test Different Scenarios

Try these user story types:
- ✅ Simple CRUD operations
- ✅ Complex workflows with multiple steps
- ✅ API integrations
- ✅ User authentication flows
- ✅ Data validation scenarios

## ⚙️ Configuration

### Adjust AI Model

```python
# In test_case_generator.py, modify:
self.llm = ChatOpenAI(
    model="gpt-4o",  # Use GPT-4 for better quality
    temperature=0.3,  # Lower = more focused, Higher = more creative
    api_key=self.api_key
)
```

### Customize Test Case Template

Edit the system prompt in `__init__` method to:
- Add company-specific test case standards
- Include additional test types
- Modify priority levels
- Add custom fields

## 🎯 Use Cases

### Perfect For:
- ✅ Sprint planning (generate initial test ideas)
- ✅ New feature testing (ensure comprehensive coverage)
- ✅ Documentation (create test documentation quickly)
- ✅ Training (show new QA what good test cases look like)

### Not Ideal For:
- ❌ Replacing manual test design completely
- ❌ Highly specialized domain testing without customization
- ❌ Final test cases (always review and refine)

## 🔍 Limitations

1. **AI-Generated Content**: Review all test cases before using in production
2. **Cost**: OpenAI API calls cost money (~$0.01-0.05 per user story)
3. **Context**: AI may miss domain-specific edge cases
4. **Internet Required**: Needs connection to OpenAI API
5. **Generic**: May not follow company-specific test case formats (customization needed)

## 🐛 Troubleshooting

### "OpenAI API key not found"
- Set OPENAI_API_KEY environment variable
- Or pass key directly: `TestCaseGenerator(api_key="your-key")`

### "Rate limit exceeded"
- Wait a minute and try again
- Or upgrade your OpenAI plan

### "Connection error"
- Check your internet connection
- Verify OpenAI API status: https://status.openai.com

### Poor Quality Output
- Try using GPT-4 instead of GPT-4o-mini
- Adjust temperature (try 0.2 for more focused results)
- Improve user story details

## 📈 Future Enhancements

- [ ] Export to Excel/JIRA format
- [ ] Integrate with test management tools (TestRail, Zephyr)
- [ ] Add test case templates for different domains
- [ ] Support multiple languages
- [ ] Generate automation scripts from test cases
- [ ] Add test data generation

## 📄 License

MIT License - Feel free to use and modify for your needs

## 🤝 Contributing

Suggestions and improvements welcome! This is a learning project.

## 📞 Support

For issues or questions, check:
- LangChain docs: https://python.langchain.com/
- OpenAI API docs: https://platform.openai.com/docs

---

**⏱️ Total Setup Time**: ~30-45 minutes  
**💰 Cost per Generation**: ~$0.01-0.05  
**🎯 Time Saved**: 30-60 minutes per user story