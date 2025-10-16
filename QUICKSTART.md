# ⚡ Quick Start Guide (10 Minutes to First Test Cases)

Follow these steps to get your AI test case generator running in 10 minutes!

## 📦 Step 1: Download Files (1 min)

Download these 5 files to a new folder:
1. `test_case_generator.py` - Main application
2. `requirements.txt` - Dependencies
3. `verify_setup.py` - Setup verification
4. `.env.example` - Environment configuration template
5. `README.md` - Full documentation

## 🔧 Step 2: Install Dependencies (3 min)

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed langchain-0.3.7 langchain-openai-0.2.8 ...
```

## 🔑 Step 3: Get OpenAI API Key (3 min)

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-proj-...`)
5. **IMPORTANT**: Save it somewhere - you won't see it again!

**⚠️ Note**: You'll need to add a payment method to your OpenAI account. Each test case generation costs ~$0.01-0.05.

## 🎯 Step 4: Configure API Key (1 min)

**Choose ONE method:**

### Method A: Environment Variable (Recommended for testing)
```bash
# Windows (Command Prompt)
set OPENAI_API_KEY=sk-proj-your-actual-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-proj-your-actual-key-here"

# Mac/Linux
export OPENAI_API_KEY=sk-proj-your-actual-key-here
```

### Method B: .env File (Recommended for regular use)
```bash
# Copy example file
cp .env.example .env

# Edit .env file and replace with your actual key
# OPENAI_API_KEY=sk-proj-your-actual-key-here
```

## ✅ Step 5: Verify Setup (1 min)

```bash
python verify_setup.py
```

**You should see:**
```
✅ Python version: 3.x.x
✅ langchain installed
✅ langchain_openai installed
✅ pydantic installed
✅ openai installed
✅ OpenAI API Key found: sk-proj-...xyz
✅ Test case generator module loaded successfully
✅ Test case generator initialized successfully

✅ ALL CHECKS PASSED! You're ready to generate test cases!
```

**If you see ❌ errors**, read the suggestions and fix them before continuing.

## 🚀 Step 6: Generate Your First Test Cases (1 min)

```bash
python test_case_generator.py
```

**What happens:**
1. Menu appears with 3 options
2. Choose option `1` (Login example) for your first try
3. Wait ~10-30 seconds while AI generates test cases
4. See comprehensive test cases printed in your terminal
5. Choose `y` to export to JSON file

**Sample output:**
```
🧪 GENERATED TEST CASES (8 cases)
================================================================================

[TC001] Successful Login with Valid Credentials
Type: functional | Priority: high

Description: Verify that a user can successfully log in...

Preconditions:
  • User account exists in the system
  • User has valid email and password

Steps:
  1. Navigate to login page
  2. Enter valid email address
  3. Enter correct password
  4. Click "Login" button
  5. Verify redirect to dashboard

Expected Result: User successfully logged in and redirected to dashboard with welcome message

[TC002] Login Fails with Invalid Email Format
...
```

## 🎉 Success! What's Next?

### Try with Your Own User Story
```bash
python test_case_generator.py
# Choose option 3
# Paste your own user story
```

### Example User Story to Try:
```
As a customer, I want to add items to my shopping cart
so that I can purchase multiple products at once.

Acceptance Criteria:
- Click "Add to Cart" button on product page
- Cart icon shows updated item count
- Can view cart contents
- Can remove items from cart
- Total price updates automatically
```

## 📊 Understanding the Output

Each test case includes:
- **Test ID**: Unique identifier (TC001, TC002...)
- **Title**: Brief description
- **Type**: functional, negative, edge_case, or security
- **Priority**: high, medium, or low
- **Preconditions**: What must be true before testing
- **Steps**: Detailed execution steps
- **Expected Result**: What should happen

## 💡 Pro Tips

### Get Better Results
1. **Be Specific**: Include detailed acceptance criteria in your user story
2. **Mention Edge Cases**: If you know specific scenarios, mention them
3. **Include Constraints**: Add technical limitations or business rules

### Save Money
- Use GPT-4o-mini (default) instead of GPT-4 for most cases
- Each generation costs ~$0.01-0.05
- Review and refine outputs instead of regenerating multiple times

### Integrate with Your Workflow
1. Generate initial test ideas during sprint planning
2. Export to JSON and import into your test management tool
3. Review and customize test cases before using
4. Use as training material for new QA team members

## 🐛 Common Issues

### "ModuleNotFoundError: No module named 'langchain'"
**Fix**: Run `pip install -r requirements.txt`

### "OpenAI API key not found"
**Fix**: Set the environment variable (see Step 4)

### "Rate limit exceeded"
**Fix**: Wait 60 seconds and try again, or check your OpenAI usage limits

### "Connection timeout"
**Fix**: Check your internet connection and try again

## 📖 Next Steps

1. ✅ Read the full `README.md` for advanced features
2. ✅ Try different user story types (API, security, data validation)
3. ✅ Customize the prompt template for your company's standards
4. ✅ Integrate with your test management tools
5. ✅ Share with your team!

## 🎯 Assessment Checklist

Before submitting your project:

**Technical (40%)**
- ✅ Code runs without errors
- ✅ Generates valid test cases
- ✅ Uses LangChain properly
- ✅ Structured output (Pydantic models)

**Usefulness (30%)**
- ✅ Covers positive, negative, and edge cases
- ✅ Test cases are realistic and actionable
- ✅ Saves time compared to manual creation
- ✅ Outputs match QA standards

**Code Quality (20%)**
- ✅ Clean, readable code structure
- ✅ Error handling for API failures
- ✅ Input validation
- ✅ Clear function documentation

**Documentation (10%)**
- ✅ README with setup instructions
- ✅ Usage examples
- ✅ Known limitations documented
- ✅ Troubleshooting guide

---

**Total Time**: ~10 minutes setup + ~1 minute per user story  
**Cost**: ~$0.01-0.05 per user story  
**Time Saved**: 30-60 minutes per user story

Happy testing! 🚀