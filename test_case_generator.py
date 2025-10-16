"""
AI-Powered Test Case Generator
Converts user stories into comprehensive test scenarios
"""

import os
import json
from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class TestCase(BaseModel):
    """Model for a single test case"""
    test_id: str = Field(description="Unique test case identifier (e.g., TC001)")
    title: str = Field(description="Brief test case title")
    description: str = Field(description="Detailed test case description")
    preconditions: List[str] = Field(description="List of preconditions")
    steps: List[str] = Field(description="Step-by-step test execution steps")
    expected_result: str = Field(description="Expected outcome")
    test_type: str = Field(description="Type: functional, negative, edge_case, or security")
    priority: str = Field(description="Priority: high, medium, or low")


class TestSuite(BaseModel):
    """Model for complete test suite"""
    user_story: str = Field(description="Original user story")
    test_cases: List[TestCase] = Field(description="List of generated test cases")
    coverage_summary: str = Field(description="Summary of test coverage")


class TestCaseGenerator:
    """AI Agent for generating test cases from user stories"""
    
    def __init__(self, api_key: str = None):
        """Initialize the test case generator"""
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "OpenAI API key not found. Set OPENAI_API_KEY environment variable "
                "or pass it as a parameter."
            )
        
        # Initialize LLM
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.3,
            api_key=self.api_key
        )
        
        # Setup output parser
        self.parser = PydanticOutputParser(pydantic_object=TestSuite)
        
        # Create prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert QA engineer specializing in test case design.
Your task is to analyze user stories and generate comprehensive test cases.

Generate test cases that cover:
- Positive scenarios (happy path)
- Negative scenarios (error handling)
- Edge cases (boundary conditions)
- Security considerations (if applicable)

For each test case, provide:
- Unique test ID
- Clear title and description
- Preconditions
- Detailed steps
- Expected results
- Test type and priority

{format_instructions}"""),
            ("user", """User Story:
{user_story}

Generate a comprehensive test suite with at least 5-8 test cases covering different scenarios.""")
        ])
    
    def generate_test_cases(self, user_story: str) -> TestSuite:
        """
        Generate test cases from a user story
        
        Args:
            user_story: The user story to generate test cases for
            
        Returns:
            TestSuite object containing all generated test cases
        """
        try:
            # Validate input
            if not user_story or not user_story.strip():
                raise ValueError("User story cannot be empty")
            
            # Format prompt
            formatted_prompt = self.prompt.format_messages(
                user_story=user_story,
                format_instructions=self.parser.get_format_instructions()
            )
            
            # Generate response
            response = self.llm.invoke(formatted_prompt)
            
            # Parse response
            test_suite = self.parser.parse(response.content)
            
            return test_suite
            
        except Exception as e:
            raise Exception(f"Error generating test cases: {str(e)}")
    
    def export_to_json(self, test_suite: TestSuite, filename: str = "test_cases.json"):
        """Export test suite to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(test_suite.dict(), f, indent=2, ensure_ascii=False)
            print(f"✅ Test cases exported to {filename}")
        except Exception as e:
            print(f"❌ Error exporting to JSON: {str(e)}")
    
    def print_test_suite(self, test_suite: TestSuite):
        """Pretty print the test suite"""
        print("\n" + "="*80)
        print(f"📋 USER STORY")
        print("="*80)
        print(test_suite.user_story)
        
        print("\n" + "="*80)
        print(f"🧪 GENERATED TEST CASES ({len(test_suite.test_cases)} cases)")
        print("="*80)
        
        for i, tc in enumerate(test_suite.test_cases, 1):
            print(f"\n[{tc.test_id}] {tc.title}")
            print(f"Type: {tc.test_type} | Priority: {tc.priority}")
            print(f"\nDescription: {tc.description}")
            
            if tc.preconditions:
                print("\nPreconditions:")
                for pre in tc.preconditions:
                    print(f"  • {pre}")
            
            print("\nSteps:")
            for j, step in enumerate(tc.steps, 1):
                print(f"  {j}. {step}")
            
            print(f"\nExpected Result: {tc.expected_result}")
            print("-" * 80)
        
        print(f"\n📊 COVERAGE SUMMARY")
        print("="*80)
        print(test_suite.coverage_summary)
        print("="*80 + "\n")


def main():
    """Main function with example usage"""
    
    # Example user stories for testing
    example_stories = [
        """
        As a user, I want to log in to the application using my email and password
        so that I can access my personal dashboard.
        
        Acceptance Criteria:
        - User can enter email and password
        - System validates credentials
        - Successful login redirects to dashboard
        - Failed login shows error message
        - Account locks after 3 failed attempts
        """,
        
        """
        As an admin, I want to export user data to CSV format
        so that I can analyze user activity offline.
        
        Acceptance Criteria:
        - Export button is visible only to admins
        - CSV includes all user fields (name, email, registration date, last login)
        - File downloads with timestamp in filename
        - Maximum 10,000 records per export
        """,
    ]
    
    try:
        # Initialize generator
        print("🚀 Initializing Test Case Generator...")
        generator = TestCaseGenerator()
        
        # Use first example story or get from user
        print("\nSelect a user story to generate test cases:")
        print("1. Login functionality")
        print("2. CSV export functionality")
        print("3. Enter custom user story")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == "1":
            user_story = example_stories[0]
        elif choice == "2":
            user_story = example_stories[1]
        elif choice == "3":
            print("\nEnter your user story (press Enter twice when done):")
            lines = []
            while True:
                line = input()
                if line == "" and lines and lines[-1] == "":
                    break
                lines.append(line)
            user_story = "\n".join(lines[:-1])  # Remove last empty line
        else:
            print("Invalid choice. Using default story.")
            user_story = example_stories[0]
        
        # Generate test cases
        print("\n⏳ Generating test cases...")
        test_suite = generator.generate_test_cases(user_story)
        
        # Display results
        generator.print_test_suite(test_suite)
        
        # Export to JSON
        export = input("Export to JSON? (y/n): ").strip().lower()
        if export == 'y':
            filename = input("Enter filename (default: test_cases.json): ").strip()
            if not filename:
                filename = "test_cases.json"
            generator.export_to_json(test_suite, filename)
        
    except ValueError as e:
        print(f"❌ Configuration Error: {str(e)}")
        print("\n💡 Setup Instructions:")
        print("1. Get your OpenAI API key from https://platform.openai.com/api-keys")
        print("2. Set it as environment variable: export OPENAI_API_KEY='your-key-here'")
        print("3. Or pass it when creating TestCaseGenerator(api_key='your-key')")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main()